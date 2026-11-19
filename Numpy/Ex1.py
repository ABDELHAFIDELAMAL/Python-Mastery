import numpy as np

tableau = np.array([[ 1,2,3] , [4,5,6]])
print(tableau)
print("Dem 1 : " , tableau.shape)

newTable = tableau.reshape(2,3)
print("Dem 2 : " , newTable.shape)

