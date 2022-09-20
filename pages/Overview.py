# importing dependencies 
import dash
from dash import html, dcc, dash_table

from config import blank_fig, config

# registering the page to be recognized by the app.
dash.register_page(__name__, path='/', name='Overview', id = 'page1')

# The layout of the first page.
layout = html.Div([
    # the store components for storing the style of the buttons and the selected flow by the user 
    dcc.Store(id = 'buttons1-store'),
    dcc.Store(id = 'flow_store'),
    # the title of the page, this gets updated by the callback
    html.Div([
        html.P('Overview of exports', id = 'page1-title-text', className = 'title-text')
    ], id = 'page1-title', className = 'title'),
    # the filters and control panel
    html.Div([
        html.Div([
            html.P('Select a trade flow'),
            html.Div([
                # The buttons
                html.Button(['Exports'], id = '1exports-b', className = 'flow-button'),
                html.Button(['Imports'], id = '1imports-b', className = 'flow-button')
            ])
        ], id = 'page1-buttons'),
        html.Div([
            html.P('Select a year'),
            # The slider
            dcc.Slider(min = 1988, max = 2016, step = 1, marks = {str(i): str(i) for i in range(1988, 2017)}, id = 'years-slider', value = 2016)
        ], id = 'page1-slider_container')
    ], id = 'page1-filters', className = 'filters-container'),
    html.Div([
        html.Div([
            html.Div([
                # the loading component for the animation when the map is being update
                dcc.Loading([
                    # The map
                    dcc.Graph(id = 'map1', config = config, figure = blank_fig())
                ]),
                # the icon for maximizing the view 
                html.I(className='fa fa-expand'),
            ], id = 'map1-container', className = 'container'),
            html.Div([
                dcc.Loading([
                    dcc.Graph(id = 'pie1', config = config, figure = blank_fig())
                ]),
                html.I(className='fa fa-expand'),
            ], id = 'pie1-container', className = 'container')
        ], className = 'row', id = 'page1-row1'),
        html.Div([
            html.Div([
                dcc.Loading([
                    dcc.Graph(id = 'scatter1', config = config, figure = blank_fig()),
                ]),
                html.I(className='fa fa-expand'),
            ], id = 'scatter1-container', className = 'container'),
            html.Div([
                dcc.Loading([
                    # The table
                    dash_table.DataTable(id = 'table1', 
                    columns = [{"name": col, "id": col} for col in ['Country', 'Trade volume (USD)']],
                    virtualization = True,
                    fixed_rows = {'headers': True},
                    style_cell={
                        'minWidth': '50%', 'width': '50%', 'maxWidth': '50%',
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                    })
                ])
            ], id = 'table1-container', className = 'container')
        ], className = 'row', id = 'page1-row2'),
    ], id = 'page1-content')

], id = 'page1-layout-main')
