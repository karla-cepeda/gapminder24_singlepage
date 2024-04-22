import dash
import dash_html_components as html # from dash import html 
import dash_core_components as dcc  # from dash import dcc

from gapminder import gapminder

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Create the dash app
app = dash.Dash(__name__)

# Create figure to add to app
fig = px.scatter(data_frame=gapminder, x="gdpPercap", y="lifeExp",
                size="pop", color="continent",hover_name="country", 
               #add frame by year to create animation grouped by country
               animation_frame="year",animation_group="country",
               #specify formating of markers and axes
               log_x = True, size_max=60, range_x=[100,100000], range_y=[28,92],
                # change labels
                labels={'pop':'Population','year':'Year','continent':'Continent',
                        'country':'Country','lifeExp':'Life Expectancy','gdpPercap':"GDP/Capita"})
# Change the axis titles and add background colour using rgb syntax
fig.update_layout({'xaxis': {'title': {'text': 'log(GDP Per Capita)'}},
                  'yaxis': {'title': {'text': 'Life Expectancy'}}}, 
                  plot_bgcolor='rgb(233, 238, 245)',paper_bgcolor='rgb(233, 238, 245)')

# https://markdowntohtml.com/
# markdown is a lightweight markup language for quick formating. 
markdown_text = '''
### Dash and Markdown
Just adding a lot of text here to explain the Dash markdown components 
''' 

#change background and color text
colors = {
    #background to rgb(233, 238, 245)
    'background': '#e9eef5',
    'text': '#1c1cbd'
}

#layout of the app using divisions (sections)
app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1('Gapminder',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    #Add multiple line text 
    html.Div('''
        Life Expectancy vs GDP per Capita for all Countries from 1952 to 2007 
    ''', style={
        'textAlign': 'center',
        'color': colors['text']}
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig 
    ),
     dcc.Markdown(children=markdown_text,style={
            'textAlign': 'center',
            'color': colors['text']
    })
])


if __name__ == '__main__':
    app.run_server(port=8091,debug=True)