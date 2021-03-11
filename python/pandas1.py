import numpy as np
import pandas as pd

# pandas.Series

x = pd.Series([1, 3, 5, np.nan, 6, 8], index=['a', 'b', 'c', 'd', 'e', 'f'])
# print(x)

# pandas.DataFrame

x = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index=[
                 'i', 'ii', 'iii'], columns=['A', 'B', 'C'])
print(x)
# 其中index对应它的行，columns对应它的列
