"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.speed(0)
tina.color('purple')
for i in range(2500):
    tina.forward(666)
    tina.left(666)
    tina.forward(666)
    tina.left(666)
    tina.forward(666)
    tina.left(666)
    tina.forward(i)
    