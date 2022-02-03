from random import randint, choices

symbols = ['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull']
money = 1

quit = False
while not(quit):
    sample = choices(symbols, k=3)
    money -= 0.2
    if len(set(sample)) == 2:
        money += 0.5
    elif len(set(sample)) == 1:
        f 
