from array import *


def find_missing(n):
    arr=array('i',range(1,n+1))
    arr.pop(45)
    print(arr)
    print('Missing Number: ',n*(n+1)/2-sum(arr))
    
find_missing(100)