# importing dependencies 
import dash
from dash import html, dcc, dash_table
from config import categories, config, blank_fig

# regestering the page to be recognized by the application 
dash.register_page(__name__, path='/detailed-view', name='Detailed view', id = 'page2')

# The layout of the second page.
layout = html.Div([
    # the store components for storing the style of the buttons and the selected flow by the user 
    dcc.Store(id = 'buttons2-store'),
    dcc.Store(id = 'flow2_store'),
    # the title of the page, this gets updated by the callback
    html.Div([
        html.P('Detailed view of exports', id = 'page2-title-text', className = 'title-text')
    ], id = 'page2-title', className = 'title'),
    #the filters and control panel
    html.Div([
        html.Div([
            html.P('Select a trade flow'),
            html.Div([
                # The buttons
                html.Button(['Exports'], id = '2exports-b', className = 'flow-button'),
                html.Button(['Imports'], id = '2imports-b', className = 'flow-button')
            ])
        ], id = 'page2-buttons'),
        html.Div([
            html.P('Select a category'),
            # The dropdown
            dcc.Dropdown(id = 'page2-dropdown', options = categories, value = categories[0])
        ], id = 'page2-dropdown_container')
    ], id = 'page2-filters', className = 'filters-container'),
    # the charts and tables
    html.Div([
        html.Div([
            html.Div([
                # the loading component for the animation when the map is being updated
                dcc.Loading([
                    # the map
                    dcc.Graph(id = 'map2', config = config, figure = blank_fig())
                ]),
                html.I(className='fa fa-expand'),
            ], id = 'map2-container', className = 'container'),
            html.Div([
                dcc.Loading([
                    dcc.Graph(id = 'line2', config = config, figure = blank_fig())
                ]),
                html.I(className='fa fa-expand'),
            ], id = 'line2-container', className = 'container')
        ], className = 'row', id = 'page2-row1'),
        html.Div([
            html.Div([
                dcc.Loading([
                    # the table
                    dash_table.DataTable(id = 'table2', 
                    columns = [{"name": col, "id": col} for col in ['commodity', 'Trade volume (USD)', 'year']],
                    virtualization = True,
                    fixed_rows = {'headers': True},
                    style_cell={
                        'minWidth': '33%', 'width': '33%', 'maxWidth': '33%',
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                    })
                ])
            ], id = 'table2-container', className = 'container-b')
        ], className = 'row-b', id = 'page2-row2'),
    ], id = 'page2-content')

], id = 'page2-layout-main')