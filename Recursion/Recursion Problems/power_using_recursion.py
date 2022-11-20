def power(base,n):
    assert type(base)==int and base>0, 'Use proper base and exponent'
    if n in [0]:
        return 1
    elif n<0:
        return (1/base)*power(base,n+1)
    return base*power(base,n-1)

print(power(3,-1))