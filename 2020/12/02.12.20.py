"""
While loops
"""

def next10(integer):
    i = integer
    integer_list = []
    while i  < integer + 10:
        integer_list.append(i)
        i += 1
    return integer_list
print(next10(0))
print(next10(10))
print(next10(-10))
print(next10(5))

def previous20(integer):
    i = integer
    integer_list = []
    while i  > integer - 40:
        integer_list.append(i)
        i -= 2
    return integer_list
print(previous20(0))
print(previous20(10))
print(previous20(-10))
print(previous20(5))

def sumSome(array):
    i,total = 0,0
    while i < len(array) and array[i] >= 0:       
        total += array[i]
        i += 1
    return total
print(sumSome([0,1,2,3,4,5]))
print(sumSome([1,2,-3,4,5]))
print(sumSome([-1,0,1,2,3,4]))
print(sumSome([1,2,3,50,100,-150]))

def findIt(array,integer):
    i = 0
    while i < len(array):
        if array[i] == integer:
            return f'I found it at index {i+1}'
        i += 1
    return 'I couldn\'t find it'
print(findIt([1,2,3,4,5],5))
print(findIt([1,2,3,4,5],1))
print(findIt([1,2,3,4,5],6))
print(findIt([1,2,2,3,4],2))
    
def removeSome(array,word):
    i, return_array = 0,[]
    while i < len(array) and array[i] != word:   
        return_array.append(array[i])
        i += 1
    return return_array
print(removeSome(["waffle","stolen","by","Hugo","?"],"by"))
print(removeSome(["waffle","stolen","by","Hugo","?"],"Michael"))
print(removeSome(["waffle","stolen","by","Hugo","?"],"stolen"))
print(removeSome(["waffle","stolen","by","Hugo","?"],"waffle"))

def howMany(array):
    i, count = 0, 0
    while i < len(array) and array[i] % 2 == array[0] % 2:     
        count += 1
        i += 1
    if array[0] % 2 == 0:
        return f"The first {count} numbers in the array were even"
    else:
        return f"The first {count} numbers in the array were odd"
print(howMany([1,3,5,6,7,9]))
print(howMany([2,2,3,4,5,6]))
print(howMany([1,1,1,1,1,1]))
print(howMany([1,2,2,2,2,2]))
print(howMany([2,2,2,2,2,2]))

def fibbo(integer):
    a, b, fib, i = 0, 1, [0,1], 0
    while fib[-1] <= integer:
        fib.append(a+b)
        a = b
        b = fib[-1]
    fib.pop(-1)
    return fib
print(fibbo(10))
print(fibbo(1))
print(fibbo(20))
print(fibbo(100))
    
def charityLoser(array, limit):
    total = 0
    reject = 0
    i = 0
    while total <= limit and i < len(array):
        if total + array[i] > limit:
            reject += array[i]
        else:
            total += array[i]
        i += 1
    return f"{total} Yen of donations was accepted, {reject} Yen of donations was rejected"
print(charityLoser([10.1,100.5,50.0,60.9],10))
print(charityLoser([10.1,100.5,50.0,60.9],20))
print(charityLoser([10.1,100.5,50.0,60.9],150))
print(charityLoser([10.1,100.5,50.0,60.9],200))

def passwordChecker():
    attempts = 0
    password = 'waffle'
    authenticated = False
    while attempts <= 2 and not(authenticated):
        value = input('Password: ')
        if value == password:
            authenticated = True
        attempts += 1

    if authenticated == False and attempts >= 3:
        return 'Access denied'
    else:
        return 'Access granted'

print(passwordChecker())



