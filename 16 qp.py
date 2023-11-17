import pandas as pd
df = pd.DataFrame({'school_code': [101, 102, 103, 104, 105],
                   'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
                   'age': [12, 13, 14, 15, 16]})

grouped_df = df.groupby('school_code')
print(type(grouped_df))
for group_name, group_df in grouped_df:
    print(group_name)
    print(group_df)
