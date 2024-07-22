# Importação de todas as blibiotecas
import streamlit as st
import pandas as pd
import plotly.express as px


# Definir por padrao visualização da tabela wide ligada
st.set_page_config(layout='wide')


# Pedir para o pandas ler meus arquivos.csv
df_reviews = pd.read_csv('datasets/customer reviews.csv')
df_top100_books = pd.read_csv('datasets/Top-100 Trending Books.csv')


# Definindo o preço min e max filtrando pela coluna de book price
# Coluna responsavel pelos valores de cada livro
price_max = df_top100_books['book price'].max()
price_min = df_top100_books['book price'].min()


# Criar o slider
# Definir o slider na side bar
# passar um label para ele, com values (preço_min e preço_max)
max_price = st.sidebar.slider('Price Range', price_min, price_max, price_max)


#Condicional referente a filtragem da coluna book price
# Correlacionando com o silder
df_books = df_top100_books[df_top100_books['book price'] <= max_price]
df_books



# Atribui a variavel fig um grafico do plotly.express
# Filtranndo pela coluna ['year of publication']
# E pegando pelo metodo value_counts() o valor de cada ano

#Na variavel 2, estou utilizando outro tipo de grafico, o histogram
# filtrando pela coluna de book price da minha tabela
fig = px.bar(df_books['year of publication'].value_counts())
fig2 = px.histogram(df_books['book price'])

# Deixando os 2 graficos no msm bloco, cada um ocupando 50% da largura
col1, col2 = st.columns(2)

#Exibindo os graficos
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
