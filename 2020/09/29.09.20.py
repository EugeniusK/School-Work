"""
Basic strings and output
"""

def first_letter(string):
    return(string[0])

def last_letter(string):
    return(string[-1])

def length_string(string):
    return(len(string))

def middle_letter(string):
    return(string[int(len(string)/2)])

def first_word(string):
    return(string[:(string.find(" "))])

def first_instance(string,word):
    return(string.find(word))

def madlib(word1,word2,word3):
    return(f"Mr {word1} doesn't {word2} a {word3}")

def replace_char(string,char1,char2):
    string = string.replace(char1,char2)
    return(string)
        
print(first_letter("Hello"))

print(last_letter("Hello"))

print(length_string("Hello"))

print(middle_letter("Hello"))

print(first_word("Hello There"))

print(first_instance("Hello There","Hello"))

print(madlib("egg","salad","sandwich"))

print(replace_char("hello","e","k"))

"""
num_list = []
greatest_product = [0,0]
for i in range(10,999999):
    #print((i/1000)**(18/(i/1000)))
    if ((i/100000)**(18/(i/100000))) > greatest_product[0]:
        greatest_product[0] = ((i/100000)**(18/(i/100000)))
        greatest_product[1] = (i/100000)

print(greatest_product)

    