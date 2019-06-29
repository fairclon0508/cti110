# CH 4 Tutorial
# 6/29/2019
# CTI-110 P4T1b - Turtle, draw initials
# Faircloth N
#

import turtle

def main():
    win = turtle.Screen()
    t = turtle.Turtle()
    t.pensize(10)
    t.color('blue')

    #move pen to starting location
    t.penup()
    t.backward(100)
    t.pendown()

    #draw N
    t.left(90)
    t.forward(100)
    t.right(145)
    t.forward(125)
    t.left(145)
    t.forward(100)

    #move pen to start of F
    t.penup()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(180)
    t.pendown()
    
    #draw F
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(70)

    #wait for user to close window
    win.mainloop()
    
main()
