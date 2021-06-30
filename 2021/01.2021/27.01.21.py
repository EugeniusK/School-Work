import datetime
import time
import random

def chal1():
    print('What\'s the best thing about Switzerland?') #prints first line of joke
    input() #waits until user presses something in terminal
    return 'I don\'t know, but the flag is a big plus.'

#print(chal1())
"""
What's the best thing about Switzerland?

I don't know, but the flag is a big plus.
"""
def chal2():
    print('What is your name?') 
    name = input() #gets name input from user
    return "Hello {}".format(name) #outputs Hello and the name variable together


#print(chal2())
"""
What is your name?
Eugene
Hello Eugene


What is your name?
Richard
Hello Richard
"""
def chal3():
    #get input as integers for the size of cuboid
    width = int(input('Width: '))
    height = int(input('Height: '))
    depth = int(input('Depth: '))
    return width*height*depth

#print(chal3())

"""
Width: 5
Height: 5
Depth: 5
125

Width: 7
Height: 8
Depth: 1
56
"""
def chal4():
    speed = int(input('Speed in m/s: '))
    time = int(input('Time in seconds: '))
    #d = st and s = d/t used
    return f'distance travelled = {speed*time}m. You would need to travel at {round(10000/time,2)} m/s to go 10km within {time} seconds'

#print(chal4())

"""
Speed in m/s: 5
Time in seconds: 10
distance travelled = 50m. You would need to travel at 1000.0 m/s to go 10km within 10 seconds

Speed in m/s: 1000000
Time in seconds: 1
distance travelled = 1000000m. You would need to travel at 10000.0 m/s to go 10km within 1 seconds
"""

def chal5():    
    birthday = datetime.datetime.strptime(input('What did ur date of birth in dd/mm/yyyy? '),'%d/%m/%Y')
    time_now = datetime.datetime.now()
    if time_now.year-birthday.year > 18:
        return 'You can vote'
    elif time_now.year-birthday.year == 18: #checks if the year dif == 18 and whether or not month and day are before or after the actual birthday
        if time_now.month-birthday.month > 0:
            return 'You can vote'
        else:
            if time_now.day-birthday.day >= 0:
                return 'You can vote'
            else:
                return 'You cannot vote'
    else:
        return 'You cannot vote'

#print(chal5())
"""
What did ur date of birth in dd/mm/yyyy? 27/01/2003 (18 years before test)
You can vote

What did ur date of birth in dd/mm/yyyy? 28/01/2003 (1 day too young for vote)
You cannot vote
"""

def chal6():
    input('Hit the enter key when ready') 
    start = float(time.time()) #gets time passed after epoch
    input('Hit the enter key when you think time has passed')
    end = float(time.time()) #gets time passed after epoch again to find difference between start and end in seconds
    return f"You were {abs(10-round(end-start,4))} seconds away from 10 seconds" 

#print(chal6())

"""
Hit the enter key when ready
Hit the enter key when you think time has passed
You were 6.662100000000001 seconds away from 10 seconds (don't know what happened with the rounding)

Hit the enter key when ready
Hit the enter key when you think time has passed
You were 9.3127 seconds away from 10 seconds
"""

def chal7():
    input('Hit the enter key when ready')
    start = float(time.time())
    attempt = input('Type the alphabet in lowercase as fast as you can ')
    end = float(time.time())
    if attempt == 'abcdefghijklmnopqrstuvwxyz':
        return f'You took {round(end-start,4)} seconds to type the whole alphabet'
    else:
        return 'You failed'

#print(chal7())

"""
Hit the enter key when ready
Type the alphabet in lowercase as fast as you can abcdefghijklmnopqrstuvwxyz
You took 5.448 seconds to type the whole alphabet

Hit the enter key when ready
Type the alphabet in lowercase as fast as you can abcdefghijklmnopqrstuvwxyz
You took 3.9605 seconds to type the whole alphabet

Hit the enter key when ready
Type the alphabet in lowercase as fast as you can asdsa
You failed
"""
def chal9():
    user_input = ''
    print('Type break to break')
    while user_input != 'break': #while the user hasn't inputed break
        print(random.randint(1,4),random.randint(1,13))
        user_input = input()
    return ''
#print(chal9())
"""
Type break to break
3 2

2 12

2 13

4 8
break
"""
def chal10():
    print('rock = 1 paper = 2 scissors = 3')
    moves = ['rock','paper','scissors']
    computer = random.randint(1,3)
    user = int(input('Your move: '))
    if user == computer:
        return f'draw computer chose {moves[computer-1]}'
    elif user%3 > computer%3:
        return f'you win computer chose {moves[computer-1]}'
    else:
        return f'you lose computer chose {moves[computer-1]}'

#print(chal10())
"""
rock = 1 paper = 2 scissors = 3
Your move: 1
you win computer chose scissors

rock = 1 paper = 2 scissors = 3
Your move: 1
draw computer chose rock
"""

def chal11():
    logic = input('Enter logic gate (choose from OR, AND, XOR, NAND and NOR): ')
    a = int(input('Enter first input: '))
    b = int(input('Enter second input: '))
    if logic == 'OR':
        return int(a or b)
    elif logic == 'AND':
        return int(a and b)
    elif logic == 'XOR':
        return int(a != b) #XOR is same as !=
    elif logic == 'NAND':
        return int(not(a and b))
    elif logic == 'NOR':
        return int(not(a or b))

#print(chal11())
"""
Enter logic gate (choose from OR, AND, XOR, NAND and NOR): OR
Enter first input: 1
Enter second input: 0
1

Enter logic gate (choose from OR, AND, XOR, NAND and NOR): XOR 
Enter first input: 1
Enter second input: 0
1
"""
def chal12():
    number = int(input('Enter number: '))
    factors = []
    for i in range(1,int(number**0.5)+1): #only need to check upto the root of the number
        if number % i == 0:
            factors.extend([i,int(number/i)]) #add n/x and x at the same time to reduce time
    if len(factors) == 2:
        print('Prime')
    return sorted(list(set(factors))) #set removes repeated terms incase it's a square number

#print(chal12())
"""
Enter number: 1457753454
[1, 2, 3, 6, 9, 18, 19, 37, 38, 57, 74, 111, 114, 171, 222, 333, 342, 666, 703, 1406, 2109, 4218, 6327, 12654, 115201, 230402, 345603, 691206, 1036809, 2073618, 2188819, 4262437, 4377638, 6566457, 8524874, 12787311, 13132914, 19699371, 25574622, 38361933, 39398742, 76723866, 80986303, 161972606, 242958909, 485917818, 728876727, 1457753454]

Enter number: 5
Prime
[1, 5]
"""
def chal25():
    user_input = ''
    dealt_cards = []
    while len(dealt_cards) != 52:
        suit = random.randint(1,4)
        card = random.randint(1,13)
        while (suit,card) in dealt_cards: #while the card has already been generated, generate a new one
            suit = random.randint(1,4)
            card = random.randint(1,13)
        print(suit,card)
        dealt_cards.append((suit,card)) #add a tuple of suit and card
        user_input = input() #wait for user to press enter
    return 'No more cards'

print(chal25())

"""
1 8

1 12

1 5

3 5

1 13

4 5

3 4

1 7

4 9

4 10

1 6

4 4

3 7

3 6

4 7

2 1

4 8

3 1

2 5

1 4

1 10

3 12

3 2

1 2

2 9

2 13

2 10

3 9

2 7

2 8

1 9

2 2

4 1

2 3

4 3

4 2

2 6

2 11

4 12

1 3

3 10

4 13

2 4

1 1

3 11

1 11

3 8

3 3

4 11

4 6

2 12

3 13

No more cards
"""
