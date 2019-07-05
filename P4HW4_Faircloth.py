# Nested Loops
# 7/5/2019
# CTI-110 P4HW4 - Nested Loops
# N Faircloth
#


#desc:
#use nested loops and turtle to draw snowflakes

import turtle

def main():
    #repeatedly attempt to get a number input from user
    while True:
        temp = input("Enter an integer 3-9: ")
        try:
            n = int(temp)
            if 3 <= n <= 9:
                break
        except:
            print("Error")

    #open turtle
    win = turtle.Screen()
    t = turtle.Turtle()
    t.penup()
    t.forward(00)
    t.pendown()
    t.left(90)
    
    #generate outer geometry
    for innerring in range(n):
        t.left(360/n)
        t.forward(n*10)
        for outerring in range(n):
            t.right(360/n)
            t.forward(n*5)
            for branch in range(n):
                t.right(360/n)
                t.forward(n*3)
                
    #generate inner geometry
    for branch in range(n):
        t.left(360/n)
        t.forward(n*10)
        for inner in range(n):
            t.left(360/n)
            t.forward(n*3)
            for center in range(n):
                t.left(360/n)
                t.forward(n)

    #wait for user to close window
    win.mainloop()
    
main()
