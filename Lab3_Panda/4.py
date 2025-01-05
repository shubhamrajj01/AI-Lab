# Create a pandas dataframe using list of tuples

import pandas as pd

# List of lists
data = [
    [101, "Alice", 28],
    [102, "Bob", 34],
    [103, "Charlie", 23]
]

# Column names
columns = ["ID", "Name", "Age"]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(df)