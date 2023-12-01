import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
  return employees

employees = pd.read_csv('employees.csv')

salaries = modifySalaryColumn(employees)

salaries.to_csv('./salaries.csv')