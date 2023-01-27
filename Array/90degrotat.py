from array import *
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
new_array=np.zeros((3,3))

for i in range(len(arr)):
    for j in range(len(arr[0])):
        new_array[j][len(arr[0])-1-i]=arr[i][j]

print(new_array)

