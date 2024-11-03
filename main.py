# main.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet


# Load data function
def load_data(filepath):
    """Load data from a specified CSV file."""
    return pd.read_csv(filepath)


# Analysis functions
def calculate_category_stats(df):
    """Calculate descriptive statistics by Category, handling NaN values."""
    if df[["Qty", "Amount"]].isnull().values.any():
        df = df.dropna(subset=["Qty", "Amount"])
    return df.groupby("Category")[["Qty", "Amount"]].describe()


def plot_category_count(df):
    """Generate a count plot for Category."""
    if "Category" in df.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x="Category", order=df["Category"].value_counts().index)
        plt.title("Sales Count by Category")
        plt.xlabel("Category")
        plt.ylabel("Sales Count")
        plt.xticks(rotation=45)
        plt.show()
    else:
        print("Category column not found in DataFrame.")


def plot_status_count(df):
    """Generate a count plot for Status."""
    if "Status" in df.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x="Status", order=df["Status"].value_counts().index)
        plt.title("Sales Count by Status")
        plt.xlabel("Status")
        plt.ylabel("Sales Count")
        plt.xticks(rotation=45)
        plt.show()
    else:
        print("Status column not found in DataFrame.")


def calculate_top_sellers(df):
    """Calculate top-selling items based on a threshold, handling NaN values."""
    df = df.dropna(subset=["Qty", "Amount"])
    top_sellers = df.groupby("SKU").agg(
        total_qty=("Qty", "sum"), total_revenue=("Amount", "sum")
    )
    threshold = top_sellers["total_revenue"].quantile(0.9)
    return top_sellers[top_sellers["total_revenue"] >= threshold]


def forecast_demand(daily_demand):
    """Generate a 30-day demand forecast using Prophet."""
    if daily_demand.shape[1] >= 2:
        demand_data = daily_demand.reset_index()
        demand_data.columns = ["ds", "y"]

        model = Prophet()
        model.fit(demand_data)

        future_dates = model.make_future_dataframe(periods=30)
        forecast = model.predict(future_dates)

        model.plot(forecast)
        plt.title("Demand Forecast for Top-Selling Items")
        plt.xlabel("Date")
        plt.ylabel("Forecasted Quantity")
        plt.show()
        return forecast
    else:
        print("Input data does not have the required format for Prophet.")
