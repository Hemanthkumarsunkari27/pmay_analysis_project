import pandas as pd

# Analysis of PMAY data
def analyze_pmay_data(pmay_data):
    # Group by state and calculate average beneficiaries percentage
    state_pmay_summary = pmay_data.groupby('state')['beneficiaries_percentage'].mean().reset_index()
    return state_pmay_summary

# Analysis of sanitation data
def analyze_sanitation_data(sanitation_data):
    # Calculate sanitation coverage over time for each state
    sanitation_summary = sanitation_data.groupby(['state', 'year'])['sanitation_coverage'].mean().unstack()
    return sanitation_summary
