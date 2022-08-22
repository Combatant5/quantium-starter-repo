import pandas
import csv
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import time


import pandas as pd


df = pd.read_csv('daily_sales_data_1_2_3_combined.csv')
fig = px.line(df,x="Date", y="Sales",color="Region",title="All Regio1ns Pink Morsel Sales")

app = Dash(__name__)

app.layout = html.Div(id="d5a",children=[html.Label(id="lab_ghheader"),html.Header("Soul Foods's Graph",id='head5', title="Foods's Graph",),html.Br(),html.Label(id="lab_graph5"),


    
            dcc.Graph(id ="graph5", figure=fig),

    html.Label(id="lab_radio"),
    html.Br(),
    dcc.RadioItems(id ="op5",
                   options=[
                       {'label': 'north', 'value': 'north'},
                       {'label': 'east', 'value': 'east'},
                       {'label': 'south', 'value': 'south'},
                       {'label': 'west', 'value': 'west'},
                       {'label': 'all', 'value': 'all'}
                       ],
                   value='all'
                  )
                                         
                    
                       ])


@app.callback(
 
    Output('graph5', 'figure'),
    Output('lab_ghheader', 'children'),
    Output('lab_graph5', 'children'),
    Output('lab_radio', 'children'),
    Input('op5','value'))
def update_figure5(Region):
            if Region == 'all':
                fig = px.line(df, x="Date", y="Sales", color="Region", title="All Regions Pink Morsel Sales")
                fig.update_layout(transition_duration=500)
                return fig,"Virualisation Title", "Virualisation", "Region picker"
                
            else:
                filtered_df = df[df.Region == Region]
                fig = px.line(filtered_df, x="Date", y="Sales", color="Region",
                      title=Region.upper() + " Region Pink Morsel Sales")
                fig.update_layout(transition_duration=500)
                return fig,"Virualisation Title", "Virsualisation", "Region picker"
                
if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=True)
