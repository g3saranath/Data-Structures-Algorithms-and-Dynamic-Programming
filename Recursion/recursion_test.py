def Recursion(n):
    if n<1:
        print('n is less than 1')
    else:
        Recursion(n-1)
        print(n)
    
Recursion(5) 
'''
Output:

n is less than 1
1
2
3
4
5
'''