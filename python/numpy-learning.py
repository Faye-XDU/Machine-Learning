import numpy as np

# 创建数组

arr = np.array([1, 2, 3, 4, 5])
# for a in arr:
#     print(a)
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mtrx = np.array(my_matrix)

# 索引和切片

# print(mtrx[1, 1], arr[:3])

# dtype

arr2 = np.array(['asdfwerf', 'b', 'c'])
arr1 = np.array(['1', '2', '3'], dtype='f')

print(arr2.dtype, arr1.dtype)

# 一般方法

arr3 = np.arange(0, 101, 2)
# print(arr3)
np.zeros((2, 5))
np.ones((4, 4))
np.eye(5)
np.random.seed(99)
arr4 = np.random.randn(10)
print(arr4)
arr5 = np.random.randint(0, 101, (4, 5))
# print(arr5)
# print(arr5.max(),arr5.min())

#进阶用法
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#reshape

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12])
newarr = arr.reshape(4, 3)

# print(arr.shape,newarr.shape)
# print(newarr)

#合并和分割

arr1 = np.array([[1, 2, 3], [11, 12, 13]])
arr2 = np.array([[4, 5, 6], [14, 15, 16]])
arr = np.concatenate((arr1,arr2), axis=1)
#axis == 1按列合并，否则按行合并
# print(arr)

newarr = np.array_split(arr, 2)
# print(newarr)

#搜索和筛选

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12])
x = np.where(arr%2 == 0)
# print(x)
# print(arr[arr > 4])

#排序

arr = np.array(['banana', 'cherry', 'apple'])
np.sort(arr)

# print(arr)

#随机

arr = np.random.choice([3, 5, 6, 9], p=[0.1, 0.3, 0.6, 0], size=(100))
# print(arr)

#随机排列

np.random.seed(99)
arr = np.array([1, 2, 3, 4, 5])
newarr = np.random.permutation(arr) #原数组不改变
# print(newarr)
# print(arr)
newarr = np.random.shuffle(arr)
# print(newarr)
# print(arr)

#正态分布

x = np.random.normal(loc=1, scale=2, size=(2, 3))
# print(x)
# sns.distplot(x, hist=False)
# plt.show()

#二项分布

x = np.random.binomial(n=9, p=0.5, size=10)
# print(x)
# sns.distplot(x, hist=True, kde=False)
# plt.show()

#多项式分布

x = np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
# print(x)