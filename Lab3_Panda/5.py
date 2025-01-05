# Create a pandas dataframe using list of dics

import pandas as pd

# Create a list of tuples
data = [
    (1, 'Alice', 23),
    (2, 'Bob', 30),
    (3, 'Charlie', 25)
]

# Create a pandas DataFrame using the list of tuples
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])

# Display the DataFrame
print(df)