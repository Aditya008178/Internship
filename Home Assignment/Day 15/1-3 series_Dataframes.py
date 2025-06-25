# 1.	Create a Series
# o	Create a Pandas Series from a list of 5 city names.
# 2.	Create a DataFrame
# o	Create a DataFrame called students with columns:
# 	Name (string), Age (int), Marks (float)
# 3.	Check Properties
# o	Print:
# 	.shape
# 	.columns
# 	.dtypes
# 	.info()
# 	.describe() (for numeric columns)


import pandas as pd

s = pd.Series(["Delhi", "Mumbai", "Pune", "Nashik", "Nagpur"])
print(s)

data = {
    'Name': ['Piyush', 'Aditya', 'Prasad'],
    'Age': [25, 30, 35],
    'Marks': [97, 98, 99]
}
df = pd.DataFrame(data)
print(df)

print("Shape: ",df.shape)
print("Columns: ",df.columns)
print("Datatype: ",df.dtypes)
print("Info: ",df.info())
print("Summary: ",df.describe())
