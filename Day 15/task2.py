# Create a DataFrame:
# Create a DataFrame with columns: Products, Price, and Stock.
# Add 5 sample rows.

import pandas as pd

data = {
    'Products': ['Laptop', 'TV', 'Fridge', 'Ac', 'Smartphone'],
    'Price': [88000, 650000, 55000, 50000, 25000],
    'stock': [15, 20, 25, 30, 35]
}
df = pd.DataFrame(data)
print(df.to_string(index=False))
