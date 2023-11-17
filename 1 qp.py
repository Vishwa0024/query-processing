import pandas as pd

dataset = {
    "employee_id": [101, 102, 103, 104, 105],
    "department_id": [90, 60, 100, 30, 50]
}

df = pd.DataFrame(dataset)
distinct_department_ids = df['department_id'].unique()
print(distinct_department_ids)
