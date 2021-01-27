# 导入需要的库
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

celsius = [[-40], [-10], [0], [8], [15], [22], [38]]
fahrenheit = [[-40], [14], [32], [46.4], [59], [71.6], [100.4]]



lr = LinearRegression()
lr.fit(celsius, fahrenheit)

celsius_test = [[-50], [-30], [10], [20], [50], [70]]
fahrenheit_test = lr.predict(celsius_test)
plt.scatter(celsius, fahrenheit, c='red', label='real')
plt.scatter(celsius_test, fahrenheit_test, c='orange', label='predicted')

plt.xlabel('celsius')
plt.ylabel('fahrenheit')
plt.legend()  # 图例
plt.grid(True)  # 设置网格，途中红色虚线
plt.title('estimated vs real data')
plt.show()
