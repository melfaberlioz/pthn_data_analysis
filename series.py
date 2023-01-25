"""PANDAS
It's a Python library used for working with data sets.

Why Use Pandas?
Allows to analyze big data and make conclusions based on
statistical theories. Pandas can clean messy data sets, and make them
readable and relevant.

Pandas as pd
Pandas is usually imported under the pd alias.
# import pandas as pd
"""

"""SERIES
is one-dimensional array-like object containing
an array of data and an associated array of data
labels (indexes).
"""

import pandas as pd

import numpy as np

data = np.array(['g', 'e', 'e', 'k', 's'])

# a = [1, 7, 2]
obj = pd.Series(data)
print(obj)

"""
Series displays the index on the left and the value
on the right. If nothing else is specified, the values 
are labeled with their index number. First value has index
0, second value has index 1 etc.
You can get the array representation and index object of the
Series via its values and index attributes.
"""

# CREATION OF YOUR OWN LABELS
a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)
# when you have created labels, you can access an item
# by referring to the label.

# Return the value of "y":
print(myvar["y"])


"""
You can also use key/value object, like a dictionary, when creating Series.
"""
# Create a simple Pandas Series from a dictionaty

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
# the key of the dictionary become the labels
print(myvar)

"""
To select only some of the items in the dictionary, use the 'index' :argument
and specify only the items you want to include in the Series
"""

myvar2 = pd.Series(calories, index = ['day1', 'day2'])
print(myvar2)


""" 
CREATING A SERIES FROM LIST
In order to create a series from list, we have to first create a 
list after that we can create a series from a list.
"""

# a simple list
list = ['g', 'e', 'e', 'k', 's']

# create series form a list
ser = pd.Series(list)
print(ser)


"""
Indexing and Selecting Data in Series
Indexing means selecting particular data from a Series.

INDEXING A SERIES USING INDEXING OPERATOR []:
Indexing operator is used to refer to the square brackets 
following an object. 
"""
# making data frame
df = pd.read_csv("nba.csv")

ser = pd.Series(df["Name"])
data = ser.head(10)
print(data)
print(" \n ")

"""
Create a Series from Scalar
If data is a scalar value, an index must be provided.
The value will be repeated to match the length of index.
"""
s = pd.Series(5, index=[1, 2, 3])
print s
