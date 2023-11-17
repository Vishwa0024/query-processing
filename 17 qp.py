import pandas as pd
df = pd.DataFrame({'school_code': [101, 102, 103, 104, 105],
                   'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
                   'age': [12, 13, 14, 15, 16]})

grouped_df = df.groupby('school_code')
agg_df = grouped_df['age'].agg(['mean', 'min', 'max'])
print(agg_df)
