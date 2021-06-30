"""
function practice and string building and converting between datatypes
16.9.20
"""

def add(a,b,c):
    return(float(a+b+c))

def subtract(a,b):
    return(int(b-a))

def tax(income,taxrate):
    return(round((income*taxrate),2))

def longDiv(denom,numer):
    return(str(denom)+" divided by "+str(numer)+" is "+str(denom//numer)+" with a remainder of "+str(denom%numer))

def powpow(a,b):
    return(str(a**b)+" and "+str(b**a))

print(add(1,2,3))
print(subtract(1.0,5.0))
print(tax(100,0.06523))
print(longDiv(5,2))
print(powpow(2,5))


