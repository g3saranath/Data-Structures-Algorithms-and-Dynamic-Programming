def gcd(a,b):
    assert type(a)==int and type(b)==int, 'Both numbers should be integers'
    b=abs(b)
    a=abs(a)
    if b==0:
        return a
    else: 
        return gcd(b,a%b)

print(gcd(12,8))