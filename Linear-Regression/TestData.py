#导入需要的库
import numpy as np
import pandas as pd

#导入数据集
dataset = pd.read_csv("D:/Python/Machine Learning/Linear-Regression/Data1.csv") #读取数据
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , 3].values #读取所有的行和列

print(X)
print(Y)