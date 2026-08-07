from sqlalchemy import create_engine
from urllib.parse import quote_plus
from config import *

connection_string = (
    f"DRIVER={{{DRIVER}}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"Trusted_Connection={TRUSTED_CONNECTION};"
    f"TrustServerCertificate={TRUST_SERVER_CERTIFICATE};"
)

engine = create_engine(
    "mssql+pyodbc:///?odbc_connect=%s"
    % quote_plus(connection_string)
)

def get_engine():
    return engine