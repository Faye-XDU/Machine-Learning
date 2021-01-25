import numpy as np

#创建数组

arr = np.array([1, 2, 3, 4, 5])
# for a in arr:
#     print(a)
my_matrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
mtrx = np.array(my_matrix)

#索引和切片

# print(mtrx[1, 1], arr[:3])

#dtype

arr2 = np.array(['asdfwerf', 'b', 'c'])
arr1 = np.array(['1', '2', '3'], dtype= 'f')

print(arr2.dtype, arr1.dtype)

#一般方法

arr3 = np.arange(0, 101, 2)
# print(arr3)
np.zeros((2, 5))
np.ones((4,4))
np.eye(5)
np.random.seed(99)
arr4 = np.random.rand(5,2)
# print(arr4)
arr5 = np.random.randint(0, 101, (4,5))
print(arr5)
print(arr5.max(),arr5.min())