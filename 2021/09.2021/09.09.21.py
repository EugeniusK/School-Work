import turtle, math, random
t = turtle.Turtle()
t.speed(0)
coords = []

def check_collision(x,y, size):
    collide = [True if abs((x**2-coord[0]**2) + (y**2-coord[1]**2))**0.5 < size else False for coord in coords]
    return True in collide

check_collision(5,6, 10)

def random_color():
    color = random.randint(128*1*1, 128*256*256)
    hex_color = hex(color)
    str_hex_color = f'#{(6-len(str(hex_color)[2:]))*"0"}{str(hex_color)[2:]}'
    return str_hex_color


turtle.screensize(400,400)
for i in range(10):        
    t.begin_fill()
    t.fillcolor(random_color())
    t.penup()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    n = random.randint(1,20)
    l = random.randint(5,20)
    r = random.randint(1,15)
    if len(coords) == 0:
        coords.append(x,y)
    else:
        if check_collision(x,y,l):

    t.setpos(random.randint(-200,200), random.randint(-200,200))
    t.pendown()
    for i in range(r):
        t.left(360/r)
        for i in range(n):
            t.forward(l)
            t.right(360/n)
    t.end_fill()
