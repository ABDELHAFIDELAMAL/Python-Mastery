from xmlrpc.client import boolean

import numpy as np

arr = np.arange(1, 10).reshape((3, 3))
print(arr)

print("=" * 20)
arr1 = np.full((3, 3), 4)
print(arr1)
arr2 = arr1.tolist()
print(arr2)
print("=" * 20)
arrr = np.trace(arr2)
print(arrr)
print("=" * 20)

a = np.sum(np.diagonal(arr2))
print(a)

print("=" * 20)
# Pandas
