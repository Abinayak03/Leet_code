import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    # Remove duplicates and sort
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)

    # Check if N is within range
    if N <= len(unique_salaries):
        return pd.DataFrame({f'getNthHighestSalary({N})': [unique_salaries.iloc[N - 1]]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
