import random
import math

from numpy import character


def task_one():
    exit = False
    while not exit:
        choice = input('Choose a number from 4,6,12 or type exit to exit ')
        if choice in ['4', '6', '12']:
            print(
                f'{int(choice)} sided dice thrown, score {random.randint(1,int(choice))}')
        elif choice == 'quit':
            exit = True
        else:
            print('Invalid choice')
    return -1


class Character:
    def __init__(self):
        self.str = 10 + math.floor(random.randint(1, 12)/random.randint(1, 4))
        self.int = 10 + math.floor(random.randint(1, 12)/random.randint(1, 4))
        self.hp = 10 + math.floor(random.randint(1, 12)/random.randint(1, 4))
        self.skl = 10 + math.floor(random.randint(1, 12)/random.randint(1, 4))
        self.cha = 10 + math.floor(random.randint(1, 12)/random.randint(1, 4))
        self.end = 10 + math.floor(random.randint(1, 12)/random.randint(1, 4))
        self.agl = 10 + math.floor(random.randint(1, 12)/random.randint(1, 4))
        self.luc = 10 + math.floor(random.randint(1, 12)/random.randint(1, 4))
        self.dmg = 10 + math.floor(random.randint(1, 12)/random.randint(1, 4))
        self.shi = 10 + math.floor(random.randint(1, 12)/random.randint(1, 4))
        self.den = 10 + math.floor(random.randint(1, 12)/random.randint(1, 4))


character_one = Character()
character_two = Character()

one_data = vars(character_one)
two_data = vars(character_two)

one_data['name'] = 'nina'
two_data['name'] = 'richard'

with open('characters.txt', 'w') as f:
    f.write(str(one_data))
    f.write('\n')
    f.write(str(two_data))


def task_three():
    one_str = int(input('Strength of character one : '))
    two_str = int(input('Strength of character two : '))

    one_skl = int(input('Skill of character one : '))
    two_skl = int(input('Skill of character two : '))

    str_modifier = math.floor(abs(one_str - two_str) / 5)
    skl_modifier = math.floor(abs(one_str - two_str) / 5)

    one_dice = random.randint(1,6)
    two_dice = random.randint(1,6)
    if one_dice == two_dice:
        print('No change')
    else:
        if one_dice > two_dice:
            one_str += str_modifier
            one_skl += skl_modifier

            two_str -= str_modifier
            two_skl -= skl_modifier

        else:
            one_str -= str_modifier
            one_skl -= skl_modifier

            two_str += str_modifier
            two_skl += skl_modifier
    print(f'Strength of character one : {one_str}')
    print(f'Skill of character one : {one_skl}')
    print(f'Strength of character two : {two_str}')
    print(f'Skill of character two : {two_skl}')


task_three()