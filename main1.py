import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300,400)
p = turtle.Turtle()
side = 5
length = 70
angle = 360.0/side
for i in range(side):
    p.forward(length)
    p.right(angle)
turtle.done()    