"""
groupby()
function to form groups based on more than one category
"""
import pandas as pd

# creating the dataframe
df = pd.read_csv('nba.csv')

# first grouping based on "Team"
# Within each team we are grouping based on "Position"
gkk = df.groupby(['Team', 'Position'])

# print the first value in each group
gkk.first()