import turtle
t = turtle.Turtle()

def drawSpiral(turtle, lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t,lineLen-0.1)

drawSpiral(t,100)