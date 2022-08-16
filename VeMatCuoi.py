# Ve mat cuoi

import turtle

t = turtle.Turtle()

t.pensize(5)
t.pencolor("blue")
t.speed(0)

BanKinhMat = 100
BanKinhConMat = 10
CanhMui = 20

# Ve mat
t.circle(BanKinhMat)



# Ve mui
t.penup()
t.goto(0,120)
t.pendown()
t.circle(-CanhMui, steps=3)


# Ve con mat
t.penup()
t.goto(-40,130)
t.fillcolor("red")
t.begin_fill()
t.pendown()
t.circle(BanKinhConMat)
t.penup()
t.goto(40,130)
t.pendown()
t.circle(BanKinhConMat)
t.end_fill()

# Mieng cuoi
t.penup()
t.goto(-35,70)
t.pendown()
t.right(90)
t.circle(35,180)

# Ket thuc
turtle.mainloop()