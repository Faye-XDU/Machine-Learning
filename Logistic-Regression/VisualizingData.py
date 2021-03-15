import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


path = 'ex2data1.txt'
data = pd.read_csv(path, header=None, names=['Exam1', 'Exam2', 'Admitted'])
data.head()

positive = data[data['Admitted'].isin([1])]
nagative = data[data['Admitted'].isin([0])]

fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(positive['Exam1'], positive['Exam2'], s=50, c='b', marker='o', label='Admitted')
ax.scatter(nagative['Exam1'], nagative['Exam2'], s=50, c='r', marker='x', label='Not Admitted')
ax.legend()
ax.set_xlabel('Exam1_score')
ax.set_ylabel('Exam2_score')
plt.show()