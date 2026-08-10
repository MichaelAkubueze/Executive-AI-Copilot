import pandas as pd
from pathlib import Path


TARGET_FILE = Path("data/targets.xlsx")


def load_targets():

    if TARGET_FILE.exists():

        return pd.read_excel(TARGET_FILE)

    return pd.DataFrame()


def get_target(metric):

    targets = load_targets()

    if targets.empty:
        return None

    row = targets.loc[
        targets["Metric"] == metric
    ]

    if row.empty:
        return None

    return row.iloc[0]["Target"]