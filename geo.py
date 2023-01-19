import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Carrega o arquivo CSV como um DataFrame do Pandas
df = pd.read_csv("novo_v2.csv")

zmin = df['densidade_demografica'].min()
zmax = df['densidade_demografica'].max()

sizeref = df['densidade_demografica'].max() / 1000

# Cria o heatmap em 3D usando latitude, longitude, densidade demográfica
fig = go.Figure(data=[go.Cone(
    x=df['longitude'],
    y=df['latitude'],
    z=df['densidade_demografica'],
    
    u=np.zeros(df.shape[0]),
    v=np.zeros(df.shape[0]),
    w=np.ones(df.shape[0]),
    colorscale='Viridis',
    sizemode="scaled",
    sizeref=sizeref,
    text=df['nome'],
    hoverinfo='text'
)])
fig.update_layout(scene = dict(
                    xaxis_title='Longitude',
                    yaxis_title='Latitude',
                    zaxis_title='Densidade Demográfica',
                    xaxis_range=[df['longitude'].min(), df['longitude'].max()],
                    yaxis_range=[df['latitude'].min(), df['latitude'].max()],
                    zaxis_range=[df['densidade_demografica'].min(), df['densidade_demografica'].max()],
                    aspectmode = "manual",
                    aspectratio = dict(x=1.6, y=1, z=1)
                ))
fig.show()
