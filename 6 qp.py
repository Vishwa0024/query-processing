import pandas as pd
import matplotlib.pyplot as plt
dataset = {
    "Date": ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01"],
    "Close": [100, 105, 110, 115, 120],
    "Volume": [100000, 120000, 140000, 160000, 180000]
}

df = pd.DataFrame(dataset)
start_date = "2023-01-01"
end_date = "2023-05-01"
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

plt.scatter(filtered_df['Close'], filtered_df['Volume'])
plt.title("Alphabet Inc. Stock Trading Volume vs. Close Price")
plt.xlabel("Close Price")
plt.ylabel("Trading Volume")
plt.show()
