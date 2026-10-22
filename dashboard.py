import streamlit as st
import pandas as pd

st.title("📊 Sales Data Analytics Dashboard")

df = pd.read_csv("sales.csv")

st.subheader("Sales Data")

st.dataframe(df)