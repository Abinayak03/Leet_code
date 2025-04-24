import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted=employee['salary'].sort_values(ascending=False).drop_duplicates()

    if len(sorted)<2:
        return pd.DataFrame({'SecondHighestSalary' : [None]})

    else:
        return pd.DataFrame({'SecondHighestSalary' : [sorted.iloc[1]]})