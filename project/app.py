# Run this app with `python app.py` and

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from db_conn import connector as con

#print(con.connect("SELECT * from country")[0])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# see https://plotly.com/python/px-arguments/ for more options

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='DBS-Project 2021'),

    html.Div(children='''
       Helena Waldorf, Charlotte Seehagen, Lenny Kovac 
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':

    query0 = "SELECT country_code, max(gdp) AS gdp\
                FROM data\
                WHERE year = 2000 AND gdp IS NOT NULL\
                GROUP BY country_code, gdp\
                ORDER BY gdp DESC\
                LIMIT 10;"
                
    query1 = "SELECT country_code, co2_emission, max(gdp) AS gdp \
                FROM data \
                WHERE country_code = 'USA' OR country_code = 'JPN' OR country_code = 'DEU' OR country_code = 'GBR' OR country_code = 'FRA' OR country_code = 'CHN' OR country_code = 'ITA' OR country_code = 'CAN' OR country_code = 'MEX' OR country_code = 'BRA'\
                AND year > 1999 AND year < 2016\
                GROUP BY country_code, co2_emission\
                ORDER BY gdp DESC\
                LIMIT 10;"
                
    query2 = "SELECT country_code, electricity_production_renewable, max(gdp) AS gdp\
                FROM data\
                WHERE WHERE country_code = 'USA' OR country_code = 'JPN' OR country_code = 'DEU' OR country_code = 'GBR' OR country_code = 'FRA' OR country_code = 'CHN' OR country_code = 'ITA' OR country_code = 'CAN' OR country_code = 'MEX' OR country_code = 'BRA'\
                AND year > 1999 AND year < 2016\
                GROUP BY country_code,  electricity_prodction\
                ORDER BY gdp DESC\
                LIMIT 10;"
                
    query3 = "SELECT country_code, co2_emission, electricity_production_renewable,                  max(gdp) AS gdp\
                FROM data\
                WHERE WHERE country_code = 'USA' OR country_code = 'JPN' OR country_code = 'DEU' OR country_code = 'GBR' OR country_code = 'FRA' OR country_code = 'CHN' OR country_code = 'ITA' OR country_code = 'CAN' OR country_code = 'MEX' OR country_code = 'BRA'\
                AND year > 1999 AND year < 2016\
                GROUP BY country_code, co2_emission, electricity_prodction\
                ORDER BY gdp DESC\
                LIMIT 10;"
                
    app.run_server(debug=True,port=80,host='0.0.0.0')
