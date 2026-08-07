import pandas as pd
from queries import run_query

query = """
SELECT

    Year,
    Month,

    SUM(Revenue) Revenue

FROM FactSales

GROUP BY

Year,
Month

ORDER BY

Year,
MIN([Order Date])
"""

df = run_query(query)

print(df)