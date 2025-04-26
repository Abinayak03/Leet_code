import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged= employee.merge(department , left_on='departmentId', right_on='id', how='left')
    # Find the max salary for each department (without losing original rows)
    merged['max_salary'] = merged.groupby('name_y')['salary'].transform('max')
    
    # Filter only the top salary earners per department
    grouped = merged[merged['salary'] == merged['max_salary']]

# Rename columns as needed
    grouped = grouped.rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})

    # Select the columns you want in output
    grouped = grouped[['Department', 'Employee', 'Salary']]
    
    # Final result
    return grouped