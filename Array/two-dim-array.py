import numpy as np

arr=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]]) #O(1) if assigned directly, space complexity O(MN) 
print(arr[1][2:])

#Insertion of value in 2-D - have to insert a row or col, cannot insert single value
##1. Addition of col [3,6,9] to 0th index - O(N)
print('Insert Col')
new_arr=np.insert(arr,0,[[0,0,0,0]],axis=1) #Axis =1 col, =0 row, O(N)
print(new_arr)

##2. Addition of row [3,6,9] to 0th index - O(M)
print('Insert Row')
ew_arr=np.insert(arr,1,[[3,6,9,12]],axis=0)
print(ew_arr)

#Append function - col or row
print('Append')
new_arr=np.append(arr,[[1,1,1,1]],axis=0)
print(new_arr)

#Search element in 2-D array

def searchelement(array,target):

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==target:
                return (i,j)
    return 'Not found'

print(searchelement(arr,12))


arr_new=np.delete(arr,0,axis=0)
print(arr_new)