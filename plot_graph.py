import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gasPrice = pd.read_csv('gas_prices.csv')
plt.plot(gasPrice.Year, gasPrice.Canada)

# adding titles
plt.suptitle('Gas Price Comparison')
plt.title('Canada', fontdict={'fontsize': 15, 'fontweight': 'bold'})
plt.xlabel('Year')
plt.ylabel('Price in USD')