import pandas as pd
import streamlit as st
import plotly.express as px 


#BASE

data = pd.read_csv(r'C:\Users\Administrador\Desktop\DADOS F1\driver_standings.csv', sep=',')
data_driver_standings = pd.read_csv(r'C:\Users\Administrador\Desktop\DADOS F1\driver_details.csv', sep=',')
data_constructor_standings = pd.read_csv(r'C:\Users\Administrador\Desktop\DADOS F1\constructor_standings.csv', sep=',')

st.set_page_config(page_title="TEMPORADAS F1")


##BOTÕES
temporada_escolhida = st.sidebar.selectbox("Temporada", (data['Year'].unique()))
#escolhe a temporada a ser analisada

filtragem_PC = st.sidebar.radio('Selecione a filtragem',("Pilotos", "Construtoras"))
#seleciona se deseja ver a pontuação por piloto ou construtores


#FUNÇÕES

@st.cache_data   
def filtrar_ano():
    filtragem = data.query(f'Year == 2022')
    return filtragem
tabela_ano = tabela_ano = filtrar_ano()
#retorna a filtragem com as informações do ano escolhido


##BOTÕES
piloto_escolhido = st.sidebar.selectbox("Piloto", (tabela_ano['Driver'].unique()))


#FUNÇÕES
@st.cache_data   
def filtrar_construtoras_ano():
    filtragem = data_constructor_standings.query(f'Year == 2022')
    return filtragem

construtora_ano = construtora_ano = filtrar_construtoras_ano()
#retorna detalhes das construras no ano escolhido

@st.cache_data   
def filtrar_piloto_ano():
    filtragem = data_driver_standings.query(f'Year == 2022')
    filtragem = filtragem.query(f'Driver == "Lando Norris"')
    return filtragem

piloto_ano = piloto_ano = filtrar_piloto_ano()
#retorna detalhes do piloto no ano escolhido

##GRÁFICOS

with st.container():
    if filtragem_PC == 'Construtoras':
        col1, col2 = st.columns(2)
        fig_date = px.bar(construtora_ano, y =  'Team', x = 'PTS', title='Pontuação no campeonato', orientation="h", width= 500, height= 550)
        col2.plotly_chart(fig_date)
    if filtragem_PC == 'Pilotos':
        col1, col2 = st.columns(2)
        fig_date = px.bar(tabela_ano, y =  'Driver', x = 'PTS', title='Pontuação no campeonato', orientation="h", width= 500, height= 550)
        col2.plotly_chart(fig_date)   
#cria um gráfico com a pontuação dos pilotos e construtores na temporada


with st.container():
    col1, col2 = st.columns(2)
    fig = px.line(piloto_ano, x="Grand Prix", y="PTS", title='Pontos do piloto', width= 550, height= 450)
    col1.plotly_chart(fig)
#cria um gráfico com a pontuação dos pilotos por corrida
