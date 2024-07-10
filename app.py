import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

fig = px.histogram(car_data, x="price", color="model", 
                   title="Distribuição dos Tipos de Veículos por Faixa de Preço",
                   labels={"type": "Tipo de Veículo", "price_range": "Faixa de Preço"}) # criar um histograma
fig.show() # exibindo

st.header("Analise de veiculos usados")
st.sidebar.header('Escolha o que deseja filtrar')

st.dataframe(car_data)

build_histogram = st.sidebar.checkbox('Criar um histograma')
build_scatter = st.sidebar.checkbox('Criar um grafico de dispersao')

if build_histogram: # se a caixa de seleção for selecionada
  st.write('Criando um histograma dos veiculo por preco' )
  fig_histogram = px.histogram(car_data, x="price", color="model", 
                                 title="Distribuição dos Veículos por Faixa de Preço",
                                 labels={"price": "Preço", "model": "Modelo"})
  st.plotly_chart(fig_histogram,use_container_width=True)

if build_scatter:
  st.write('Criado um garioc de disppersao')
  fig_scatter = px.scatter(car_data, y="type", x='price', title='Preço por Tipo de Veículo',labels={'type': 'Tipo de Veículo', 'price': 'Preço'}) # criar um gráfico de dispersão
  st.plotly_chart(fig_scatter, use_container_width=True)