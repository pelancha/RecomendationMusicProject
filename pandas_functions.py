import pandas as pd

df = pd.read_csv('../data/playlist_2010to2022.csv')

def get_shape():
    return df.shape[0]

def get_artist_by_name(artist):

    return "\n".join([f"[{i[0]}]({'https://open.spotify.com/'+i[1]})" for i in df[df["artist_name"] == artist][["track_name", "track_id"]].values])

