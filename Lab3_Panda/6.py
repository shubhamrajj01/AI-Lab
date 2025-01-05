# Convert list of nested dictionary into pandas dataframe
import pandas as pd

data = [
    {'ID': 1, 'Name': 'Alice', 'Age': 23},
    {'ID': 2, 'Name': 'Bob', 'Age': 30},
    {'ID': 3, 'Name': 'Charlie', 'Age': 25}
]

df = pd.DataFrame(data)

print(df)