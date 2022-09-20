# importing dependencies 
import dash
from dash import callback, dcc, html, Input, Output, ctx
import plotly.express as px
from config import overview_data, countries, token

# this callback controls both the style of the buttons and the trade flow status which is then used in various parts of the app
@callback(
    Output('buttons1-store', 'data'),
    Output('flow_store', 'data'),
    Input('1exports-b', 'n_clicks'),
    Input('1imports-b', 'n_clicks')
)
def update_buttons1_style(button1, button2):
    button_id = ctx.triggered_id if not None else '1exports-b'
    if button_id == '1exports-b':
        styles = [{'background-color': '#313a46', 'color': 'white'}, None]
        flow = 'Export'
    elif button_id == '1imports-b':
        styles = [None, {'background-color': '#313a46', 'color': 'white'}]
        flow = 'Import'
    else:
        styles = [{'background-color': '#313a46', 'color': 'white'}, None]
        flow = 'Export'

    return styles, flow

# This callback applies the styles stored in the store component from the previous callbacks on the flow buttons.
@callback(
    Output('1exports-b', 'style'),
    Output('1imports-b', 'style'),
    Input('buttons1-store', 'data')
)
def update_buttons1_styles(styles):
    return styles[0], styles[1]


# This callback controls the title of the page according to the flow selected.
@callback(
    Output('page1-title-text', 'children'),
    Input('flow_store', 'data')
)
def update_overview_title(flow):
    return f'Overview of {flow}s'

# The map callback 
@callback(
    Output('map1', 'figure'),
    Input('years-slider', 'value'),
    Input('flow_store', 'data')
)
def update_map(year, flow):
    # filtering the data according to the selected year and trade flow 
    dff = overview_data
    dff = overview_data[(overview_data['year'] == year) & (overview_data['flow'] == flow)]

    fig = px.choropleth_mapbox(dff, 
                            # The geojson is used here. 
                           geojson=countries, 
                           locations="country", 
                           color= "Trade volume (USD)",
                        #    The featureidkey is the name of the feature in the geojson that corresponds to the specified locations in the locations argument 
                           featureidkey= "properties.admin",
                           color_continuous_scale = 'GnBu',
                        #    setting the zoom of the map 
                           zoom = 1,
    )
    # the layout of the map 
    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0}, 
    # The token is used here 
    mapbox_accesstoken = token,  
    dragmode= False,
    plot_bgcolor="rgba( 0, 0, 0, 0)",
    paper_bgcolor="rgba( 0, 0, 0, 0)",
    title = f'Trade volume (USD) of {flow}s per country in {str(year)}'
    )
    return fig


# The callback for the pie chart 
# process is simillar to the previous callback 
@callback(
    Output('pie1', 'figure'),
    Input('years-slider', 'value'),
    Input('flow_store', 'data')
)
def update_pie1(year, flow):
    dff = overview_data
    dff = overview_data[(overview_data['year'] == year) & (overview_data['flow'] == flow)]
    dff = dff.groupby(['continent'], as_index = False)['Trade volume (USD)'].sum()

    fig = px.pie(dff, 
    names = "continent", 
    values = "Trade volume (USD)",
    hole = 0.65,
    title = "",
    )

    fig.update_layout(margin={"r":30,"t":30,"l":30,"b":30}, 
    plot_bgcolor="rgba( 0, 0, 0, 0)",
    paper_bgcolor="rgba( 0, 0, 0, 0)",
    font = dict(color = "black"),
    title = f'Trade volume (USD) of {flow}s per continent in {str(year)}'
    )
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')

    return fig

# the callback for the scatter plot 
@callback(
    Output('scatter1', 'figure'),
    Input('flow_store', 'data')
)
def update_scatter(flow):
    dff = overview_data[overview_data['flow'] == flow]
    fig = px.scatter(dff, x = 'year', y = 'Trade volume (USD)', color = 'continent', hover_data = ['country'])
    
    fig.update_layout(margin={"r":30,"t":30,"l":30,"b":30}, 
    plot_bgcolor="rgba( 0, 0, 0, 0)",
    paper_bgcolor="rgba( 0, 0, 0, 0)",
    font = dict(color = "black"),
    title = f'Trend of {flow}s overtime, hover on a trace to see countries'
    )
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')

    return fig

# the callback for the table 
@callback(
    Output('table1', 'data'),
    Input('years-slider', 'value'),
    Input('flow_store', 'data')
)
def update_table1(year, flow):
    dff = overview_data
    dff = overview_data[(overview_data['year'] == year) & (overview_data['flow'] == flow)]
    dff = dff[['country', 'Trade volume (USD)']]
    dff = dff.rename(columns = {'country':'Country'})

    return dff.to_dict('records')