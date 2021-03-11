import numpy as np
from sklearn.svm import SVR
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3

model = SVR()
model.fit(X, y)
pred = model.predict(X)

print(pred)