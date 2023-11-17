import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Name": ["Alice", "Bob", np.nan, "Carol", "Dave"],
    "Age": [25, 30, np.nan, 35, 40],
    "Salary": [100000, 120000, np.nan, 140000, 160000]
})
df_filtered = df[df.isnull().sum(axis=1) >= 2]
print(df_filtered)
