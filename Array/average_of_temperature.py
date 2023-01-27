from array import *

n=int(input('Enter number of days?: '))

arr=array('d',[])

for i in range(n):
    arr.append(float(input(f'Day {i} temperature: ')))

print("Average :",sum(arr)/n)
print(f"{len([i for i in arr if i>sum(arr)/n])} days above average")