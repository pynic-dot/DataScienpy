import numpy as np
# print(np.__version__)
# print("HelloWorld")


#Creating numpy ndarray Objects

arr = np.array([[1,3,4,5,6],[4,5,6,7,8]])
# print(arr)
# # print(type(arr)) # type function shows the type of array
# # print(arr.ndim) # ndim shows the number of dimension array have
# arr1 = np.array([1,3,4], ndmin= 8)
# print(arr1)
# print(arr1.ndim)

# print(arr[1,2])

x = arr.copy()

arr[1]= 12

y = x.view()

y[0] = 10
# print(x)
# print(y)
# print(arr.base)
# print(y.base)
# print(x.base)
# print(arr.shape)

z = np.array([1,2],ndmin = 6)

arr2 = np.array([1,2,3,4,5,6,7,8,9],ndmin=2)
# print(arr2.reshape(-1,3))
# for x in arr2:
# # print(x)
# for x in arr2:
#     for y in x:
#         for x in y:
#             print(x)

# for x in np.nditer(arr2):
    # print(x)
# for x in np.nditer(arr2,flags=['buffered'],op_dtypes=['char']):
    # print(x)
for indx ,x in np.ndenumerate(arr2):
    print(indx,"->",x)