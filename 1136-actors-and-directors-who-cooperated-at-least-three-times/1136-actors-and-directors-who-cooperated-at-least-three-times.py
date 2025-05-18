import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id','director_id'],as_index=False)['timestamp'].count()
    return df[df['timestamp'] >= 3][['actor_id','director_id']]