# Formula 1 Dashbord <br> 1950 - 2022 

## 🏎️ Apresentação 
O dashbord tem como objetivo apresentar gráficos para o usuário consultar ao realizar uma análise com os aspectos principais de cada temporada de Formula 1 desde a sua estreia em 1950 até o ano de 2022. A realização desse espaço onde a pessoa pode consultar informações essencias sobre a história da Formula 1 se fez necessário porque não existe na internet algum outro site que reuna tanto contéudo de forma consisa e detalhada de forma que facilite para o usuario a obtenção de informação ou a comparação das temporadas e dos pilotos ao longo dos anos. 

## 📋 Pré-requisitos 
Do que você precisa antes de abrir o código:

Python

Baixar o streamlit:
```
pip install streamlit
```
Baixar o banco de dados no repositorio:
```
Desafio-Python/Dados F1
```

## 💾 Banco de Dados
O banco de dados completo se encontra [aqui](https://www.kaggle.com/datasets/debashish311601/formula-1-official-data-19502022). <br>
Para a criação do dashbord, foram utilizados os seguintes arquivos do banco de dados:
* driver_standings.csv - contém a posição de todos os pilotos nos Grand Prix de cada temporada
* driver_details.csv - contém detalhes sobre os pilotos em cada temporada
* constructor_standings.csv - contém a posição de todas as construtoras no campeonato de 1958, primeiro ano do campeonato de construtoras, até 2022
* race_summaries - contém o resultado de cada Grand Prix de 1950 até 2022

## 🏁 Começando
No terminal do python:
```
streamlit run main.py
```

## 🛠️ Estrutura
Elementos do dashbord

**Sidebar**
* *Selectbox temporada* -> permite ao usuário escolher qual temporada ele deseja analisar
* *Selectbox piloto* -> permite ao usuário escolher qual piloto da temporada escolhida será analisado
* *Radio piloto e construtoras* -> as opções atualizam o gráfico "Pontuação no campeonato" para o campeonato dos pilotos ou das construtoras na temporada escolhida

**Gráficos**
* *Número de corridas* -> apresenta a quantidade de corridas na temporada e compara com a quantidade na primeira temporada, com a média de corridas e com a quantidade na temporada de 2022
* *Metric* -> apresenta o tempo da volta mais rápida e mais lenta de cada temporada
* *Podio da temporada* -> apresenta os três primeiros colocados da temporada em análise, o nome e a pontuação que fizeram
* *Pontuação no campeonato* -> pode variar entre os pontos de cada piloto na temporada e a pontuação de cada construtora
* *Desemppenho piloto* -> apresenta a pontuação do piloto escolhido em cada Grand Prix da temporada
* *Legendas* -> trazem informações relevantes sobre os gráficos

## 👨‍💻 Desenvolvedor 
Responsável pela criação do projeto

Diego - Programação e documentação

Conheça mais acessando o GitHub do desenvolvedor [aqui](https://github.com/Di3go07)!
