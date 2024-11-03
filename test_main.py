# test_main.py

import pandas as pd
import pytest
from main import calculate_category_stats, calculate_top_sellers, forecast_demand


# Sample test data
@pytest.fixture
def sample_data():
    return pd.DataFrame(
        {
            "Category": ["Electronics", "Clothing", "Books"],
            "Qty": [10, 20, 30],
            "Amount": [100.0, 200.0, 300.0],
            "SKU": ["A1", "B2", "C3"],
            "Status": ["Shipped", "Cancelled", "Shipped"],
            "Fulfilment": ["FBA", "FBA", "Third-Party"],
            "Courier Status": ["Delivered", "Pending", "Cancelled"],
            "Date": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
        }
    )


def test_calculate_category_stats(sample_data):
    category_stats = calculate_category_stats(sample_data)
    assert "Qty" in category_stats.columns.levels[1]
    assert "Amount" in category_stats.columns.levels[1]


def test_calculate_top_sellers(sample_data):
    top_sellers = calculate_top_sellers(sample_data)
    assert not top_sellers.empty


def test_forecast_demand():
    # Create mock daily demand data
    daily_demand = pd.Series(
        [10, 12, 15, 10, 20, 25, 30], index=pd.date_range(start="2024-01-01", periods=7)
    )
    forecast = forecast_demand(daily_demand)
    assert "yhat" in forecast.columns
    assert len(forecast) > len(
        daily_demand
    )  # Check forecast goes beyond historical data
