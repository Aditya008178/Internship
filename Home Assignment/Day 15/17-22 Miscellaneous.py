# 17.	Sorting
# o	Sort the DF by Marks in ascending and then in descending order.
# 18.	Rename Columns
# o	Rename columns Name -> Student Name, Marks -> Total Marks.
# 19.	Export DF
# o	Export the final DF to a .csv file named student_records.csv.
# ________________________________________
# 20.	Apply a Function
# o	Use .apply() to categorize marks:
# 	Marks >= 80: Excellent
# 	Marks >= 60: Good
# 	Marks >= 40: Pass
# 	Marks < 40: Fail
# 21.	Check Duplicates
# o	Identify and remove duplicate rows in the DF.
# 22.	Merge Two DataFrames
# o	Create another DF with columns Name and Class Teacher.
# o	Merge both DFs on the Name column.


import pandas as pd


data = {
    'Name': ['Piyush', 'Shubham', 'Prasad', 'Sumedh', 'Ganesh', 'Tanish'],
    'Age': [25, 22, 35, 18, 21, 23],
    'Marks': [97, 98, 89, 80, 90, 91]
}
df = pd.DataFrame(data)

\
df_sorted_asc = df.sort_values(by='Marks', ascending=True)
print("\nSort by Marks in Ascending Order: ",df_sorted_asc)

df_sorted_desc = df.sort_values(by='Marks', ascending=False)
print("\nSort by Marks in Descending Order: ",df_sorted_desc)



df = df.rename(columns={'Name':'Student Name', 'Marks':'Total Marks'})
print("\nRenamed Columns: ",df)



df.to_csv('student_records.csv',index=False)
print("\nExported to student_records.csv")


def categorize_marks(marks):
    if marks>=90:
        print("Excellent")

    elif marks>=80:
        print("Good")

    elif marks>=40:
        print("Pass")
    else:
        print("Fail")

df['Category'] = df['Total Marks'].apply(categorize_marks)
print("\nData with Category Column: ",df)


print("\nDuplicate Rows: ",df[df.duplicated()])


df.loc[len(df)] = df.iloc[0]
print("\nDuplicate Row: ",df)



df = df.drop_duplicates()
print("\nRemoving Duplicates: ",df)



data2 = {
    'Student Name': ['Piyush', 'Shubham', 'Prasad', 'Rohan', 'Aryan'],
    'Class Teacher': ['Ms. Gaidhani', 'Mr. Sangle', 'Ms. Suslade', 'Ms. Waghchoure', 'Mr. Mahajan']
}

df2 = pd.DataFrame(data2)
print("\nDataFrame 2: \n", df2)

merged_df = pd.merge(df, df2, on='Student Name', how='left')
print("\nMerged DataFrame:")
print(merged_df)
