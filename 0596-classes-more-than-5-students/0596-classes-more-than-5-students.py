import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    counts = courses['class'].value_counts()
    popular = counts[counts>=5].index.tolist()
    return pd.DataFrame({'class': popular})