import numpy as np

arr = np.full((3,4),5)
arr1 = np.arange(0,10,2)
print(arr)


import numpy as np
print(np.__version__)

ones = np.ones(5)  # مصفوفة كلها رقم 1

zeros = np.zeros((3,3)) # مصفوفة 3*3 كلها أصفار
ranges = np.arange(10)  # مصفوفة من 0 إلى 9

print(ones)
print(zeros)
print(ranges)
# create Array
A = np.array([ [ [ 3 , 4] , [ 1 , 2]] , [ [ 1, 2 ] , [ 3, 4]] ])
A[0 , 0 , 1] = 2
print(A[0,0,1])
# Number of dimontion
print(A.ndim)


