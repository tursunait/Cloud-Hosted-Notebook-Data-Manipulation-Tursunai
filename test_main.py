import pytest
import pandas as pd
from main import (
    load_data,
    calculate_category_stats,
    plot_category_count,
    plot_status_count,
    calculate_top_sellers,
    forecast_demand,
)

# Sample data for testing
sample_data = {
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing"],
    "SKU": ["AN201-RED-M", "AN202-ORANGE-S", "AN201-RED-XL", "SET449-KR-NP-S"],
    "Qty": [10, 5, 15, 20],
    "Amount": [100.0, 50.0, 150.0, 200.0],
    "Status": ["Shipped", "Cancelled", "Shipped", "Unshipped"],
    "Fulfilment": ["Amazon", "Merchant", "Amazon", "Merchant"],
    "Date": ["04-01-22", "04-02-22", "04-03-22", "04-04-22"],
}

sample_df = pd.DataFrame(sample_data)


def test_load_data(monkeypatch):
    # Mock pd.read_csv to return sample_df
    def mock_read_csv(filepath):
        return sample_df

    monkeypatch.setattr(pd, "read_csv", mock_read_csv)

    # Run load_data with a fake file path
    df = load_data("fake_path.csv")
    pd.testing.assert_frame_equal(df, sample_df)


def test_calculate_category_stats():
    result = calculate_category_stats(sample_df)
    assert "Qty" in result.columns
    assert "Amount" in result.columns
    assert result.loc["Electronics", ("Qty", "mean")] == 12.5  # (10 + 15) / 2


def test_calculate_top_sellers():
    result = calculate_top_sellers(sample_df)
    assert "total_qty" in result.columns
    assert "total_revenue" in result.columns
    assert result["total_revenue"].min() >= result["total_revenue"].quantile(0.9)


def test_plot_category_count():
    # Just check if it runs without error
    try:
        plot_category_count(sample_df)
    except Exception as e:
        pytest.fail(f"plot_category_count raised an exception: {e}")


def test_plot_status_count():
    # Just check if it runs without error
    try:
        plot_status_count(sample_df)
    except Exception as e:
        pytest.fail(f"plot_status_count raised an exception: {e}")


def test_forecast_demand():
    # Prepare daily demand data for forecast test
    daily_demand = sample_df.groupby("Date")["Qty"].sum()

    # Check if forecast runs without errors and returns the correct structure
    try:
        forecast = forecast_demand(daily_demand)
        assert "ds" in forecast.columns
        assert "yhat" in forecast.columns
    except Exception as e:
        pytest.fail(f"forecast_demand raised an exception: {e}")


if __name__ == "__main__":
    pytest.main()
