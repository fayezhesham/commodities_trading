# importing dependencies 
import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output
from callbacks import main_callbacks, page1_callbacks, page2_callbacks

# initializing the dash app
app = dash.Dash(__name__, use_pages=True, suppress_callback_exceptions = True, external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.1/css/all.min.css'])

# creating the navigation bar layout 
navbar = html.Div([
                    html.A(html.Div([page["name"]], id = page['id'], className = 'nav-button'), href = page['path'], className = 'nav-link')
                    for page in dash.page_registry.values()
            ], id = 'nav-container')

# setting the layout of the app 
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    dcc.Store(id = 'styles'),
    navbar,
    html.Div([dash.page_container])
])




# running the app 
if __name__ == "__main__":
    app.run(debug=False)