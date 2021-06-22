import random
#Task 1 
"""
total = 0
while True:
    print('Enter next sales value')
    sales = input()
    total += float(sales)
    if sales == '0':
        break
print('Total =',total)
"""
#task 2
"""score = 0
while True:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1 == die2:
        score = 0
    else:
        score += (die1 + die2)
        print('score =', score)

    if input('press y for anothetr go') != 'y':
        break
print('score=', score)"""

#task 3

"""wounds = 0
gremlins = 4
strength = 30
while strength > 0:
    if gremlins >= 1:
        wounds += gremlins
    if strength > 2:
        gremlins -= 1
        print('mighty Max has dealth a deathly blow to a gremlin, but his stregnth is fading')
    strength -= wounds
    print(f'wounds = {wounds} gremlins = {gremlins} strength = {strength}')

print('Alas, our hero has been overcome... Game Over')"""

#task 4

print("How many grains of wheat will be on each square?")
powerOf2 = 1
total = 1
for n in range(2,7):
    powerOf2 *= 2
    total += powerOf2
    print(f'You have a total of {total} grains on squares 1 to {n}')
    