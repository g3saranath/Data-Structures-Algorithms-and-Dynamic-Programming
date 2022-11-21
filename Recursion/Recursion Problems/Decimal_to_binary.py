def Decimal2Binary(n):
    if n==1 or n==0:
        return n
    else:
        print(n//2)
        return n%2+Decimal2Binary(n//2)*10

print(Decimal2Binary(15))