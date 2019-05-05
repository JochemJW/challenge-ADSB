# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df_accidents_2012_to_2014 = pd.read_csv('https://www.dropbox.com/s/zxv70rmfrfq5h3k/accidents_2012_to_2014.csv?dl=1',low_memory=False)
df_accidents_2009_to_2011 = pd.read_csv('https://www.dropbox.com/s/o9vz1aufkdnoowc/accidents_2009_to_2011.csv?dl=1',low_memory=False)
df_accidents_2005_to_2007 = pd.read_csv('https://www.dropbox.com/s/nzwwiubqjn19lkl/accidents_2005_to_2007.csv?dl=1',low_memory=False)
df = pd.concat([df_accidents_2012_to_2014, df_accidents_2009_to_2011, df_accidents_2005_to_2007])
df2 = pd.read_csv('https://www.dropbox.com/s/n9gm0wu5mmlqcs7/Vehicle_Information.csv?dl=1', encoding='cp1252')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

grouped_by_Road_Type = df.groupby('Road_Type')
groupedby_speed_limit = df.groupby('Speed_limit')
size = [x / 100 for x in groupedby_speed_limit['Speed_limit'].count().tolist()]
df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
grouped_by_time = df.groupby(df['Time'].dt.hour)

app.layout = html.Div(
[
	html.Div([
		html.Div(children=[html.H3('aaaaa',style={'text-align': 'center'})
		], className="twelve columns"),
	], className="row")
])

if __name__ == '__main__':
    app.run_server(debug=True)
