import pandas as pd
dataset = {
    "Item": ["Phone", "Laptop", "TV", "Fridge", "AC"],
    "Unit Sold": [100, 50, 25, 10, 5]
}

df = pd.DataFrame(dataset)
pivot_table = df.pivot_table(index='Item', values='Unit Sold', aggfunc='sum')
print(pivot_table)
