"""
Test goes here

"""

# test_main.py
import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def sample_data():
    return pd.DataFrame(
        {
            "Category": ["Electronics", "Clothing", "Electronics", "Books"],
            "Qty": [5, 10, 15, 20],
            "Amount": [100, 200, 300, 400],
            "SKU": ["A1", "B2", "A1", "C3"],
            "Status": ["Shipped", "Cancelled", "Shipped", "Shipped"],
            "Fulfilment": ["FBA", "FBA", "Third-Party", "FBA"],
            "Courier Status": ["Delivered", "Pending", "Delivered", "Cancelled"],
            "Date": pd.to_datetime(
                ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"]
            ),
        }
    )


def test_category_stats(sample_data):
    category_stats = sample_data.groupby("Category")[["Qty", "Amount"]].describe()
    assert "Qty" in category_stats.columns
    assert "Amount" in category_stats.columns


def test_top_selling_items(sample_data):
    top_sellers = sample_data.groupby("SKU").agg(
        total_qty=("Qty", "sum"), total_revenue=("Amount", "sum")
    )
    threshold = top_sellers["total_revenue"].quantile(0.9)
    top_selling_skus = top_sellers[top_sellers["total_revenue"] >= threshold].index
    assert len(top_selling_skus) > 0


def test_fulfillment_counts(sample_data):
    fulfillment_counts = sample_data["Fulfilment"].value_counts()
    assert "FBA" in fulfillment_counts
    assert fulfillment_counts["FBA"] == 2


def test_date_conversion(sample_data):
    sample_data["Date"] = pd.to_datetime(sample_data["Date"], errors="coerce")
    assert sample_data["Date"].dtype == "datetime64[ns]"
