def Fibonacci(n):
    assert n>=0 and type(n)==int, 'Please provied appropriate input - positive number and integer'
    if n==1 or n==0:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(4))