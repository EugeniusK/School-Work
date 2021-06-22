"""
arrays and lists worksheet
"""

def integersTolist(a,b,c,d):
    return [a,b,c,d]

print(integersTolist(1,2,3,4))

def addValueToList(array, value):
    array.append(value)
    return array

print(addValueToList([1,2],5))

def addValueAtIndex1(array,value,index):
    if index < len(array):
        array.insert(index,value)
        return array
    else:
        return "Invalid index"

print(addValueAtIndex1([1,2,3,4,5],5,7))
print(addValueAtIndex1([1,2,3,4,5],6,5))

def addValueAtIndex2(array,value,index):
    if index <= len(array):
        array.insert(index,value)
        return array
    else:
        return "Invalid index"

print(addValueAtIndex2([1,2,3,4,5],5,7))
print(addValueAtIndex2([1,2,3,4,5],6,5))

def wordOccurences(string,word):
    return f"The word {word} appeared {string.count(word)} number of times in the given string"

print(wordOccurences("Hello Michael","e"))

def sortWords(string):
    return sorted(string.split(),key = lambda string : string[0].lower())

print(sortWords("Hello Michael this is a test"))

def reverseString(string):
    return string[::-1]

print(reverseString("Hello"))

def findReplace(array,value):
    return f"The value {value} was found at index {array.index(value)}. Here is the new array {[x for x in array if x != value]}"

print(findReplace([1,2,3,4,5],5))

def wafflesStolen(array):
   return f"The fewest waffles stolen in a day was {min(array)}, and the most waffles stolen in a single day was {max(array)}."
 
print(wafflesStolen([1,3,2,4,5,6,7]))



def wafflesStolenAverage(array):
    return f"The average number of waffles stolen per day was {int(sum(array)/len(array))}."

print(wafflesStolenAverage([1,3,2,4,5,6,7]))

def sumAverage(array0,array1):
    return f"The sum of the two arrays combined is {sum(array0+array1)} and the average of array 1 is {sum(array0)/len(array0)} and the average of array 2 is {sum(array1)/len(array1)}"

print(sumAverage([1,2,3,4],[2,4,5,6]))

