import plotly.express as px 
import pandas as pd 
import streamlit as st 

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#BASE

data = pd.read_csv(r'C:\Users\Administrador\Desktop\DADOS F1\driver_standings.csv', sep=',')
data_driver_standings = pd.read_csv(r'C:\Users\Administrador\Desktop\DADOS F1\driver_details.csv', sep=',')
data_constructor_standings = pd.read_csv(r'C:\Users\Administrador\Desktop\DADOS F1\constructor_standings.csv', sep=',')

app = dash.Dash(__name__)

st.set_page_config(page_title="TEMPORADAS F1")

##BOTÕES
temporada_escolhida = st.sidebar.selectbox("Temporada", (data['Year'].unique()), value = 2022)
#escolhe a temporada a ser analisada

#SIDERBAR

app.layout = html.Div ([
    html.H1("Temporada"),

    dcc.Dropdown( id="select_year",
        options = [{"label": data['Year'].unique(), "value": {temporada_escolhida}}], 
        multi = False, 
        value = 2022,
    ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={}) 
])
 


if __name__ == '__main__':
    app.run_server(debug = True)


