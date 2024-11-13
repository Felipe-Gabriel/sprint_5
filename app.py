import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Projeto Sprint 5:")
st.header("Ferramentas de Desenvolvimento de Software")

car_data = pd.read_csv('notebooks/vehicles.csv') # lendo os dados

st.subheader('Gráfico Histogrma')
hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Gráfico Dispersão')
disper_button = st.button('Criar dispersão')

if disper_button:
    st.write('Criando dispersão para o conjunto de dados de anúncios de vendas de carros')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)

modelos = car_data['model'].dropna().unique()
modelo_selecionado = st.selectbox('Selecione o modelo do veículo:', modelos)

dados_filtrados = car_data[car_data['model'] == modelo_selecionado]

dados_filtrados = dados_filtrados.dropna(subset=['model_year','price'])

plt.figure(figsize=(20,6))
sns.boxplot(x='model_year',y='price', data=dados_filtrados)
plt.xlabel('Ano do Modelo')
plt.ylabel('Preço')
plt.title(f'Boxplt de Preço por Ano para o Modelo: {modelo_selecionado}')
st.pyplot(plt)