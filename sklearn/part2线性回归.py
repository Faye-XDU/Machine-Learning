import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
#拟合图形 y = 1*x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression()
reg.fit(X, y)

# print(y)

print(reg.coef_)
print(reg.intercept_)
pre =  reg.predict(np.array([[3, 5]]))
print(pre)
