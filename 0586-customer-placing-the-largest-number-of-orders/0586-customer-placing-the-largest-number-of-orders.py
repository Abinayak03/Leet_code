import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
   orders = orders.groupby('customer_number',as_index=False)['order_number'].count()
   orders= orders.sort_values(by='order_number',ascending= False)
   if orders.empty:
        return pd.DataFrame(columns=['customer_number'])

   return orders.iloc[[0]][['customer_number']]
   