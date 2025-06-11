import turtle
win = turtle.Screen()
win.bgcolor("blue")
turtle.title("Country")

t = turtle.Turtle()
t.shape("turtle")
t.pu()
t.goto(-400,300)
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
t.goto(-100,0)
t.pd()
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.circle(100)
t.end_fill()
t.pu()
t.goto(400,0)




turtle.done()
