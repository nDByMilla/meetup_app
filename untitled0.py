import pymongo
import pandas as pd
from pymongo import MongoClient
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

uri = 'mongodb+srv://camil:Black12Passat@cluster0-vwgo4.mongodb.net/meetup_rsvp_db?retryWrites=true&w=majority' 

client = MongoClient(uri)
db = client.meetup_rsvp_db
collection = db.meetup_rsvp_message_detail_tbl
df = pd.DataFrame(list(collection.find()))


df['group_lat']=df.group_lat.astype(float)
df['group_lon']=df.group_lon.astype(float)
df['guests']=df.guests.astype(int)

#print(df.group_lat)

mapbox_access_token = "pk.eyJ1IjoiY2FtaWxsYXNjZiIsImEiOiJja2MwcHRpYmsxbHZwMnJsZ2liZzB2eTFvIn0.guAe-bjjqGzOYGC4O-c0Iw"

px.set_mapbox_access_token(mapbox_access_token)

fig = px.scatter_mapbox(df, lat="group_lat",lon="group_lon",size='guests',
                hover_name='event_name' ,zoom=4)
fig.update_layout(mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=51,
            lon=1
        )),mapbox_style="basic",title='meetup events',width=1400,height=800)

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])
fig.show()

app.run_server(debug=True)
