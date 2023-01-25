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
import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
