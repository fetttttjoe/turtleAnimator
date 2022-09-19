import turtle
import colorsys
pen = turtle.Pen()
turtle.bgcolor("black")
h = 0
n = 36
for x in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    pen.pencolor(c)
    pen.width(x/100)
    pen.forward(x)
    pen.left(80)