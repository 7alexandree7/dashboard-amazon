import streamlit as st
import pandas as pd
import plotly.express as px

df_reviews = pd.read_csv('datasets/customer reviews.csv')
df_top100_books = pd.read_csv('datasets/Top-100 Trending Books.csv')


books = df_top100_books['book title'].unique()
book = st.sidebar.selectbox('Books', books)

df_book = df_top100_books[df_top100_books ['book title'] == book]
df_book