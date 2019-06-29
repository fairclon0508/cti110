# CH 4 Tutorial
# 6/29/2019
# CTI-110 P4T1 - Turtle shapes
# Faircloth N
#

import turtle

def main():
    win = turtle.Screen()
    t = turtle.Turtle()

    #make pen blue, draw square using for loop
    t.color('blue')
    for i in range(4):
        t.forward(100)
        t.left(90)

    #move pen
    t.penup()
    t.backward(200)
    t.pendown()
    
    #make pen red, draw triangle using for loop
    t.color('red')
    for i in range(3):
        t.forward(100)
        t.left(120)
        
    #wait for user to close window
    win.mainloop()
    
main()
