# PMAY and Sanitation Analysis Project

## Project Overview

This project aims to analyze the impact of the Pradhan Mantri Awas Yojana (PMAY) scheme and the state of sanitation in India. Using data from Snowflake and interactive visualizations with Streamlit, the application enables users to explore PMAY beneficiaries and sanitation progress across different states. The project identifies key insights and gaps in housing and sanitation infrastructure, helping inform policy decisions.

## Features

1.Data Ingestion: Loads PMAY and sanitation data from Snowflake.
2.Data Transformation**: Processes and transforms the data for analysis.
3.Data Analysis: Computes insights such as beneficiary percentages and sanitation coverage trends.
4.Interactive Visualizations: Users can explore data by state, district, and year with an interactive Streamlit app.
4.Downloadable Data: Processed data is available for download for further analysis.

## Technology Stack

- **Snowflake**: Centralized data storage and processing.
- **Python**: Data manipulation, analysis, and visualization.
- **Streamlit**: Builds the interactive user interface for data exploration.
- **Pandas**: Data processing and manipulation.
- **Seaborn & Matplotlib**: Data visualization libraries.

## Project Structure

├── app.py # Main Streamlit app file ├── snowflake_connection.py # Snowflake connection setup ├── data_processing.py # Data retrieval functions ├── analysis.py # Data analysis functions ├── requirements.txt # Dependencies └── README.md # Project documentation


## Setup Instructions

### Prerequisites

- Python 3.7 or later
- Snowflake account (for database access)
- Streamlit installed for running the app

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository

2.Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install the required dependencies:
pip install -r requirements.txt

4.Configure your Snowflake connection in snowflake_connection.py by updating the following placeholders with your credentials:
user='<USERNAME>'
password='<PASSWORD>'
account='<ACCOUNT>'
warehouse='<WAREHOUSE>'
database='<DATABASE>'
schema='<SCHEMA>'


#### Running the application

1.Start the Streamlit app:
streamlit run app.py

2.Open the link provided (e.g., http://localhost:8501) in your web browser.


##### Usage
PMAY Beneficiaries Analysis: Explore the percentage of PMAY beneficiaries across states.
Sanitation Coverage Analysis: View sanitation progress for each state over time.
Data Download: Use the download buttons to export data for further analysis.


###### Error Handling and Logging
Errors during data ingestion, transformation, or visualization are logged in error_log.log. Check this file if issues arise.
The application validates data completeness and logs any discrepancies for troubleshooting.


###### Deployment(Optional)
To deploy this app on Streamlit Cloud:
1.Push your project to a GitHub repository.
2.Go to Streamlit Cloud and connect to your GitHub account.
3.Select your project repository and configure environment variables for Snowflake credentials if required.
4.Deploy the app for online access.


###### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
