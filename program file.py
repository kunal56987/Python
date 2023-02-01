import turtle
import time
pen=turtle.Turtle()
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def text1():
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color('orange')
    pen.write('I REALLY LOVE YOU YAAR')

heart()
text1()
time.sleep(5)
pen.ht()