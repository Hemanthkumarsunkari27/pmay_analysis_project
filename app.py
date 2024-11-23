import streamlit as st
from data_processing import get_pmay_data, get_sanitation_data
from analysis import analyze_pmay_data, analyze_sanitation_data
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
pmay_data = get_pmay_data()
sanitation_data = get_sanitation_data()

# Analyze data
state_pmay_summary = analyze_pmay_data(pmay_data)
sanitation_summary = analyze_sanitation_data(sanitation_data)

# Streamlit app layout
st.title("Housing and Sanitation Analysis in India")
st.subheader("PMAY Beneficiaries Analysis")

# PMAY Beneficiaries Visualization
st.write("PMAY Beneficiaries by State")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='state', y='beneficiaries_percentage', data=state_pmay_summary, ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)

st.subheader("Sanitation Coverage Analysis")
state_option = st.selectbox("Select State for Sanitation Analysis", sanitation_summary.index)

# Sanitation Coverage Line Chart
st.write(f"Sanitation Coverage over Years in {state_option}")
fig, ax = plt.subplots(figsize=(10, 6))
sanitation_summary.loc[state_option].plot(kind='line', ax=ax)
plt.ylabel('Sanitation Coverage (%)')
plt.xlabel('Year')
st.pyplot(fig)

# Download data option
st.write("Download Processed Data")
if st.button("Download PMAY Data"):
    st.write(state_pmay_summary.to_csv(index=False), file_name="pmay_data.csv")
if st.button("Download Sanitation Data"):
    st.write(sanitation_summary.to_csv(), file_name="sanitation_data.csv")
