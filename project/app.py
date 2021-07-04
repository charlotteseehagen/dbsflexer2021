# Run this app with `python app.py` and

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from db_conn.connector import connect 

""" DIE MEGA COOLEN QUERIES
    RATHER UGLY DESIGN BUT NO TIME
    TIME IS PRECIOUS 
"""
query0 ="SELECT data.country_code, country_name, year, max(gdp) AS gdp \
	FROM data, country \
	WHERE year = 2000 AND gdp IS NOT NULL \
	AND data.country_code = country.country_code\
		GROUP BY data.country_code, country_name, year, gdp\
		ORDER BY gdp DESC\
		LIMIT 10;"

query1 ="SELECT foo.country_code, data.year, data.co2_emission, data.gdp, foo.country_name\
	FROM (\
	SELECT data.country_code,country_name, year, max(gdp) AS gdp\
		FROM data, country\
		WHERE year = 2000 AND gdp IS NOT NULL \
		AND data.country_code = country.country_code\
			GROUP BY data.country_code, country_name,year, gdp\
			ORDER BY gdp DESC\
			LIMIT 10\
	) as foo, data, country \
	WHERE foo.country_code = data.country_code AND data.year >= 2000\
		GROUP BY foo.country_code, data.year, data.co2_emission, data.gdp, foo.country_name\
		ORDER BY foo.country_code DESC,\
			 data.year DESC;"

query2 ="SELECT foo.country_code, data.year, data.electricity_production_renewable, data.gdp, foo.country_name\
	FROM (\
	SELECT data.country_code,country_name, year, max(gdp) AS gdp\
		FROM data, country\
		WHERE year = 2000 AND gdp IS NOT NULL \
		AND data.country_code = country.country_code\
			GROUP BY data.country_code, country_name,year, gdp\
			ORDER BY gdp DESC\
			LIMIT 10\
	) as foo, data, country \
	WHERE foo.country_code = data.country_code AND data.year >= 2000\
		GROUP BY foo.country_code, data.year, data.co2_emission, data.gdp, foo.country_name,data.electricity_production_renewable\
		ORDER BY foo.country_code DESC,\
			 data.year DESC;"\



""" VISU STUFF """
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#establish connection and fetch queries
raw_data = connect(query0)
#first figure bar --------------------------------------------------
df0 = {"Country Code": [], "Country Name" : [], "Year" : [], "GDP(USD)" : []}
#transform data
if raw_data[1]:
    for tup in raw_data[0]:
        df0["Country Code"].append(tup[0])
        df0["Country Name"].append(tup[1])
        df0["Year"].append(tup[2])
        df0["GDP(USD)"].append(tup[3])

else:
    print("FUCK")

pd.DataFrame(df0)
fig = px.bar(df0, x="Country Code", y="GDP(USD)", color="Country Code", hover_name="Country Name")

#first line graph --------------------------------------------------
raw_data = connect(query1)
df1 = {"Country Code": [], "Country Name" : [], "Year" : [], "GDP(USD)" : [], "Co2 Emissions(tonnes)" : []}
if raw_data[1]:
    for tup in raw_data[0]:
        df1["Country Code"].append(tup[0])
        df1["Year"].append(tup[1])
        df1["Co2 Emissions(tonnes)"].append(tup[2])
        df1["GDP(USD)"].append(tup[3])
        df1["Country Name"].append(tup[4])

else:
    print("FUCK")

pd.DataFrame(df1)
fig0 = px.line(df1, x="Year", y="Co2 Emissions(tonnes)", color="Country Code", hover_name="Country Name")

#second line graph -------------------------------------------------
raw_data = connect(query2)
df2 = {"Country Code": [], "Country Name" : [], "Year" : [], "GDP(USD)" : [], "Renewable Electricity Sources(Kwh)" : []}
if raw_data[1]:
    for tup in raw_data[0]:
        df2["Country Code"].append(tup[0])
        df2["Year"].append(tup[1])
        df2["Renewable Electricity Sources(Kwh)"].append(tup[2])
        df2["GDP(USD)"].append(tup[3])
        df2["Country Name"].append(tup[4])

else:
    print("FUCK")

pd.DataFrame(df2)
fig2 = px.line(df2, x="Year", y="Renewable Electricity Sources(Kwh)" , color="Country Code", hover_name="Country Name")

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig
        ),
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig0
        ),
    ]),
    html.Div([
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='graph3',
            figure=fig2
        ),
    ]),
])

if __name__ == '__main__':

    app.run_server(debug=True,port=80,host='0.0.0.0')

