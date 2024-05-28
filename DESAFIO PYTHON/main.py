import pandas as pd
import streamlit as st
import plotly.express as px 
import plotly.graph_objects as go
from math import inf 


##BASE

data = pd.read_csv(r'C:\Users\Administrador\Desktop\DADOS F1\driver_standings.csv', sep=',')
data_driver_details = pd.read_csv(r'C:\Users\Administrador\Desktop\DADOS F1\driver_details.csv', sep=',')
data_constructor_standings = pd.read_csv(r'C:\Users\Administrador\Desktop\DADOS F1\constructor_standings.csv', sep=',')
data_races = pd.read_csv(r'C:\Users\Administrador\Desktop\DADOS F1\race_summaries.csv', sep=',') 

st.set_page_config(page_title="TEMPORADAS F1", page_icon=":checkered_flag:")




##FILTRAGEM
lista_temporadas = data['Year'].unique()
#salva uma lista com o ano de cada temporada


#TEXTO SIDEBAR I
with st.container():
    st.sidebar.header(''':red[FORMULA 1] Dashboard''')
    st.sidebar.subheader('''1950 - 2022''')
st.sidebar.divider()


#BOTÃO TEMPORADA
temporada_escolhida = st.sidebar.selectbox("Temporada", lista_temporadas)
#seleciona a temporada a ser analisada


##FILTRAR PILOTOS
def filtrar_lista_pilotos():
    filtrar_pltLs = data_driver_details.query(f'Year == {temporada_escolhida}')
    return filtrar_pltLs
lista_dos_pilotos = filtrar_lista_pilotos()
#filtra a lista de pilotos na temporada

lista_pilotos = lista_dos_pilotos['Driver'].unique()
#salva a filtragem anterior

piloto_escolhido = st.sidebar.selectbox("Piloto", lista_pilotos, index = None, placeholder="Selecione um piloto")
#seleciona o piloto da lista a ser analisado


#BOTÃO
filtragem_PC = st.sidebar.radio('Selecione a filtragem',("Pilotos", "Construtoras"))
#seleciona se deseja ver a pontuação por piloto ou construtores

#TEXTO SIDERBAR II
st.sidebar.divider()
with st.container():
    st.sidebar.write("**Sobre**")
    st.sidebar.markdown("Diego Penna Andrade Barros")
    st.sidebar.markdown("PDITA 274")


#MAIN
st.header(f'Temporada de {temporada_escolhida}')
st.caption('Análise detalhada da temporada escolhida')

##FUNÇÃO
def filtrar_ano():
    filtragem = data.query(f'Year == {temporada_escolhida}')
    return filtragem
tabela_ano = filtrar_ano()
#retorna a filtragem com as informações referentes ao ano escolhido

def filtrar_construtoras_ano():
    filtragem_constr = data_constructor_standings.query(f'Year == {temporada_escolhida}')
    return filtragem_constr
construtora_ano = filtrar_construtoras_ano()
#retorna detalhes das construras no ano escolhido
#DETALHE: as construtoras só começaram no ano de 1958, por isso antes desse ano  o gráfico está vazio

def filtrar_piloto_ano():
    filtragem_plt = data_driver_details.query(f'Year == {temporada_escolhida}')
    filtragem_plt = filtragem_plt.query(f'Driver == "{piloto_escolhido}"')
    return filtragem_plt
piloto_ano = filtrar_piloto_ano()
#retorna a filtagrem com o piloto escolhido na temporada 

def races_lap():
    filtragem_voltas = data_races.query(f'Year == {temporada_escolhida}')
    filtragem_voltas = filtragem_voltas['Time']
    return filtragem_voltas
tempo_voltas = races_lap()
#retorna a filtragem com o tempo da volta mais rapida em cada corrida da temporada


##GRÁFICO
with st.container():
    col1,col2 = st.columns(2)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = len(data_races.query(f'Year == {temporada_escolhida}')),
        domain = {'x': [0, 1], 'y': [0, 1]},
        delta = {'reference': len(data_races.query(f'Year == 1950'))},
        title = {'text': "Número de corridas"},
        gauge = {'axis': {'range': [None, 25]},
            'steps' : [
                {'range': [0, len(data_races)/72], 'color': "gray"}, #média do numero de corridas por temporada
                {'range': [0, len(data_races.query(f'Year == 1950'))], 'color': "lightgray"}], #numero de corridas na primeira temporada
            'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': len(data_races.query(f'Year == 2022'))
            #numero de corridas na ultima temporada
        }}))
    col1.plotly_chart(fig)

with st.container():
    col1,col2 = st.columns(2)
    col1.metric("Volta mais rápida", sorted(tempo_voltas)[0])
    col1,col2 = st.columns(2)
    col1.metric("Volta mais lenta", sorted(tempo_voltas)[-1])

with st.container():
    if filtragem_PC == 'Construtoras':
        col1, col2 = st.columns(2)
        fig_date = px.pie(construtora_ano, values = 'PTS', names = 'Team', title='Pontuação no campeonato', width= 450, height= 550)
        col2.plotly_chart(fig_date)
    if filtragem_PC == 'Pilotos':
        col1, col2 = st.columns(2)
        fig_date = px.bar(tabela_ano, y =  'Driver', x = 'PTS', hover_data=["Car","PTS"], title='Pontuação no campeonato', orientation="h", width= 450, height= 550)
        col2.plotly_chart(fig_date)  
#DETALHE: as construtoras só começaram no ano de 1958, por isso antes desse ano  o gráfico está vazio 
#cria um gráfico com a pontuação dos pilotos e construtores na temporada

with st.container():
    col1, col2 = st.columns(2)
    fig = px.line(piloto_ano, x="Grand Prix", y="PTS", hover_data=["Race Position"], title=(f'Desempenho {piloto_escolhido}'), width= 550, height= 500, markers=True)
    col1.plotly_chart(fig)
#cria um gráfico com a pontuação dos pilotos por corrida
