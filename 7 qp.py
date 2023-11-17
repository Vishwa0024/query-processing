import pandas as pd
dataset = {
    "Item": ["Phone", "Laptop", "TV", "Fridge", "AC"],
    "Sale Value": [10000, 20000, 30000, 40000, 50000]
}
df = pd.DataFrame(dataset)
pivot_table = df.pivot_table(index='Item', values='Sale Value', aggfunc=['max', 'min'])
print(pivot_table)
