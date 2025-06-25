# 11.	Introduce Missing Values
# o	Create a DF with columns Name, Age, Marks where some Age and Marks values are NaN.
# 12.	Check for Missing Values
# o	Use .isnull() and .sum() to count NaNs.
# 13.	Fill Missing Values
# o	Fill NaN in the Marks column with the average marks.
# 14.	Drop Missing Values
# o	Drop rows where any NaN occurs.

import pandas as pd
import numpy as np

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [25, np.nan, 35, 18, np.nan],
    'Marks': [97, 98, np.nan, 80, 90]

}
df = pd.DataFrame(data)

print("Data with missing values: \n",df)
print("Missing values: ",df.isnull().sum())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
print("Fill missing values: \n",df)
print("Drop rows where NaN occurs: \n",df.dropna())