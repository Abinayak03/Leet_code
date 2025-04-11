import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    heavy = animals[animals.weight>100]
    des = heavy.sort_values(by='weight',ascending=False)
    return des[['name']]