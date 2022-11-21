def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someodd(arr, cb):
    if len(arr)==0:
        return False
    elif cb(arr[0])==True:
        return True
    return someodd(arr[1:],cb)

print(someodd([1,2,3,4,5],isOdd))
print(someodd([2,4,6,8],isOdd))