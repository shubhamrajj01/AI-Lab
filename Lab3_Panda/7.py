# Replace values in pandas dataframe using regex(regular expression).

import pandas as pd

data = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 30, 25]
}
df = pd.DataFrame(data)

df['Name'] = df['Name'].replace({'A.': 'Ann', 'B.': 'Ben'}, regex=True)

print(df)