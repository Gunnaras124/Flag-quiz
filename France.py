import turtle
win = turtle.Screen()
win.bgcolor("green")
turtle.title("Country")

t = turtle.Turtle()
t.shape("turtle")
t.pu()
t.goto(-400,300)
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
t.goto(100,100)




turtle.done()
