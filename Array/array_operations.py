from array import *

#1. Creating an Array and Traverse

arr=array('i',[1,2,3,4,5])

print('Traverseral O(N) :')
for i in arr:
    print(i)

print('\n')

#2. Accessing elements through indexes

print('Accessing Element - O(1) : Index: 2')
print(arr[2])
print('\n')

#3. Append value to an array using "append()" method

print('Append method - O(1):')
arr.append(6)
print(arr)
print('\n')

#4. Insert value using insert() method
print('Insert value to array')
arr.insert(3,0)
print(arr)
print('\n')


#5. Using extend() method
print('Extending the array')
arr2=array('i',[10,11,12])
arr.extend(arr2)
print(arr)
print('\n')

#6. Add elements from list using fromlist() method
lis=[20,21,22]
arr.fromlist(lis)
print(arr)
print('\n')

#7. Remove any element from an array
print('Remove element')
arr.remove(21) #Removes only one/first value found
print(arr)
print('\n')

#8. Remove last element using pop O(1)
print('Pop')
arr.pop()
print(arr)
print('\n')

#9. Index method
print('Index')
print(arr.index(20))
print('\n')

#10. Reverse method
print('Reversing :')
arr.reverse()
print(arr)
print('\n')

#11. Getting buffer information using buffer_info() method
print('Buffer Information')
print(arr.buffer_info())
print('\n')

#12. Number of occurances of elements using count() method
print('Count of 1')
arr.append(1)
print(arr.count(1))
print('\n')

#13. Convert array to string using tostring() method
print(arr.tostring())