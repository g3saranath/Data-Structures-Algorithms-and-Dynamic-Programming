import time
def Recursion_power(n):
    if n==0:
        return 1
    else: 
        power=Recursion_power(n-1)
        return power*2

x=Recursion_power(5)
print(x)

def iteration_power(n):
    power=1
    for i in range(0,n):
        power=power*2
    return power
y=iteration_power(5)
print(y)