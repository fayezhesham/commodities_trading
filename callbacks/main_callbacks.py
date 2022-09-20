# importing dependencies 
from dash import callback, dcc, html
from dash.dependencies import Input, Output

# This callback controls the style of the navigation buttons according to the current page 
# The output is in a dcc.Store component which then will be used in the next callback
@callback(
    Output('styles', 'data'),
    Input('url', 'pathname')
)
def update_styles(path):
    if path == '/':
        styles = [{'background-color': '#94c4d4', 'color': 'black'}, None]
    elif path == '/detailed-view':
        styles = [None, {'background-color': '#94c4d4', 'color': 'black'}]
    else: 
        styles = [None]*2
    return styles


# This callback takes the input from the dcc.Store component from the callback above and outputs the style of the navigation buttons.
@callback(
    Output('page1', 'style'),
    Output('page2', 'style'),
    Input('styles', 'data')
)
def update_button_style(styles):
    return styles[0], styles[1]