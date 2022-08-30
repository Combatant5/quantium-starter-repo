import pandas
import csv
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import dash


count1=0
df = pd.read_csv('daily_sales_data_1_2_3_combined.csv')

############################################################3####
CONST_Header_DATA="Soul Foods's Graph"
CONST_Visualization_DATA = px.line(df,x="Date", y="Sales",color="Region",title="All Region Pink Morsel Sales")
CONST_RadioItem_DATA = [
                       {'label': 'north', 'value': 'north'},
                       {'label': 'east', 'value': 'east'},
                       {'label': 'south', 'value': 'south'},
                       {'label': 'west', 'value': 'west'},
                       {'label': 'all', 'value': 'all'}
                       ]

##################################################################

fig = px.line(df,x="Date", y="Sales",color="Region",title="All Region Pink Morsel Sales")

options5=[
                       {'label': 'north', 'value': 'north'},
                       {'label': 'east', 'value': 'east'},
                       {'label': 'south', 'value': 'south'},
                       {'label': 'west', 'value': 'west'},
                       {'label': 'all', 'value': 'all'}
                       ]


list5=[]


head_text5="Soul Foods's Graph"


app = Dash(__name__)

app.layout = html.Div(id="d5a",children=[html.Label(id="lab_ghheader"),html.Header(head_text5,id='head5', title=head_text5),html.Br(),html.Label(id="lab_graph5"),


    
            dcc.Graph(id ="graph5", figure=fig),

    html.Label(id="lab_radio"),
    html.Br(),
    dcc.RadioItems(id ="op5",
                   options = options5,
                   value='all'
                  )
                                         
                    
                       ])


@app.callback(

    Output('lab_ghheader', 'children'),
    Output('lab_graph5', 'children'),
    Output('lab_radio', 'children'),
    Output('graph5', 'figure'),
    Input('op5', 'value'))

def update5(Region):
    global count1
    global list5
    global fig
    global head_text5

    
    
    if(count1!=3):
        list5=[]
        if (str(type(app.layout["head5"]))=="<class 'dash.html.Header.Header'>" and head_text5 == CONST_Header_DATA):
            list5.append("Visualization Title")
            count1 = count1 + 1
        else:
            list5.append("head_text not present or does not match the defined text")
            

        if (str(type(app.layout["graph5"]))=="<class 'dash.dcc.Graph.Graph'>" and fig == CONST_Visualization_DATA):
            list5.append("Visualization")
            count1 = count1 + 1

        else:
            list5.append("visualization not present or does not match the defined data")

        if (str(type(app.layout["op5"]))=="<class 'dash.dcc.RadioItems.RadioItems'>" and options5 == CONST_RadioItem_DATA):
            list5.append("Region Picker")
            count1 = count1 + 1

        else:
            list5.append("radio_Item not present or does not match the defined data")

        if(count1==3):
            if Region == 'all':
                fig = px.line(df, x="Date", y="Sales", color="Region", title="All Regions Pink Morsel Sales")
                fig.update_layout(transition_duration=500)
                
            else:
                filtered_df = df[df.Region == Region]
                fig = px.line(filtered_df, x="Date", y="Sales", color="Region",
                      title=Region.upper() + " Region Pink Morsel Sales")
                fig.update_layout(transition_duration=500)

            return list5[0], list5[1], list5[2], fig

        else:
            count1=0
            
            return list5[0], list5[1], list5[2],dash.no_update
            

            
            

    elif(count1==3):
            if Region == 'all':
                fig = px.line(df, x="Date", y="Sales", color="Region", title="All Regions Pink Morsel Sales")
                fig.update_layout(transition_duration=500)
                
            else:
                filtered_df = df[df.Region == Region]
                fig = px.line(filtered_df, x="Date", y="Sales", color="Region",
                      title=Region.upper() + " Region Pink Morsel Sales")
                fig.update_layout(transition_duration=500)

            return list5[0], list5[1], list5[2], fig
            

        
        
                
    
        
    

    
    


        

    



if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=True)
