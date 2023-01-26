import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.size'] = [7.50, 3.50]
plt.rcParams['figure.autolayout'] = True

headers = ['Name', 'Age', 'Marks']

# with the 'index' gives each rows name
df = pd.read_csv('student.csv', names=headers)

# load data into DataFrame object
df.set_index('Name').plot()

plt.show()
