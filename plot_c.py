"""
Use 'plot()' method to create diagrams.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()


"""
SCATTER PLOT
Specify that you want a scatter plot with the 'kind' argument:
# kind = 'scatter'
A scatter plot needs an x- ans an y-axis.
"""
# in the example below we will use "Diration' for the x-axis and
# "Calories" for the y-axis.

df2 = pd.read_csv('data.csv')

df2.plot(kind='scatter', x='Duration', y='Calories')
plt.show()

"""
HISTOGRAM
# kind = 'hist'
A histogram needs only one column.
"""
# in the example below we will use "Duration" column to create the
# histogram

df3 = pd.read_csv('data.csv')
df3["Duration"].plot(kind='hist')