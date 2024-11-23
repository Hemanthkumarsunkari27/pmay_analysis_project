from snowflake_connection import fetch_data

# Fetch PMAY data
def get_pmay_data():
    query = """
    SELECT state, district, beneficiaries_percentage, year
    FROM pmay_data
    """
    pmay_data = fetch_data(query)
    return pmay_data

# Fetch sanitation data
def get_sanitation_data():
    query = """
    SELECT state, sanitation_coverage, year
    FROM sanitation_data
    """
    sanitation_data = fetch_data(query)
    return sanitation_data
