import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("Play Store Data.csv")

st.title("Google Play Store Dashboard")

st.header("Top KPIs")
st.write("Total Installs:", df['Installs'].sum())
st.write("Average Rating:", round(df['Rating'].mean(), 2))

st.header("Installs by Category")
fig = px.bar(df, x='Category', y='Installs', title='Total Installs by Category')
st.plotly_chart(fig)

st.header("Average Rating by Category")
fig2 = px.bar(df, x='Category', y='Rating', title='Average Rating by Category')
st.plotly_chart(fig2)
