"""DATA FRAMES
Data sets in Pandas are usually multi-dimensional tables, callled
DataFrames.
Series is like a column, a DataFrame is the whole table.
A Pandas DataFrame is a 2 dimensional datat structure, like a 2
dimensional array, or table with rows and columns.
"""

# create a DataFrame from two Series

import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

"""
LOCATE ROW
From the result above, the DataFrame is like a tablr with rows
and columns.
Pandas use the 'loc' attribute to return one or more specified row(s).
"""

# return row 0:
# refer to the row index
print(df.loc[0])


"""
NAMED INDEXES
with the 'index' argument, you can name your own indexes.
"""
# add a list of names to give each row a name:
data2 = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ['day1', 'day2', 'day3'])

print(df)
