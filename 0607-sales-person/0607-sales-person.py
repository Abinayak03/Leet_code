import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Merge Company and Orders on com_id
    merged = orders.merge(company, on='com_id', how='inner')

    # Step 2: Get sales_id who dealt with RED company
    red_sales_ids = merged[merged['name'] == 'RED']['sales_id'].unique()

    # Step 3: Filter SalesPerson whose sales_id is NOT in red_sales_ids
    result = sales_person[~sales_person['sales_id'].isin(red_sales_ids)][['name']]

    return result