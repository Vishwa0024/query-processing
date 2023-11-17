import pandas as pd
import matplotlib.pyplot as plt
dataset = {
    "Date": ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01"],
    "Close": [100, 105, 110, 115, 120]
}
df = pd.DataFrame(dataset)

start_date = "2023-01-01"
end_date = "2023-05-01"
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

plt.plot(filtered_df['Date'], filtered_df['Close'])

plt.title("Alphabet Inc. Stock Prices")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.show()
