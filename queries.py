import pandas as pd
from database import get_engine

engine = get_engine()

def run_query(query):

    return pd.read_sql(query, engine)