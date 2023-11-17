import pandas as pd
df = pd.DataFrame({'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
                   'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
                   'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank'],
                   'age': [12, 13, 14, 15, 16, 17]})

grouped_df = df.groupby(['school_code', 'class'])
for group_name, group_df in grouped_df:
    print(group_name)
    print(group_df)
