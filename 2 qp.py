import pandas as pd
dataset = {
    "employee_id": [101, 102, 103, 104, 105],
    "job_id": ["IT_PROG", "AC_ACCOUNT", "HR_REP", "MK_REP", "SA_REP"],
    "start_date": ["2001-01-01", "1999-12-31", "2000-01-01", "2002-01-01", "2003-01-01"],
    "end_date": ["2005-12-31", "2006-12-31", "2007-12-31", "2008-12-31", "2009-12-31"]
}
df = pd.DataFrame(dataset)
grouped_df = df.groupby('employee_id')
filtered_grouped_df = grouped_df.filter(lambda x: len(x) > 1)
employee_ids = filtered_grouped_df['employee_id'].unique()

print(employee_ids)
