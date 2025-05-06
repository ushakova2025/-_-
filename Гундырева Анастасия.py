from turtle import*

def draw_orange():
    pensize(12)
    down()
    color('orange')
    left(60)
    fd(230)
    left(30)
    circle(50,180)
    left(30)
    fd(230)

def draw_black():
    pensize(12)
    down()
    color('black')
    left(60)
    fd(230)
    left(30)
    circle(50,180)
    left(30)
    fd(230)

def petal():
    pensize(8)
    down()
    color('red')
    fd(70)
    left(30)
    circle(30,180)
    left(30)
    fd(70)

for i in range(1,6):
    if i%2==0:
        draw_orange()
        up()
        right(30)
        fd(12)
        right(90)
        fd(130)
        right(180)
    else:
        draw_black()
        up()
        right(30)
        fd(12)
        right(90)
        fd(130)
        right(180)


up()
pensize(5)
fd(65)
left(90)
pensize(8)
color('green')
down()
fd(252)
up()
fd(64)
down()
fd(40)
left(90)
up()
fd(20)
down()
left(180)
for i in range(5):
    petal()
    left(90)
    left(60)

