import pandas as pd
from pathlib import Path

from ai_config import (
    DEFAULT_REVENUE_TARGET,
    DEFAULT_PROFIT_TARGET,
    DEFAULT_ORDER_TARGET,
    DEFAULT_CUSTOMER_TARGET,
)

# ==========================================================
# TARGET FILE
# ==========================================================

TARGET_FILE = Path("data/targets.xlsx")

# ==========================================================
# DEFAULT TARGETS
# ==========================================================

DEFAULT_TARGETS = {
    "Revenue": DEFAULT_REVENUE_TARGET,
    "Profit": DEFAULT_PROFIT_TARGET,
    "Orders": DEFAULT_ORDER_TARGET,
    "Customers": DEFAULT_CUSTOMER_TARGET,
}

# ==========================================================
# TARGET CACHE
# ==========================================================

_TARGET_CACHE = None


# ==========================================================
# LOAD TARGETS
# ==========================================================

def load_targets():
    """
    Loads company targets from Excel.

    Uses an in-memory cache for performance.
    Falls back gracefully if the workbook is missing,
    unreadable or incorrectly formatted.
    """

    global _TARGET_CACHE

    if _TARGET_CACHE is not None:
        return _TARGET_CACHE

    try:

        if not TARGET_FILE.exists():
            _TARGET_CACHE = pd.DataFrame()
            return _TARGET_CACHE

        targets = pd.read_excel(TARGET_FILE)

        required = {"Metric", "Target"}

        if not required.issubset(targets.columns):
            _TARGET_CACHE = pd.DataFrame()
            return _TARGET_CACHE

        targets = targets.copy()

        targets["Metric"] = (
            targets["Metric"]
            .astype(str)
            .str.strip()
        )

        _TARGET_CACHE = targets

    except Exception:

        _TARGET_CACHE = pd.DataFrame()

    return _TARGET_CACHE


# ==========================================================
# GET TARGET
# ==========================================================

def get_target(metric):
    """
    Returns the configured target for a KPI.

    If the target is unavailable,
    the default configuration value is returned.
    """

    metric = str(metric).strip()

    targets = load_targets()

    if targets.empty:
        return DEFAULT_TARGETS.get(metric)

    row = targets.loc[
        targets["Metric"] == metric
    ]

    if row.empty:
        return DEFAULT_TARGETS.get(metric)

    value = row.iloc[0]["Target"]

    if pd.isna(value):
        return DEFAULT_TARGETS.get(metric)

    try:
        return float(value)
    except (TypeError, ValueError):
        return DEFAULT_TARGETS.get(metric)


# ==========================================================
# RELOAD TARGETS
# ==========================================================

def reload_targets():
    """
    Clears the cache and reloads the workbook.
    """

    global _TARGET_CACHE

    _TARGET_CACHE = None

    return load_targets()


# ==========================================================
# GET ALL TARGETS
# ==========================================================

def get_all_targets():
    """
    Returns all configured targets merged with defaults.
    """

    targets = DEFAULT_TARGETS.copy()

    table = load_targets()

    if table.empty:
        return targets

    for _, row in table.iterrows():

        metric = str(row["Metric"]).strip()

        value = row["Target"]

        if pd.notna(value):
            targets[metric] = value

    return targets