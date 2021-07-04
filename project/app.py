# Run this app with `python app.py` and

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from db_conn.connector import connect 
#QUERIES:
query0 = "SELECT country_code,country_name, max(gdp) AS gdp\
            FROM data, country\
            WHERE year = 2000 AND gdp IS NOT NULL AND country_code == country_code \
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
            WHERE country_code = 'USA' OR country_code = 'JPN' OR country_code = 'DEU' OR country_code = 'GBR' OR country_code = 'FRA' OR country_code = 'CHN' OR country_code = 'ITA' OR country_code = 'CAN' OR country_code = 'MEX' OR country_code = 'BRA'\
            AND year > 1999 AND year < 2016\
            GROUP BY country_code, co2_emission, electricity_prodction\
            ORDER BY gdp DESC\
            LIMIT 10;"

#establish connection and fetch queries
def data_fetch():
    raw_data = connect(query0)
    #transform data
    df0 = {"Country Code": [], "Year" : [], "GDP(USD)": []}
    
    if raw_data[1]:
        for tup in raw_data[0]:
            df0["Country Code"].append(tup[0])
            df0["Year"].append(tup[1])
            df0["GDP(USD)"].append(tup[3])

    else:
        print("FUCK")

    return pd.DataFrame(df0)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#call data from db
df = data_fetch()

fig = px.scatter(df, x="Year", y="GDP(USD)", color="Country Code", hover_name="Country Names")

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
