import pandas as pd


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows from the DataFrame."""
    return df.drop_duplicates()


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to lowercase and remove extra spaces."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    return df


def apply_column_mapping(
    df: pd.DataFrame, column_mapping: dict[str, str]
) -> pd.DataFrame:
    """Rename columns using a mapping dictionary."""
    return df.rename(columns=column_mapping)


def calculate_order_totals(df: pd.DataFrame) -> dict[str, float]:
    """Calculate total product price for each order ID."""
    order_totals = {}

    for _, row in df.iterrows():
        order_id = row["order_id"]
        price = float(row["price"])

        if order_id in order_totals:
            order_totals[order_id] += price
        else:
            order_totals[order_id] = price

    return order_totals
