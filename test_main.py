"""
Test goes here

"""

import pytest
import pandas as pd
from mylib.lib import calculate_mean, calculate_median, calculate_std_dev

# Creating a DataFrame to use for tests
df = pd.DataFrame({"values": [1, 2, 3, 4, 5]})
col = "values"


def test_calculate_mean():
    assert calculate_mean(df, col) == 3


def test_calculate_median():
    assert calculate_median(df, col) == 3


def test_calculate_std_dev():
    assert calculate_std_dev(df, col) == pytest.approx(1.58, rel=1e-2)


def test_calculate_mean_empty():
    df_empty = pd.DataFrame({"values": []})
    assert calculate_mean(df_empty, "values") is None


def test_calculate_median_single_value():
    df_single = pd.DataFrame({"values": [5]})
    assert calculate_median(df_single, "values") == 5


def test_calculate_std_dev_single_value():
    df_single = pd.DataFrame({"values": [5]})
    assert calculate_std_dev(df_single, "values") == 0
