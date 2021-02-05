import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.reshape(np.random.rand(100), [-1, 1])
salt = np.random.randn(100, 1) * 0.2
y = 0.3 * X + 1 + salt
reg = LinearRegression()
reg.fit(X, y)
y_pred = reg.coef_ * X + reg.intercept_
print(reg.coef_)
print(reg.intercept_)

plt.scatter(X, y)
plt.plot(X, y_pred, color = 'r')
plt.show()