# Imports

import spotipy
import os
import pandas as pd
import seaborn as sns 
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

# Conection

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

load_dotenv()

url = "spotify:artist:4gzpq5DPGxSnKTe4SA8HAU"
coldplay = "4gzpq5DPGxSnKTe4SA8HAU"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

results = spotify.artist_top_tracks(url)
results

# DF

if results :
    tracks = results['tracks']

tabla = pd.DataFrame(tracks)

popu = tabla[['name', 'popularity', 'duration_ms']]
popu

top_popu = popu.sort_values('duration_ms', ascending = False)

top3 = top_popu.head(3)
top3

# Scatter plot

scatter = sns.scatterplot(y='popularity', x='duration_ms', data=top_popu)
scatter

## No se observa ninguna relacion directa entre la duración y la popularidad entre canciones. 