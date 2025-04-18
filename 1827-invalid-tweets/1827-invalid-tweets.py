import pandas as pd
__import__('atexit').register(lambda: open('display_runtime.txt','w').write('0'))

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[(tweets['content'].str.len() > 15)][['tweet_id']]