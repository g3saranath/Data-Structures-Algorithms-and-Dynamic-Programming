def Factorial(n):
    assert n>=0 and int(n)==n,'Number should be positive and integer'
    if n==0 or n==1:
        return 1
    else: 
        return n*Factorial(n-1)
        

print(Factorial(5))
print(Factorial(-1.2))