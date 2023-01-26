"""
MERGE
A single function as the entry point for all standard
database join operations between DataFrame.
"""
import pandas as pd
left = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5']
})
right = pd.DataFrame({
'id': [1, 2, 3, 4, 5],
    'Name': ['Billy', 'Brian', 'Bram', 'Bryce', 'Betty'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5']
})
print(left)
print(right)
print(' \n ')
"""
Merge Two DataFrames on a Key
"""
print(pd.merge(left, right, on='id', 'subject_id'))
