import random

#class of player with skill attribute
class Player:
    def __init__(self, name, skill, stamina):
        self.name = name.capitalize()
        self.skill = skill
        self.stamina = stamina

#returns sum of some dice
def dice_sum(num_dice, faces):
    total = 0
    for i in range(num_dice):
        total += random.randint(1,faces)
    return total

#returns an output with player starting scores and dice rolled
def report_round(player1, player2, skill1, skill2, roll1, roll2, result):
    output = f'{player1.name} rolled {roll1} and is now on {skill1}\n'
    output += f'{player2.name} rolled {roll2} and is now on {skill2}\n'
    output += f'{player1.name} {result} against {player2.name}'
    return output

#inputs 2 player objects and accesses their skill
#returns a message if the first player won or lost
def fight_round(player1, player2):
    skill_1 = player1.skill
    skill_2 = player2.skill
    roll_1 = dice_sum(2,6)
    roll_2 = dice_sum(2,6)
    skill_1 = player1.skill + roll_1
    skill_2 = player2.skill + roll_2
    if skill_1 == skill_2:
        result =  'drew'
        player1.stamina -= 1
        player2.stamina -= 1
    elif skill_1 > skill_2:
        result =  'won'
        player2.stamina -= 2
    else:
        result = 'lost'
        player1.stamina -= 2
    return report_round(player1, player2, skill_1, skill_2, roll_1, roll_2, result)

#inits 2 players with name, skill and stamina
Fighter = Player('fighter',7,100)
Monster = Player('monster',5,20)
God = Player('god',100000000,100000000)

#one round of a fight
def fight_battle(PlayerOne, PlayerTwo):
    while True:
        print(fight_round(PlayerOne, PlayerTwo))
        if PlayerOne.stamina > 0 and PlayerTwo.stamina > 0:
            print(f'{PlayerOne.name} is on {PlayerOne.stamina} stamina')
            print(f'{PlayerTwo.name} is on {PlayerTwo.stamina} stamina')
            print(f' ')
        else:
            if PlayerOne.stamina <= 0:
                print(f'{PlayerOne.name} has perished against {PlayerTwo.name}')
                print(f'{PlayerTwo.name} was on {PlayerTwo.stamina} stamina')
            elif PlayerTwo.stamina <= 0:
                print(f'{PlayerTwo.name} has perished against {PlayerOne.name}')
                print(f'{PlayerOne.name} was on {PlayerOne.stamina} stamina')
            else:
                print(f'{PlayerOne.name} and {PlayerTwo.name} managed to kill eachother')
            print('----------')
            print('Fight Over')
            print('----------')
            break

fight_battle(Fighter, Monster)
monster_name = ['Richard', 'Joe', 'Nina', 'Gus', 'Yutaka', 'Keith', 'Vladimir', 'Hank', 'Bartholomew']
potion_found = 0
monsters_fought = 0
while Fighter.stamina > 0:
    opponent = Player(monster_name[random.randint(0,len(monster_name))-1], 2, random.randint(20,50))
    fight_battle(Fighter, opponent)
    monsters_fought += 1
    if random.randint(1,10) < 5 and Fighter.stamina > 0:
        potion = random.randint(1,5)
        Fighter.stamina += potion
        print(f'{Fighter.name} found a potion that boosted their stamina by {potion}')
        print(f'{Fighter.name} is now on {Fighter.stamina} stamina')
        potion_found += 1
        
else:
    print(f'{Fighter.name} found {potion_found} potions and fought {monsters_fought} monsters until they died')
    print('---------')
    print('Game Over')
    print('---------')