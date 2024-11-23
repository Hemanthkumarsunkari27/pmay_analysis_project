import snowflake.connector

# Replace these values with your Snowflake credentials
user = '<YOUR_USERNAME>'
password = '<YOUR_PASSWORD>'
account = '<YOUR_ACCOUNT_IDENTIFIER>'
warehouse = '<YOUR_WAREHOUSE>'
database = '<YOUR_DATABASE>'
schema = '<YOUR_SCHEMA>'

def connect_to_snowflake():
    try:
        # Establish a connection to Snowflake
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        print("Connection successful!")
        return conn
    except Exception as e:
        print("Failed to connect to Snowflake:", e)
        return None

# Test the connection
conn = connect_to_snowflake()
if conn:
    try:
        # Run a simple test query
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_VERSION()")
        version = cursor.fetchone()
        print("Snowflake version:", version[0])
    finally:
        # Close the connection
        conn.close()
