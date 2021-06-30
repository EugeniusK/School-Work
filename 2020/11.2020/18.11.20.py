"""
Iteration
"""
import math
def print10(integer):
    return list(range(integer,integer+10))

print(print10(9))


def down10(integer):
    return list(range(integer,integer-20,-2))
        
print(down10(20))

def sumUp(array):
    total = 0
    for i in array:
        total += i
    return total

print(sumUp([1,2,4,5,6]))

def removal(array,words):
    return [x for x in array if x != words]

print(removal(["Hello", "Michael", ".", "Michael", "is", "a", "gamer"],"Michael"))

def insertOften(array,insert,stepping):
    for i in range(stepping,stepping*len(array) // stepping,stepping):
        array.insert(i+int(i/stepping)-1,insert)
        
    return array

print(insertOften([1,2,3,4,5,6,7,8,9,10,11],0,3))


def gooseFilter(array):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return [x for x in array if x in geese]

print(gooseFilter(["Pilgrim","Michael"]))

def starTree(int):
    if int % 2 == 0:
        return "Your star tree would be invalid, try again"
    else:
        return "".join(["*"*x+"\n" for x in range(1,int)]+["*"*int])

print(starTree(5))

def howMany(array):
    if array[0] % 2 == 0:
        return f"There were {len([x for x in array if x % 2 == 0])} even numbers in the array"
    else:
        return f"There were {len([x for x in array if x % 2 == 1])} odd numbers in the array"

print(howMany([2,2,3]))

def fizzBuzz(integer):
    return ['FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(1,integer+1)]
print(fizzBuzz(16))

def binToDec(binary):
    if list(str(binary)).count('0') + list(str(binary)).count('1') == len(str(binary)):
        return sum([int(str(binary)[::-1][x])*(2**x) for x in range(len(str(binary)))])
    else:
        return "Invalid binary number"

print(binToDec(101011))
def decToBec(dec): #Why is Binary abbreviated to Bec?
    if dec == int(dec) and dec >= 0:
        power = int(math.log(dec,2))
        binary = []
        for i in range(power,-1,-1):
            if 2**i <= dec:
                dec -= 2**i
                binary.append('1')
            else:
                binary.append('0')
        return "".join(binary)
    else:
        return "Invalid decimal number"

print(decToBec(1234565321))


print("tests")
print(" ")
print(" ")
print(" ")
print("print10")
print(print10(10))
#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(print10(1))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(print10(0))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(print10(-10))
#[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
print("down10")
print(down10(0))
#[0, -2, -4, -6, -8, -10, -12, -14, -16, -18]
print(down10(20))
#[20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
print(down10(10))
#[10, 8, 6, 4, 2, 0, -2, -4, -6, -8]
print(down10(-10))
#[-10, -12, -14, -16, -18, -20, -22, -24, -26, -28]
print("sumUp")
print(sumUp([1,2,3,4,5,6,7,8,9,10]))
#55
print(sumUp([-1,-2,-3]))
#-6
print(sumUp([8, 13, 28, 38, 40, 49, 50, 72, 101, 105, 118, 170, 181, 192, 211, 221, 230, 233, 238, 242, 253, 259, 266, 271, 272, 284, 286, 291, 308, 310, 313, 315, 323, 324, 342, 345, 358, 368, 381, 392, 394, 424, 427, 444, 466, 481, 492, 493, 507, 511, 514, 517, 519, 537, 542, 559, 565, 622, 625, 632, 634, 640, 663, 668, 673, 693, 697, 699, 713, 722, 742, 749, 752, 758, 763, 767, 775, 778, 779, 791, 792, 804, 805, 811, 820, 825, 844, 868, 902, 911, 915, 927, 934, 936, 937, 972, 977, 978, 993, 994]))
#51473
print("removal")
print(removal(["The", "sun", "is", "shining", "all", "the", "day", "long"],"the"))
#['The', 'sun', 'is', 'shining', 'all', 'day', 'long']
print(removal(["one","two","one","two"],"one"))
#['two', 'two']
print(removal(["Who","stole","all","waffles","?"],"Michael"))
#['Who', 'stole', 'all', 'waffles', '?']
print("insertOften")
print(insertOften([1,1,1,1,1],2,1))
#[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(insertOften([1,1,1,1,1],2,2))
#[1, 1, 2, 1, 1, 2, 1]
print(insertOften([1,1,1,1,1],2,3))
#[1, 1, 1, 2, 1, 1]
print(insertOften([1,1,1,1,1,1,1,1,1,1],2,4))
#[1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1]
print("gooseFiter")
print(gooseFilter(["Robin","Swallow","African","Thrush"]))
#['Swallow', 'African']
print(gooseFilter(["Toulouse","Pilgrim","Steinbacher","Steinbacher"]))
#['Toulouse', 'Pilgrim', 'Steinbacher', 'Steinbacher']
print(gooseFilter(["Toulouse","Swallow","african","African"]))
#['Toulouse', 'african', 'African']
print(gooseFilter(["Robin","Swallow","European","Thrush"]))
#['Swallow', 'Thrush']
print("starTree")
print(starTree(3))
print(starTree(5))
print(starTree(4))
print(starTree(7))
print("howMany")
print(howMany([1,2,3,4,5,6]))
#There were 3 odd numbers in the array.
print(howMany([2,2,3,4,5,6]))
#There were 4 even numbers in the array.
print(howMany([1,1,1,1,1,1]))
#There were 6 odd numbers in the array. 
print(howMany([1,2,2,2,2,2]))
#There were 1 odd numbers in the array.
print("fizzBuzz")
print(fizzBuzz(3))
#[1, 2, 'Fizz']
print(fizzBuzz(5))
#[1, 2, 'Fizz', 4, 'Buzz']
print(fizzBuzz(30))
#[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz']
print(fizzBuzz(15))
#[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
print("bintoDec")
print(binToDec("10000"))
#16
print(binToDec("1111"))
#15
print(binToDec("10101010"))
#170
print(binToDec("111111111"))
#511
print(binToDec("101010102"))
#Invalid binary number
print('decToBec')
print(decToBec(-1))
#Invalid decimal number
print(decToBec(10.1))
#Invalid decimal number
print(decToBec(7))
#111
print(decToBec(32))
#100000
print(decToBec(127))
#1111111
print(decToBec(65592))
#10000000000111000
