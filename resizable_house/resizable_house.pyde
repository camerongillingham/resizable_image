# Cameron Gillingham
# CLass: CS20
# Description: created a resizable picture of a house
# Date: Sept. 30, 2020

# x is the x of the canvas
# y is the y of the canvas

size(600, 600)


def drawhouse(x, y):
    print(mouseX, mouseY)
    rect(x/3, y/5, x/5, 11*y/75)
    triangle(x/3, y/5, 13*x/30, y/10, 8*x/15, y/5)
    rect(2*x/5, 7*y/25, x/25, y/15)
    circle(41*x/100, 8*y/25, x/150)
    rect(7*x/15, 7*y/30, x/25, y/25)
    rect(7*x/15, 7*y/30, x/50, y/50)
    rect(73*x/150, 7*y/30, x/50, y/50)
    rect(7*x/15, 19*y/75, x/50, y/50)
    line(13*x/30, y/10, 7*x/20, 23*y/300)
    line(x/3, y/5, 13*x/50, y/6)
    line(x/3, 103*y/300, 77*x/300, 19*y/60)
    line(77*x/300, 19*y/60, 13*x/50, y/6)
    line(13*x/50, y/6, 7*x/20, 23*y/300)

drawhouse(width, height)
