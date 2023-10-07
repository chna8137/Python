#code02-06.py

import turtle

myT = None

myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0,4) : # for(int = 0, i < 4, i++)
    myT.forward(200)
    myT.right(90)

turtle.done()