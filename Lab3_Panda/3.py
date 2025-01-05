# Create pandas dataframe using list of lists.

import pandas as pd

# Create a dictionary of lists
data = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 30, 25]
}

# Create a pandas DataFrame using the dictionary of lists
df = pd.DataFrame(data)

# Display the DataFrame
print(df)