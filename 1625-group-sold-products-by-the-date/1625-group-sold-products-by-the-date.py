import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities=activities.drop_duplicates()
    activities = activities.groupby('sell_date',as_index=False)[['product']].agg(
        num_sold = ('product','count'),
        products = ('product', lambda x : ','.join(sorted(x)))
    )
    return activities