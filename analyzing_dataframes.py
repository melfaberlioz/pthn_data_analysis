"""
Viewing the Data
Method for getting a quik overview of the DataFrame, is the
HEAD() method.
The 'head()' method returns the headers and a specified number of
rows, starting from the top.
"""

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
# if the number of rows isn't specified, the
# 'head()' method will return the top 5 rows.

df2 = pd.read_csv('data.csv')
print(df.head())


"""
There is also a 'tail()' method for viewing the LAST
rows fo the DataFrame.
The 'tail()' method returns the header and a specified number
of rows, starting from the bottom.
"""
print(df.tail())