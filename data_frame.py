"""DATA FRAMES
Data sets in Pandas are usually multi-dimensional tables, callled
DataFrames.
Series is like a column, a DataFrame is the whole table.
A Pandas DataFrame is a 2 dimensional datat structure, like a 2
dimensional array, or table with rows and columns.

DataFrame can be made of more than one series or we can say that a
dataframe is a collection of series that can be used to analyse the data.
"""
import pandas as pd

# creating DataFrame from multiple Series
writer = ['Jitender', 'Purnima', 'Arpit', 'Jyoti']
article = [210, 211, 114, 178]

# creating two series by passing list
writer_series = pd.Series(writer)
article_series = pd.Series(article)

# creating a dictionary by passing Series objects as values
frame = {'Author': writer_series, 'Article': article_series}

# creating DataFrame by passing Dictionary
result = pd.DataFrame(frame)

"""ADD A NEW COLUMN"""
age = [21, 21, 24, 23]
# creating new column in the dataframe by providing a Series
result['Age'] = pd.Series(age)

print(result)


# create a DataFrame from two Series
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

