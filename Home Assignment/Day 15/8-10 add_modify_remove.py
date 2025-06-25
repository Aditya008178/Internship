# 8.	Add a New Column
# o	Add a column Pass which is True if Marks >= 40 else False.
# 9.	Modify an Existing Column
# o	Increase every student’s marks by 5.
# 10.	Remove a Column
# o	Drop the Age column and print the resulting DF.

import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [21, 22, 20, 18, 17],
    'Marks': [74, 73, 80, 70, 22]
}
df = pd.DataFrame(data)


df['Pass'] = df['Marks'] >= 40
print("Add Column Pass: \n")
print(df)
df['Marks'] = df['Marks']+5
print("\n Marks Increased by 5: \n",df)
df = df.drop('Age',axis=1)
print("Remove Age column: \n",df)