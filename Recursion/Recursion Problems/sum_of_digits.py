def sum_of_digits(n):
    assert n>=0 and type(n)==int,'Enter valid input'
    if n==0:
        return 0
    else:
        return int(n%10)+sum_of_digits(n//10)

print(sum_of_digits(3255))