import os
import sys
import pymongo
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

uri = 'mongodb://camil:@127.0.0.1:27017/meetup_rsvp_db'

def main(uri):
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    
    # First we'll add a few songs. Nothing is required to create the songs 
    # collection; it is created automatically when we insert.

    songs = db['meetup_rsvp_message_detail_tbl']
    # Note that the insert method can take either an array or a single dict.
    # more weeks at number 1.
    cursor = songs.find({'guests': {'$ne': "0"}}).sort('group_name', 1)
    for doc in cursor:
        print(doc['group_name'])
        #, doc['gues
    client.close()
    docs = [i['group_name'] for i in cursor]
    return docs
docs = main(uri=uri)

app.layout = html.Div([
    html.H2('Meetup summary dashboard'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in docs],
        value='London Muslims Get Together'),
    html.Div(id='display-value')])


@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])

def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
