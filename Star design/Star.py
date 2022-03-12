import turtle
import colorsys

y = turtle.Turtle()
d = turtle.Screen()
d.bgcolor('black')
y.speed(0)
p = 150
q = 0
y.left(180)
for i in range(180):
    v = colorsys.hsv_to_rgb(q, 1, 0.8)
    q+= 1/p
    y.color(v)
    y.left(144)
    y.forward(i*5)