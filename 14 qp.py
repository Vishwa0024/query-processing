import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Alice", "Bob", np.nan, "Carol", "Dave"],
    "Age": [25, 30, np.nan, 35, 40],
    "Salary": [100000, 120000, np.nan, 140000, 160000]
})
columns_with_missing_values = df.columns[df.isnull().any()]
for column in columns_with_missing_values:
    df[column].fillna("", inplace=True)

print(df)

