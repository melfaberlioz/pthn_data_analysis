import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gasPrice = pd.read_csv('gas_prices.csv')
plt.plot(gasPrice.Year, gasPrice.Canada)