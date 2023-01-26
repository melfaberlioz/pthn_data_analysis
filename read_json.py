"""
READ JSON
Big data sets are often stored as JSON.
JSON is plain text, but has the format of an OBJECT.
"""
import pandas as pd
df = pd.read_json('data.json')
print(df.to_string())

