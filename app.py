import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, fetch_latest_data

st.set_page_config(page_title="Congress Trades", layout="wide")
st.title("Congress Trades Dashboard - Personal Version")

# Sidebar: update button
if st.sidebar.button("Update Data"):
    fetch_latest_data()
    st.success("Data updated!")

# Load data
data = load_data()

# Filters
senator_filter = st.sidebar.multiselect("Select Senator", options=data['senator'].unique(), default=data['senator'].unique())
ticker_filter = st.sidebar.multiselect("Select Ticker", options=data['ticker'].unique(), default=data['ticker'].unique())
filtered_data = data[(data['senator'].isin(senator_filter)) & (data['ticker'].isin(ticker_filter))]

# Display table
st.subheader("Trades Table")
st.dataframe(filtered_data)

# Bar chart
st.subheader("Trades Overview")
trade_counts = filtered_data.groupby('ticker')['amount'].sum().reset_index()
fig = px.bar(trade_counts, x='ticker', y='amount', title="Total Traded Amount by Stock")
st.plotly_chart(fig, use_container_width=True)