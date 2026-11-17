import pandas as pd

from validator import check_duplicates
from transformer import standardize_columns, calculate_order_totals


# Test 1: Check duplicate rows
def test_check_duplicates():
    df = pd.DataFrame({
        "id": [1, 2, 2]
    })

    assert check_duplicates(df) == 1


# Test 2: Check column name standardization
def test_standardize_columns():
    df = pd.DataFrame({
        " ORDER_ID ": [1, 2],
        " CUSTOMER_ID ": [3, 4]
    })

    result = standardize_columns(df)

    assert list(result.columns) == ["order_id", "customer_id"]


# Test 3: Check order total calculation
def test_calculate_order_totals():
    df = pd.DataFrame({
        "order_id": ["A101", "A101", "B102"],
        "price": [100.0, 200.0, 300.0]
    })

    result = calculate_order_totals(df)

    assert result == {
        "A101": 300.0,
        "B102": 300.0
    }