"""
Use 'plot()' method to create diagrams.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()
