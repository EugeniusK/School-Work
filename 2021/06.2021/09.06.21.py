import random
score = 0
flag = True
while flag:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1 == die2:
        score = 0
    else:
        score += (die1 + die2)
        print(f"Your current score is {score}")
    if input('Another go? ') not in ['yes', 'Yes', 'Y', 'y', 'true', 'True', '1']:
        flag = False
print(f"You finished with a score of {score}")