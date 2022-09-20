# importing dependencies 
import dash
from dash import callback, dcc, html, Input, Output, ctx
import plotly.express as px
from config import detailed_data, countries, token

# The next 2 callbacks are similar to the other 2 callbacks in the first page for storing the style of the buttons and the trade flow. 
@callback(
    Output('buttons2-store', 'data'),
    Output('flow2_store', 'data'),
    Input('2exports-b', 'n_clicks'),
    Input('2imports-b', 'n_clicks')
)
def update_buttons2_style(button1, button2):
    button_id = ctx.triggered_id if not None else '2exports-b'
    if button_id == '2exports-b':
        styles = [{'background-color': '#313a46', 'color': 'white'}, None]
        flow = 'Export'
    elif button_id == '2imports-b':
        styles = [None, {'background-color': '#313a46', 'color': 'white'}]
        flow = 'Import'
    else:
        styles = [{'background-color': '#313a46', 'color': 'white'}, None]
        flow = 'Export'

    return styles, flow


@callback(
    Output('2exports-b', 'style'),
    Output('2imports-b', 'style'),
    Input('buttons2-store', 'data')
)
def update_buttons2_styles(styles):
    return styles[0], styles[1]


# This callback updates the title according to the selected flow.
@callback(
    Output('page2-title-text', 'children'),
    Input('flow2_store', 'data')
)
def update_overview_title(flow):
    return f'Detailed view of {flow}s'


# the callback for the second map.
# similar to the map in the first page.
@callback(
    Output('map2', 'figure'),
    Input('page2-dropdown', 'value'),
    Input('flow2_store', 'data')
)
def update_map2(category, flow):
    dff = detailed_data[(detailed_data['category'] == category) & (detailed_data['flow'] == flow)]
    dff = dff.groupby(['country'], as_index = False)['Trade volume (USD)'].sum()

    fig = px.choropleth_mapbox(dff, 
                           geojson=countries, 
                           locations="country", 
                           color= "Trade volume (USD)",
                           featureidkey= "properties.admin",
                           color_continuous_scale = 'GnBu',
                           zoom = 1,
    )

    fig.update_layout(margin={"r":0,"t":30,"l":0,"b":0}, 
    mapbox_accesstoken = token,  
    dragmode= False,
    plot_bgcolor="rgba( 0, 0, 0, 0)",
    paper_bgcolor="rgba( 0, 0, 0, 0)",
    title = f'{flow}s volume (USD) of {category[3:]} per country.'
    )
    return fig


# the callback for the line chart 
@callback(
    Output('line2', 'figure'),
    Input('page2-dropdown', 'value'),
    Input('flow2_store', 'data')
)
def update_line2(category, flow):
    dff = detailed_data[(detailed_data['category'] == category) & (detailed_data['flow'] == flow)]
    dff = dff.groupby(['commodity', 'year'], as_index = False)['Trade volume (USD)'].sum()

    fig = px.line(dff, x = 'year', y = 'Trade volume (USD)', color = 'commodity')

    fig.update_layout(margin={"r":30,"t":30,"l":30,"b":30}, 
    plot_bgcolor="rgba( 0, 0, 0, 0)",
    paper_bgcolor="rgba( 0, 0, 0, 0)",
    font = dict(color = "black"),
    showlegend = False,
    title = f'Trend of {flow}s of each commodity in {category}, hover to see commodities'
    )
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    return fig


# the callback for the second table 
@callback(
    Output('table2', 'data'),
    Input('page2-dropdown', 'value'),
    Input('flow2_store', 'data')
)
def update_table2(category, flow):
    dff = detailed_data[(detailed_data['category'] == category) & (detailed_data['flow'] == flow)]
    dff = dff.groupby(['commodity', 'year'], as_index = False)['Trade volume (USD)'].sum()
    return dff.to_dict('records')