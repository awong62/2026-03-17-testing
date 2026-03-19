import pytest 
import pandas as pd
import matplotlib.pyplot as plt

from analyze_sales import load_data, clean_data, calculate_average_revenue, create_revenue_plot


##============
## Setup data
##============

@pytest.fixture
def raw_test_data():
    """Creates small, predictable DataFrame. Has a None value and a negative value"""
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
        'Revenue': [100.0, -50.0, None, 200.0]
    }
    return pd.DataFrame(data)

@pytest.fixture
def clean_test_data():
    """Creates small, predictable DataFrame. Has nothing wrong it"""
    data = {
        'Month': ['Jan', 'Apr'],
        'Revenue': [100.0, 200.0]
    }
    return pd.DataFrame(data)

@pytest.fixture
def empty_test_data():
    """Create an empty dataframe"""
    return pd.DataFrame(columns=["Month", "Revenue"])


##============
## Tests
##============

def test_clean_data_removes_invalid_rows(raw_test_data):
    """Tests that negatvie and NaN revenues are dropped"""
    cleaned_df = clean_data(raw_test_data)

    assert len(cleaned_df) == 2
    assert cleaned_df['Revenue'].min() > 0
    assert cleaned_df.isna().sum().sum() == 0

def test_calculate_average_revenue_math(clean_test_data):
    """Tests that the mean calculation is correct on valid data."""
    avg = calculate_average_revenue(clean_test_data)
    
    # The average of 100 and 200 is 150
    assert avg == 150.0

def test_create_revenue_plot_returns_figure(clean_test_data):
    """Tests that the plotting function returns a valid matplotlib Figure."""
    fig = create_revenue_plot(clean_test_data)
    
    # Check observability: We can inspect the returned object!
    assert isinstance(fig, plt.Figure)
    assert fig.axes[0].get_title() == "Monthly Revenue"

# 2. Edge Cases (Unexpected or rare use cases)
def test_clean_data_on_already_clean_data(clean_test_data):
    """Tests that cleaning perfectly good data doesn't accidentally alter it."""
    cleaned_df = clean_data(clean_test_data)
    
    assert len(cleaned_df) == 2
    # pandas testing utility for comparing DataFrames
    pd.testing.assert_frame_equal(cleaned_df, clean_test_data)

def test_clean_data_on_empty_dataframe(empty_test_data):
    """Tests how the cleaning function handles an empty dataset."""
    cleaned_df = clean_data(empty_test_data)
    assert len(cleaned_df) == 0

# 3. Abnormal, Error, or Adversarial Use Cases
def test_calculate_average_revenue_raises_error_on_empty(empty_test_data):
    """Tests that the function throws an exception when it should."""
    # We expect a ValueError to be raised here
    with pytest.raises(ValueError, match="Cannot calculate average on an empty DataFrame"):
        calculate_average_revenue(empty_test_data)

def test_load_data_missing_file():
    """Tests that the system throws the expected error if a file is missing."""
    with pytest.raises(FileNotFoundError):
        load_data("this_file_does_not_exist.csv")