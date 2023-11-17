import pandas as pd

# Create a dataset
dataset = {
    "Region": ["East", "West", "Central"],
    "Manager": ["Martha", "Douglas", "Hermann"],
    "SalesMan": ["Alexander", "Michael", "Shelli"],
    "Sale Amount": [10000, 20000, 30000]
}

df = pd.DataFrame(dataset)
pivot_table = df.pivot_table(index=['Region', 'Manager', 'SalesMan'], values='Sale Amount', aggfunc='sum')

print(pivot_table)
