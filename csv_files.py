"""
READ CSV Files
A simple way to store big data sets is to use CSV files (comma separated
files).
"""
# Load the data.csv into a DataFrame:

import pandas as pd
df = pd.read_csv('data.csv')
# use 'to_string()' to print the entire DataFrame
print(df.to_string())

print(" \n \n ")

"""
If you have a large DataFrame with many rows, Pandas will only return the first
5 rows, and the last 5 rows.
"""
# print the DataFrame without the 'to_string()' method:
df_2 = pd.read_csv('data.csv')
print(df)

print(" \n \n ")

"""
SELECT SUBSET OF COLUMNS
If you want to select a subset of columns from the CSV file:
"""
data = pd.read_csv('data.csv')
df_3 = pd.DataFrame(data, columns=['Duration', 'Calories'])
print(df_3)