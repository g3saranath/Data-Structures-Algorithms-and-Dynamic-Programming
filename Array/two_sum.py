def two_sum(arr,target):

    for i in range(len(arr)):
        if target-arr[i] in arr[i+1:]:
            return (i,arr[i+1:].index(target-arr[i])+i+1)
    return 'Cannot find a pair'

array=[3,3,2,4]
target=6

print(two_sum(array,target))