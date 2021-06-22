"""
function practice
8.9.20
"""
def mult10(integer):
    return(integer*10)

def intDiv(denom,numer):
    return(denom//numer)


def besties(name1,name2):
    return(name1+" and "+name2+" are best friends")


def dailyAdvice(sentence,number):
    return(sentence+" "+str(number)+" times")


def addNums(number1,number2):
    return(number1+number2)


def subNums(number1,number2,number3):
    return(addNums(number1,number2)-number3)


print(mult10(99))

print(intDiv(5,2))

print(besties("Nina","Risa"))

print(dailyAdvice("Brush your teeth",2))

print(subNums(5,6,1))
