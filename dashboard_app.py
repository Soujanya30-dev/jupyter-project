import streamlit as st
import pandas as pd
import plotly.express as px
from nltk.sentiment.vader import SentimentIntensityAnalyzer

df = pd.read_csv("data/Play Store Data.csv")
reviews_df = pd.read_csv("data/User Reviews.csv")

st.title("Google Play Store Dashboard")

st.header("Key Metrics")
st.write("Total Installs:", df['Installs'].sum())
st.write("Average Rating:", round(df['Rating'].mean(), 2))

st.header("Installs by Category")
fig1 = px.bar(df, x='Category', y='Installs', title="Total Installs by Category")
st.plotly_chart(fig1)

st.header("Ratings Distribution")
fig2 = px.histogram(df, x='Rating', nbins=10, title="Rating Histogram")
st.plotly_chart(fig2)

st.header("Sentiment Analysis")
sia = SentimentIntensityAnalyzer()
reviews_df['Sentiment'] = reviews_df['Translated_Review'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
st.write("Average Sentiment Score:", round(reviews_df['Sentiment'].mean(), 2))
fig3 = px.histogram(reviews_df, x='Sentiment', nbins=20, title="Sentiment Distribution")
st.plotly_chart(fig3)
