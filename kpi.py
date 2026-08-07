# ==========================================================
# kpi.py
# Enterprise Sales KPI Engine
# ==========================================================

from queries import run_query


# ==========================================================
# TOTAL REVENUE
# ==========================================================

def get_total_revenue():

    query = """
    SELECT
        SUM(Revenue) AS Revenue
    FROM FactSales
    """

    return float(run_query(query).iloc[0]["Revenue"])


# ==========================================================
# TOTAL PROFIT
# ==========================================================

def get_total_profit():

    query = """
    SELECT
        SUM(Profit) AS Profit
    FROM FactSales
    """

    return float(run_query(query).iloc[0]["Profit"])


# ==========================================================
# TOTAL ORDERS
# ==========================================================

def get_total_orders():

    query = """
    SELECT
        COUNT(*) AS Orders
    FROM FactSales
    """

    return int(run_query(query).iloc[0]["Orders"])


# ==========================================================
# TOTAL CUSTOMERS
# ==========================================================

def get_total_customers():

    query = """
    SELECT
        COUNT(DISTINCT [Customer ID]) AS Customers
    FROM FactSales
    """

    return int(run_query(query).iloc[0]["Customers"])


# ==========================================================
# AVERAGE ORDER VALUE
# ==========================================================

def get_average_order():

    query = """
    SELECT

        SUM(Revenue) / COUNT(*) AS AverageOrder

    FROM FactSales
    """

    return float(run_query(query).iloc[0]["AverageOrder"])


# ==========================================================
# GROSS MARGIN
# ==========================================================

def get_gross_margin():

    query = """
    SELECT

        AVG([Profit Margin %]) AS GrossMargin

    FROM FactSales
    """

    return float(run_query(query).iloc[0]["GrossMargin"])


# ==========================================================
# MONTHLY REVENUE
# ==========================================================

def get_monthly_revenue():

    query = """
    SELECT

        Year,
        [Month],
        MIN([Order Date]) AS SortDate,
        SUM(Revenue) AS Revenue

    FROM FactSales

    GROUP BY

        Year,
        [Month]

    ORDER BY

        MIN([Order Date])
    """

    return run_query(query)


# ==========================================================
# SALES BY REGION
# ==========================================================

def get_sales_by_region():

    query = """
    SELECT

        Region,
        SUM(Revenue) AS Revenue

    FROM FactSales

    GROUP BY Region

    ORDER BY Revenue DESC
    """

    return run_query(query)


# ==========================================================
# SALES BY CATEGORY
# ==========================================================

def get_sales_by_category():

    query = """
    SELECT

        Category,
        SUM(Revenue) AS Revenue

    FROM FactSales

    GROUP BY Category

    ORDER BY Revenue DESC
    """

    return run_query(query)


# ==========================================================
# SALES BY CHANNEL
# ==========================================================

def get_sales_by_channel():

    query = """
    SELECT

        [Sales Channel],
        SUM(Revenue) AS Revenue

    FROM FactSales

    GROUP BY [Sales Channel]

    ORDER BY Revenue DESC
    """

    return run_query(query)


# ==========================================================
# CUSTOMER SEGMENTS
# ==========================================================

def get_customer_segments():

    query = """
    SELECT

        [Customer Segment],
        COUNT(*) AS Customers

    FROM FactSales

    GROUP BY [Customer Segment]

    ORDER BY Customers DESC
    """

    return run_query(query)