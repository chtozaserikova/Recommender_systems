import pandas as pd
import numpy as np
from ast import literal_eval



def clean_data(df):
    relevant_features = ['title','genres', 'release_date', 'runtime', 'vote_average', 'vote_count', 'overview', 'id']
    df = df[relevant_features]

    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['year'] = pd.DatetimeIndex(df['release_date']).year
    df = df.drop('release_date', axis=1)  

    df['genres'] = df['genres'].fillna('[]')
    df['genres'] = df['genres'].apply(literal_eval)
    df['genres'] = df['genres'].apply(lambda x: [i['name'].lower() for i in x] if isinstance(x, list) else [])

    return df
