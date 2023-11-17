import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(0, 100, size=(10, 4)), columns=['col1', 'col2', 'col3', 'col4'])

df.iloc[0, 0] = np.nan
df.iloc[1, 1] = np.nan
df.iloc[2, 2] = np.nan
df.iloc[3, 3] = np.nan

print(df)
