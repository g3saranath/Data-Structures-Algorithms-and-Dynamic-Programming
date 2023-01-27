from array import *

arr=array('i',[3,4,5,6,7,2,3,5,43,46,22,78,56,93,34])

prod=1

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if prod<arr[i]*arr[j]:
            prod=arr[i]*arr[j]
            integers=(arr[i],arr[j])
print(prod)
print(integers)