import turtle
# This is first program this kinda succ
s = turtle.Screen()
s.setup(width=1000,height=1000)
turtle.title("Sticlmin")
global t
t = turtle.Turtle()
tg = turtle.Turtle()
t.hideturtle()
s.bgpic('add.gif')
def Human(t,xcord,ycord,s):
    t.speed(s)
    t.penup()
    t.goto(xcord,ycord)
    t.pendown()
    t.pencolor('black')
    t.hideturtle()
    t.pensize(5)
    t.rt(90)
    t.fd(100)
    t.rt(45)
    t.fd(50)
    t.back(50)
    t.lt(90)
    t.fd(50)
    t.back(50)
    t.rt(45)
    t.back(100)
    t.rt(45)
    t.fd(50)
    t.back(50)
    t.lt(90)
    t.fd(50)
    t.back(50)
    t.rt(225)
    t.fd(35)
    t.rt(90)
    t.circle(35)
def Ground(t,xcord,ycord,s):
    t.speed(s)
    t.penup()
    t.goto(xcord,ycord)
    t.pendown()
    t.pencolor('black')
    t.pensize(2.5)
    t.fillcolor('green')
    t.begin_fill()
    t.fd(2000)
    t.rt(90)
    t.fd(250)
    t.lt(270)
    t.fd(2000)
    t.end_fill()
def House(t,xcord,ycord):
    t.penup()
    t.goto(xcord,ycord)
    t.pendown()
    t.pensize(2)
    t.fillcolor('yellow')
    t.lr(90)
    t.fd(200)
    t.rl(90)

Human(turtle,50,0,2)
Human(t,-50,0,2)
Ground(tg,-1000,-250,3)
a = 0
input(a)
