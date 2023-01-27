from array import *

arr=array('i',[2,3,4,5,6,7,8,9,19,20,12,3])
i=0
j=1
while(i<len(arr)-1 and j<len(arr)):
    if arr[i]^arr[j]==0:
        print(arr[i],' at ',i,' and ',arr[j],' at ',j,' is not unique')
    if j==len(arr)-1:
        i+=1
        j=i+1
    else:
        j+=1