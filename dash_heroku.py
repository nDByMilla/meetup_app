import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
#import cdata.mongodb as mod
import plotly.graph_objs as go
import pyodbc
 #Server=
from sshtunnel import SSHTunnelForwarder
import pymongo
import pprint

#'MONGO_HOST = "REMOTE_IP_ADDRESS"
MONGO_DB = "meetup_rsvp_db"
MONGO_USER = "camil"
MONGO_PASS = "Black12Passat"

server = SSHTunnelForwarder(
    ssh_username=MONGO_USER,
    ssh_password=MONGO_PASS,
    remote_bind_address=(127.0.0.1, 27017)
)

server.start()

client = pymongo.MongoClient("127.0.0.1", server.local_bind_port) # server.local_bind_port is assigned local port
db = client[MONGO_DB]
#'pprint.pprint(db.collection_names())

server.stop()
#cnxn = mod.connect("Port=27017;Database=meetup_rsvp_db;User=camil;Password=Black12Passat;")
#cnxn = pyodbc.connect("DSN=CData MongoDB Sys;Port=27017,Database=meetup_rsvp_db,User=camil;Password=Black12Passat")
'''

cnxn = pyodbc.connect('DRIVER={CData ODBC Driver for MongoDB};Server=127.0.0.1;Port=27017;Database=meetup_rsvp_db;User=camil;Password=Black12Passat;')
heroku logs --tailheroku logs --taildf = pd.read_sql("SELECT group_name, guests FROM meetup_rsvp_message_detail_tbl LIMIT 10", cnxn)
app_name = 'dash-mongodbdataplot'

print(df.guests)



cnxn = pyodbc.connect('DRIVER={CData ODBC Driver for OData};User=camil;Password=Black12Passat;URL=http://myserver/myOrgRoot;')

df = pd.read_sql("SELECT group_name, guests FROM meetup_rsvp_message_detail_tbl LIMIT 10", cnxn)
app_name = 'dash-mongodbdataplot'

print(df)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'CData + Dash'


trace = go.Bar(x=df.borough, y=df.cuisine, name='borough')
 
app.layout = html.Div(children=[html.H1("CData Extension + Dash", style={'textAlign': 'center'}),
dcc.Graph(
id='example-graph',
figure={
'data': [trace],
'layout':
go.Layout(title='MongoDB restaurants Data', barmode='stack')
})
], className="container")
    
    '''