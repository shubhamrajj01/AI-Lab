# 2.Create dataframe from dic of n array or list

import pandas as pd

data = [[2, 2, 0], [5, 3, 1], [9, 4, 0]]
df = pd.DataFrame(data, columns=['A', 'B','C'])
print(df)