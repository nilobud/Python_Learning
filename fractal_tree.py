
import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

t = turtle.Turtle()
t.shape("turtle")
t.left(90)
t.speed(0)
t.up()
t.backward(100)
t.down()
t.color("green")
tree(150,t)