# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:06:23 2022

@author: Aman Ailani
"""
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

#Importing and Cleaning Data
df = pd.read_csv(r"C:\Users\Aman Ailani\Desktop\Data Science\Spotify 2010 - 2019 Top 100.csv")

df = df.dropna()

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Munging Data to have 10 main genres 


needed = ['dance pop', 'pop', 'atl hip hop', 'hip hop', 'boy band', 'canadian hip hop', 'edm', 'folk-pop']

for genre in df['top genre']:
    if genre not in needed:
        df = df.replace([genre],'other')

#creating new column for energy level of song 
def f(energy):
    if energy['nrgy'] < 40:
        val = 'low'
    elif energy['nrgy'] < 55:
        val = 'medium'
    else:
        val = 'high'
    return val
df['Energy Level of Song'] = df.apply(f, axis=1)

#creating new column for danceability of song 
def d(dancing):
    if dancing['dnce'] < 30:
        val = 'low'
    elif dancing['dnce'] < 60:
        val = 'medium'
    else:
        val = 'high'
    return val

df['Dancing Power'] = df.apply(d, axis=1)

df["top year"] = df["top year"].astype(str)
df.rename(columns = {'nrgy':'energy', 'dnce':'danceability', 'acous':'softness', 'spch':'wordiness', 'dB':'decibels', 'val':'positivity'}, inplace = True)
df.drop(['year released', 'live', 'wordiness', 'decibels', 'dur', 'added'], axis=1, inplace=True)
### pandas dataframe to html table

def generate_table(dataframe, max_rows=25):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=stylesheet)
server = app.server

fig = px.bar(df, x="title", y="bpm", color="top year")


app.layout = html.Div([
    html.H1('Have Songs in the Last Decade Become More Upbeat?',
            style={'textAlign' : 'center'}),
    html.A('Click to view full dataset',
           href='https://www.kaggle.com/datasets/muhmores/spotify-top-100-songs-of-20152019',
           target='_blank'),
    dcc.Graph(figure=fig, id='plot'),
    html.Div([html.H4('List of Top Genres:'),
              dcc.Dropdown(
                  options=[{'label': 'Dance Pop', 'value': 'dance pop'},
                           {'label': 'Pop', 'value': 'pop'},
                           {'label': 'Atlanta Hip Hop', 'value': 'atl hip hop'},
                           {'label': 'Hip Hop', 'value': 'hip hop'},
                           {'label': 'Boy Band', 'value': 'boy band'},
                           {'label': 'Canadian Hip Hop', 'value': 'canadian hip hop'},
                           {'label': 'EDM', 'value': 'edm'},
                           {'label': 'Folk-Pop', 'value': 'folk-pop'},
                           {'label': 'Others', 'value': 'other'}],
                  value=['other', 'dance pop', 'pop', 'atl hip hop', 'hip hop', 'boy band', 'canadian hip hop', 'edm', 'folk-pop', 'other'],
                  id = 'checklist')],
             style={'width' : '50%', 'float' : 'right'}),
    html.Div([html.H4('Types of Artists'),
              dcc.Dropdown(
                  options=[{'label': 'Solo', 'value': 'Solo'},
                           {'label': 'Band/Group', 'value': 'Band/Group'},
                           {'label': 'Duo', 'value': 'Duo'},
                           {'label': 'Trio', 'value': 'Trio'}],
                  value=['Solo', 'Band/Group', 'Duo', 'Trio'],
                  id = 'checklist2')],
             style={'width' : '50%', 'float' : 'left'}),
    html.Div([html.H4('Energy Level of Song:'),
              dcc.Dropdown(
                  options=[{'label': 'low', 'value': 'low'},
                           {'label': 'medium', 'value': 'medium'},
                           {'label': 'high', 'value': 'high'}],
                  value=['low', 'medium', 'high'],
                  id = 'checklist3')],
             style={'width' : '50%', 'float' : 'right'}),
    html.Div([html.H4('Dancing Power of Song:'),
              dcc.Dropdown(
                  options=[{'label': 'low', 'value': 'low'},
                           {'label': 'medium', 'value': 'medium'},
                           {'label': 'high', 'value': 'high'}],
                  value=['low', 'medium', 'high'],
                  id = 'checklist4')],
             style={'width' : '50%', 'float' : 'left'}),
    html.Div(id='table')
    ])

# Callbacks for Genres to update table & plot 
@app.callback(
    Output("table", "children"),
    [Input("checklist", "value"),
    Input("checklist2", "value"),
    Input("checklist3", "value"),
    Input("checklist4", "value")]
)
def update_table(genres, artists, energy, dance):
    x = df[df['top genre'] == genres].sort_values('bpm')
    x = x[x['artist type'] == artists].sort_values('bpm')
    x = x[x['Energy Level of Song'] == energy].sort_values('bpm')
    x = x[x['Dancing Power'] == dance].sort_values('bpm')
    return generate_table(x)

@app.callback(
    Output("plot", "figure"),
    [Input("checklist", "value"),
    Input("checklist2", "value"),
    Input("checklist3", "value"),
    Input("checklist4", "value")]
)
def update_plot(genres, artists, energy, dance):
    df2 = df[df['top genre'] == genres].sort_values('top year', ascending=True)
    df2 = df2[df2['artist type'] == artists].sort_values('top year', ascending=True)
    df2 = df2[df2['Energy Level of Song'] == energy].sort_values('top year', ascending=True)
    df2 = df2[df2['Dancing Power'] == dance].sort_values('top year', ascending=True)
    fig = px.bar(df2, x="title", y="bpm", color="top year")
    return fig


if __name__ == '__main__':
    app.run_server(debug=False)