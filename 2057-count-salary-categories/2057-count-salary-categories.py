import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    def get_salary(salary):
        if salary < 20000:
            return "Low Salary"
        elif salary >= 20000 and salary <= 50000 :
            return "Average Salary"
        else:
            return "High Salary"
    accounts['range'] = accounts['income'].apply(get_salary)
     # Group and count
    result = accounts.groupby('range').size().reset_index(name='accounts_count')

    # Rename column
    result.rename(columns={'range': 'category'}, inplace=True)

    # Ensure all 3 categories are present in final result
    all_categories = ['Low Salary', 'Average Salary', 'High Salary']
    result = result.set_index('category').reindex(all_categories, fill_value=0).reset_index()

    return result