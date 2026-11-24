import csv

import pandas as pd


def read_csv_file(file_path: str) -> pd.DataFrame:
    """Read a CSV file and return a DataFrame."""
    """ Read """
    return pd.read_csv(file_path)


def read_csv(path: str) -> list[dict[str, str]]:
    """Read a CSV file and return a list of dictionaries."""
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    return data


import json


def load_column_mapping(path):
    """Load column mapping from a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        mapping = json.load(file)

    return mapping
