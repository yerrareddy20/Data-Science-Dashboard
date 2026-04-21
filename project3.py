import streamlit as st
import pandas as pd
from src.analysis import get_basic_info, get_summary, get_missing_values
from src.visualization import plot_histogram, plot_correlation

st.set_page_config(page_title="Data Science Dashboard", layout="wide")

st.title("Data Science Dashboard")

# Upload file
file = st.file_uploader("Upload CSV File", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader(" Data Preview")
    st.write(df.head())

    # Basic Info
    info = get_basic_info(df)
    st.subheader(" Basic Info")
    st.write(info)

    # Summary
    st.subheader("Statistical Summary")
    st.write(get_summary(df))

    # Missing Values
    st.subheader("Missing Values")
    st.write(get_missing_values(df))

    # Select column
    column = st.selectbox("Select Column for Histogram", df.columns)

    if st.button("Show Histogram"):
        fig = plot_histogram(df, column)
        st.pyplot(fig)

    # Correlation
    if st.button("Show Correlation Heatmap"):
        fig = plot_correlation(df)
        st.pyplot(fig)