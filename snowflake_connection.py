import snowflake.connector
import pandas as pd

# Establish connection to Snowflake
def connect_to_snowflake():
    conn = snowflake.connector.connect(
        user='<USER NAME>',
        password='<PASSWORD>',
        account='<ACCOUNT>',
        warehouse='<WAREHOUSE>',
        database='<DATABASE>',
        schema='<SCHEMA>'
    )
    return conn

# Query data from Snowflake
def fetch_data(query):
    conn = connect_to_snowflake()
    try:
        df = pd.read_sql(query, conn)
    finally:
        conn.close()
    return df
