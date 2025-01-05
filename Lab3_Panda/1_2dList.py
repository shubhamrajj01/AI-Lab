# Make pa panda dataframe with 2D list.

import pandas as pd

# Create a 2D list
data = [
    [1, 'Alice', 23],
    [2, 'Bob', 30],
    [3, 'Charlie', 25]
]

# Create a pandas DataFrame using the 2D list
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])

# Display the DataFrame
print(df)