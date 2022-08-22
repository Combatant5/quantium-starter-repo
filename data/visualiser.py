import pandas
import csv
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import time


import pandas as pd


df = pd.read_csv('daily_sales_data_1_2_3_combined.csv')
fig = px.line(df,x="Date", y="Sales",color="Region",title="All Region Pink Morsel Sales")

app = Dash(__name__)

app.layout = html.Div(id="d5a",children=[html.Label(id="lab_ghheader"),html.Header("Soul Foods's Graph",id='head5', title="Soul Foods's Graph",),html.Br(),html.Label(id="lab_graph5"),


    
            dcc.Graph(id ="graph5", figure=fig),
            
            
            ])
                
if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=True)
