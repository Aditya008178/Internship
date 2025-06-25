# Selection and Indexing:
# Select only the Name column.
# Select the first 3 rows using .iloc.
# Select people older than 30.


import pandas as pd

data = {
    'Name': ['Aditya', 'Piyush', 'Prasad' , 'Shubham', 'Sumedh'],
    'Age': [36, 31, 35, 22, 23],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Nashik', 'Hyderabad']
}
df = pd.DataFrame(data)

print(" Only the Name column")
print(df['Name'])
# print(df.Name)

print("\n First 3 rows")
print(df.iloc[2]) 

print("\n People older than 30")
print(df[df['Age'] > 30])

