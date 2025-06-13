import random
import turtle
win = turtle.Screen()
win.bgcolor("orange")
turtle.title("Country")
t=turtle.Turtle()

def germany():
    t.shape("turtle")

    t.pu()
    t.goto(-400, 200)
    t.pd()

    t.color("black")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

    t.rt(90)
    t.fd(120)
    t.lt(90)

    t.color("red")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

    t.rt(90)
    t.fd(120)
    t.lt(90)

    t.color("yellow")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

def austria():
    t.shape("turtle")

    t.pu()
    t.goto(-400,200)
    t.pd()

    t.color("red")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

    t.rt(90)
    t.fd(120)
    t.lt(90)

    t.color("white")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

    t.rt(90)
    t.fd(120)
    t.lt(90)

    t.color("red")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

def belgium():
    t.shape("turtle")
    t.pu()
    t.goto(-400, 300)
    t.pd()
    t.color("black")
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.rt(90)
        t.fd(400)
        t.rt(90)
    t.end_fill()
    t.fd(200)
    t.color("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.rt(90)
        t.fd(400)
        t.rt(90)
    t.end_fill()
    t.fd(200)
    t.color("red")
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.rt(90)
        t.fd(400)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(100, 100)

def france():
    t.shape("turtle")
    t.pu()
    t.goto(-400, 300)
    t.pd()
    t.color("blue")
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.rt(90)
        t.fd(400)
        t.rt(90)
    t.end_fill()
    t.fd(200)
    t.color("white")
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.rt(90)
        t.fd(400)
        t.rt(90)
    t.end_fill()
    t.fd(200)
    t.color("red")
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.rt(90)
        t.fd(400)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(100, 100)

def indonesia():
    t.shape("turtle")

    t.pu()
    t.goto(-400, 200)
    t.pd()

    t.color("red")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

    t.rt(90)
    t.fd(120)
    t.lt(90)

    t.color("white")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

def italy():
    t.shape("turtle")
    t.pu()
    t.goto(-400, 300)
    t.pd()
    t.color("green")
    t.fillcolor("green")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.rt(90)
        t.fd(400)
        t.rt(90)
    t.end_fill()
    t.fd(200)
    t.color("white")
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.rt(90)
        t.fd(400)
        t.rt(90)
    t.end_fill()
    t.fd(200)
    t.color("red")
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.fd(200)
        t.rt(90)
        t.fd(400)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(100, 100)

def japan():
    t.shape("turtle")
    t.pu()
    t.goto(-400, 300)
    t.pd()
    t.color("white")
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(600)
        t.rt(90)
        t.fd(400)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(-100, 0)
    t.pd()
    t.color("red")
    t.fillcolor("red")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.pu()
    t.goto(400, 0)


def luxembourg():
    t.shape("turtle")

    t.pu()
    t.goto(-400, 200)
    t.pd()

    t.color("red")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

    t.rt(90)
    t.fd(120)
    t.lt(90)

    t.color("white")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

    t.rt(90)
    t.fd(120)
    t.lt(90)

    t.color("#ADD8E6")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

def monaco():
    t.shape("turtle")

    t.pu()
    t.goto(-400, 200)
    t.pd()

    t.color("red")
    t.begin_fill()
    t.fd(400)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(400)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

    t.rt(90)
    t.fd(120)
    t.lt(90)

    t.color("white")
    t.begin_fill()
    t.fd(400)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(400)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()



def netherlands():
    t.shape("turtle")

    t.pu()
    t.goto(-400, 200)
    t.pd()

    t.color("red")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

    t.rt(90)
    t.fd(120)
    t.lt(90)

    t.color("white")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

    t.rt(90)
    t.fd(120)
    t.lt(90)

    t.color("blue")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

def poland():
    t.shape("turtle")

    t.pu()
    t.goto(-400, 200)
    t.pd()

    t.color("white")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

    t.rt(90)
    t.fd(120)
    t.lt(90)

    t.color("red")
    t.begin_fill()
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.fd(600)
    t.rt(90)
    t.fd(120)
    t.rt(90)
    t.end_fill()

guala=[austria,belgium,france,germany,indonesia,italy,japan,luxembourg,monaco,netherlands,poland]
lives=5
points=0

while len(guala) > 0:
    t.reset()
    t.speed(100)
    flag=random.choice(guala)
    flag()
    answer=input("Guess the flag:")
    if answer==flag.__name__:
        guala.remove(flag)
        points+=1
        print("You found it!")
    else:
        lives-=1
        print("You didn't find it")
    print("points:",points,"lives:",lives)
    if lives==0:
        t.reset()
        t.write("You lost",font=("Arial",30))
        break
    if points==11:
        t.reset()
        t.write("You won",font=("Arial",30))
turtle.done()