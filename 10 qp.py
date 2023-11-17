import pandas as pd

data = {
    'employee_id': [1, 1, 2, 2, 3, 3, 3],
    'job': ['Developer', 'Designer', 'Developer', 'Manager', 'Manager', 'Designer', 'Developer']
}

df = pd.DataFrame(data)

multiple_jobs = df.groupby('employee_id')['job'].nunique()
employees_with_multiple_jobs = multiple_jobs[multiple_jobs >= 2].index

print("Employees who did two or more jobs in the past:")
print(employees_with_multiple_jobs)
