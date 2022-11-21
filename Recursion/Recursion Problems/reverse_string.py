#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.



def reverse(strng):
    if len(strng)==1:
        return strng[0]
    else:
        return strng[len(strng)-1]+reverse(strng[:len(strng)-1])

print(reverse(strng='hello world'))