# 4.	Column Selection
# o	From the students DF, select the Name column and print it.
# 5.	Row Selection by Position
# o	Use .iloc to print the first 3 rows.
# 6.	Row Selection by Label
# o	Set Name as the index and use .loc to fetch a student by name.
# 7.	Conditional Selection
# o	Select students with Marks > 75.
# o	Select students with Age <= 20.

import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [21, 22, 20, 18, 17],
    'Marks': [74, 73, 80, 70, 22]
}
df = pd.DataFrame(data)
# print(df)

print("Name Column: \n",df['Name'])
print("\nFirst 3 rows: \n", df.loc[:2] )
df.set_index('Name', inplace=True)
print("\nFetch by name: \n",df.loc['Piyush'])
print("\nStudents with marks greater than 75: \n")
print(df[df['Marks'] > 75])
print("\nStudents which age less than 20: ")
print(df[df['Age'] <= 20])

