# Inspect the DataFrame:
# Use .head() and .tail() to view your data.
# Use .info() and .describe() to understand the structure

import pandas as pd


data = {
    'Products': ['Laptop', 'TV', 'Fridge', 'Ac', 'Smartphone'],
    'Price': [88000, 650000, 55000, 50000, 25000],
    'stock': [15, 20, 25, 30, 35]
}
df = pd.DataFrame(data)
print(df.to_string(index = False))


# First 5 rows
print("\n head")
print(df.head())

# Last 5 rows
print("\n Tail")
print(df.tail())



# Info about data types
print("\n Info")
print(df.info())

# Statistical summary
print("\n Summary")
print(df.describe())