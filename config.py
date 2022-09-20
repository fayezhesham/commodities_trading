# importing dependencies 
import pandas as pd
import plotly.graph_objects as go
import json
# reading the data 
detailed_data = pd.read_csv('data/data_cleaned.csv')
overview_data = pd.read_csv('data/overview.csv')
# getting the categories in the data, this step is done to avoid importing the whole data set in the layout file.
categories = list(detailed_data['category'].unique())

# Plotly mapbox token 
token = "pk.eyJ1IjoiZmF5ZXotaCIsImEiOiJja3kxc3N1azkwZXJnMnBsZzhkY3owY3NvIn0.bZf3aU9wAEx1mx4Vzbd0Xg"

# the geojson file used in the maps 
countries = json.load(open('countries.json', 'r'))

# define a blank figure function to be used in the dcc.Graph component when there isn't a specified figure.
# to avoid showing the empty graph by default
def blank_fig():
    fig = go.Figure(go.Scatter(x=[], y = []))
    fig.update_layout(template = None,
                     plot_bgcolor="rgba( 0, 0, 0, 0)",
                     paper_bgcolor="rgba( 0, 0, 0, 0)",)
    fig.update_xaxes(showgrid = False, showticklabels = False, zeroline=False)
    fig.update_yaxes(showgrid = False, showticklabels = False, zeroline=False)

    return fig


# the configuration of the graphs 
# avoids displaying plotly's logo which is displayed by default and adds some function buttons
config = {'displaylogo': False,
         'modeBarButtonsToAdd':['drawline',
                                'drawopenpath',
                                'drawclosedpath',
                                'drawcircle',
                                'drawrect',
                                'eraseshape'
                               ]}

