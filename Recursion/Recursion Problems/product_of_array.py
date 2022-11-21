def ArrayProduct(arr):
    if len(arr)==0:
        return 1
    else: 
        return arr[0]*ArrayProduct(arr[1:])

print(ArrayProduct([1,2,3,2,5]))