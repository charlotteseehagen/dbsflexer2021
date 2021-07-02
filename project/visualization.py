# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://github.com/charlotteseehagen/dbsflexer2021/blob/3228184e263220b0e2513809b765a34acba3899d/project/data_sets/data_clean.csv')

fig = px.scatter(df, x="gdp", y="co2_emission",
                 size="population_total", color="country_code", hover_name="country_code",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='co2-emission-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
