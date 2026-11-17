import pandas as pd


def check_nulls(df: pd.DataFrame) -> pd.Series:
    """Count missing values in each column."""
    return df.isnull().sum()


def check_duplicates(df: pd.DataFrame) -> int:
    """Count duplicate rows in the DataFrame."""
    return int(df.duplicated().sum())