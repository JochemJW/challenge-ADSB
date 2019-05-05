# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df_accidents_2012_to_2014 = pd.read_csv('Datasets/1.6 million UK traffic accidents/accidents_2012_to_2014.csv',low_memory=False)
df_accidents_2009_to_2011 = pd.read_csv('Datasets/1.6 million UK traffic accidents/accidents_2009_to_2011.csv',low_memory=False)
df_accidents_2005_to_2007 = pd.read_csv('Datasets/1.6 million UK traffic accidents/accidents_2005_to_2007.csv',low_memory=False)
df = pd.concat([df_accidents_2012_to_2014, df_accidents_2009_to_2011, df_accidents_2005_to_2007])
df2 = pd.read_csv('Datasets/UK Road Safety Traffic Accidents and Vehicles/Vehicle_Information.csv', encoding='cp1252')

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
	], className="row"),
	html.Div([
		html.Div(children=[html.H3('Road type',style={'text-align': 'center','margin-top': '100%'})
		], className="two columns"),
		html.Div(children=[	
		    dcc.Graph(id = 'test', style="background-color: #e3e3e3",figure={
		            'data': [
		                {'x': grouped_by_Road_Type['Road_Type'].count().keys().tolist(), 
		                 'y': grouped_by_Road_Type['Road_Type'].count().tolist(), 'type': 'bar'}
		            ],
		            'layout': {
		                'title': 'Number of accidents by road type',
		                'xaxis':{
		                	'title':'Road type'
		                	},
                		'yaxis':{
                			'title':'Accidents'
                			}
		            }
		        } ),
		], className="five columns"),
		html.Div([
		        dcc.Graph(id = 'a', figure={
		            'data': [
		                {'x': groupedby_speed_limit['Speed_limit'].count().keys().tolist(), 
		                 'y': groupedby_speed_limit['Number_of_Casualties'].mean().tolist(), 
		                 'mode':'markers',
		                 'marker':{
		                    'size':size,
		                    'sizemode':'area',
		                }}
		            ],
		            'layout': {
		                'title': 'Number of accidents and mean number of casualities by speed limit on road',
		                'xaxis':{
		                	'title':'speed limit on road in km/h'
		                	},
                		'yaxis':{
                			'title':'mean number of casualties'
                			}
		            }
		        } )
			], className="five columns")
	], className="row"),
	html.Div([
		html.Div(children=[html.H3('Time',style={'text-align': 'center','margin-top': '100%'})
		], className="two columns"),
		html.Div(children=[	
		    dcc.Graph(id = 'x', figure={
		            'data': [
		                {'x': grouped_by_time['Time'].count().keys().tolist(),
		                 'y': grouped_by_time["Time"].count().tolist(),
		                 'type': 'bar'}
		            ],
		            'layout': {
		                'title': 'Total accidents by hour',
		                'xaxis':{
		                	'title':'Time'
		                	},
                		'yaxis':{
                			'title':'number of accidents'
                			}
		            }
		        } ),
		], className="five columns"),
		html.Div(children=[	
		    dcc.Graph(id = 'c', figure={
		            'data': [
		                {'x': ['monday','tuesday','wednesday','thursday','friday','saturday','sunday'],
		                 'y': df.groupby(['Day_of_Week'])['Day_of_Week'].count(),
		                 'type': 'bar'}
		            ],
		            'layout': {
		                'title': 'Total accidents by day of week',
		                'xaxis':{
		                	'title':'Time'
		                	},
                		'yaxis':{
                			'title':'number of accidents'
                			}
		            }
		        } ),
		], className="five columns")
	], className="row"),
	html.Div([
		html.Div(children=[html.H3('Age',style={'text-align': 'center','margin-top': '100%'})
		], className="two columns"),
		html.Div(children=[	
		    dcc.Graph(id = 'v', figure={
		            'data': [
		                {'x': df2.groupby('Age_Band_of_Driver')['Age_Band_of_Driver'].count().keys().tolist(),
		                 'y': df2.groupby('Age_Band_of_Driver')['Age_Band_of_Driver'].count(),
		                 'type': 'bar'}
		            ],
		            'layout': {
		                'title': 'number of accident by Age',
						'xaxis':{
		                	'title':'Age'
		                	},
                		'yaxis':{
                			'title':'number of accidents'
                			}
		            }
		        } ),
		], className="ten columns")
	], className="row")
])

if __name__ == '__main__':
    app.run_server(debug=True)