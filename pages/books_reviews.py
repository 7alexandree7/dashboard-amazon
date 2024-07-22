import streamlit as st
import pandas as pd
import plotly.express as px

# Definir por padrao visualização da tabela wide ligada
st.set_page_config(layout='wide')


df_reviews = pd.read_csv('datasets/customer reviews.csv')
df_top100_books = pd.read_csv('datasets/Top-100 Trending Books.csv')


books = df_top100_books['book title'].unique()
book = st.sidebar.selectbox('Books', books)

df_book = df_top100_books[df_top100_books ['book title'] == book]
df_reviews_filtrado = df_reviews[df_reviews['book name'] == book]



book_title = df_book['book title'].iloc[0]
book_genre = df_book['genre'].iloc[0]
book_price = f'${df_book['book price'].iloc[0]}'
book_rating = df_book['rating'].iloc[0]
book_year = df_book['year of publication'].iloc[0]


st.title(book_title)
st.subheader(book_genre)


col1, col2, col3 = st.columns(3)

col1.metric('Price', book_price)
col2.metric('Rating', book_rating)
col3.metric('Year', book_year)

st.divider()


for row in df_reviews_filtrado.values:
    message = st.write(f'***{row[2]}***')
    message = st.write(row[5])