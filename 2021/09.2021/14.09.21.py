import turtle, random
t = turtle.Turtle()
t.speed(0)


'''t.begin_fill()
t.fillcolor('green')
for n in range(10):
    color = ['red', 'blue', 'green']
    t.begin_fill()
    if n == 9:
        t.fillcolor(color[2])
    elif n % 2 == 0:
        t.fillcolor(color[0])
    else:
        t.fillcolor(color[1])
    for i in range(10):
        t.forward(50)
        t.right(36)
    t.right(36)
    t.end_fill()'''


'''def random_color():
    color = random.randint(0, 255*255*256)
    hex_color = hex(color)
    str_hex_color = f'#{(6-len(str(hex_color)[2:]))*"0"}{str(hex_color)[2:]}'
    return str_hex_color

for i in range(100):
    t.begin_fill()
    t.fillcolor(random_color())
    t.left(random.randint(0,90))
    t.forward(50)
    n = random.randint(1,20)
    l = random.randint(30,90)
    for i in range(n):
        t.forward(l)
        t.right(360/n)
    t.end_fill()'''

'''for i in range(4):
    t.forward(10)
    t.left(90)'''

t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.color('green')
t.forward(40)
t.backward(40)
t.setpos(0,30)
t.setpos(0,30)
t.setpos(0,30)
t.setpos(0,30)
t.setpos(0,30)
t.setpos(0,30)
t.setpos(0,30)

input()