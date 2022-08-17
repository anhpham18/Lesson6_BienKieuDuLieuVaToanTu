import turtle
import math


t = turtle.Turtle()
npa_screen = turtle.Screen()

turtle.bgcolor("light blue")
t.pensize(2)
t.speed(0)

t.penup()
t.goto(-300,-300)
CaoNha = 150
NgangNha = 120
SauNha = 100
RongCuaChinh = 40
CaoCuaChinh = 75
CaoCuaSo = 40
NgangCuaSo = 40


# Mặt trước: màu xanh dương
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.forward(NgangNha)
t.left(90)
t.forward(CaoNha)
t.left(90)
t.forward(NgangNha)
t.left(90)
t.forward(CaoNha)
t.end_fill()

# Cửa chính: màu xanh lá
t.penup()
t.left(90)
t.forward(RongCuaChinh)
t.pendown()
t.fillcolor("light green")
t.begin_fill()
t.left(90)
t.forward(CaoCuaChinh)
t.right(90)
t.forward(RongCuaChinh)
t.right(90)
t.forward(CaoCuaChinh)
t.right(90)
t.forward(RongCuaChinh)
t.end_fill()

# Mặt tường bên phải: màu vàng
t.penup()
t.left(180)
t.forward(80)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.left(30)
t.forward(SauNha)
t.right(120)
t.backward(CaoNha)
t.right(60)
t.forward(SauNha)
t.left(60)
t.forward(CaoNha)
t.end_fill()


# Mái trước: hình tam giác, màu hồng 
t.penup()
t.backward(CaoNha)
t.right(90)
t.pendown()
t.fillcolor(244/255, 30/255, 220/255)
t.begin_fill()
t.forward(NgangNha)
t.right(135)
t.forward(NgangNha/math.sqrt(2))
t.right(90)
t.forward(NgangNha/math.sqrt(2))
t.end_fill()


# Sâu mái nhà: Màu cam
t.penup()
t.backward(NgangNha/math.sqrt(2))
t.left(75)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.forward(SauNha)
t.right(75)
t.forward(NgangNha/math.sqrt(2))
t.right(105)
t.forward(SauNha)
t.right(75)
t.forward(NgangNha/math.sqrt(2))
t.end_fill()


# Cửa sổ: Màu nâu
t.penup()
t.backward(NgangNha/math.sqrt(2))
t.left(135)
t.forward(40)
t.left(120)
t.forward(30)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.forward(NgangCuaSo)
t.right(120)
t.forward(CaoCuaSo)
t.right(60)
t.forward(NgangCuaSo)
t.right(120)
t.forward(CaoCuaSo)
t.end_fill()


# Thân cây: màu nâu
t.penup()
t.goto(200,-305)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.forward(60)
t.right(90)
t.forward(30)
t.right(90)
t.forward(60)
t.right(90)
t.forward(30)
t.end_fill()


# Tán lá: màu xanh lá (1/3)
t.penup()
t.right(90)
t.forward(60)
t.left(90)
t.forward(45)
t.pendown()
t.fillcolor("light green")
t.begin_fill()
t.left(45)
t.backward(120/math.sqrt(2))
t.left(90)
t.forward(120/math.sqrt(2))
t.left(45)
t.backward(120)



# Tán lá: màu xanh lá (2/3)
t.penup()
t.left(90)
t.forward(60)
t.left(90)
t.pendown()
t.left(45)
t.backward(120/math.sqrt(2))
t.left(90)
t.forward(120/math.sqrt(2))
t.left(45)
t.backward(120)



# Tán lá: màu xanh lá (3/3)
t.penup()
t.left(90)
t.forward(60)
t.left(90)
t.pendown()
t.left(45)
t.backward(120/math.sqrt(2))
t.left(90)
t.forward(120/math.sqrt(2))
t.left(45)
t.backward(120)
t.end_fill()


# Mặt trời
BanKinhMatTroi = 40
TiaDai = 50
TiaNgan = 30

t.penup()
t.goto(50,0)
t.pendown()
t.fillcolor("Yellow")
t.begin_fill()
t.circle(BanKinhMatTroi)
t.end_fill()


# Tia mặt trời
t.pensize(1)

t.penup()
t.right(90)
t.pendown()
t.forward(50)

t.penup()
t.backward(TiaDai+BanKinhMatTroi)
t.right(45)
t.forward(BanKinhMatTroi)
t.pendown()
t.forward(TiaNgan)

t.penup()
t.backward(TiaNgan+BanKinhMatTroi)
t.right(45)
t.forward(BanKinhMatTroi)
t.pendown()
t.forward(TiaDai)

t.penup()
t.backward(TiaDai+BanKinhMatTroi)
t.right(45)
t.forward(BanKinhMatTroi)
t.pendown()
t.forward(TiaNgan)

t.penup()
t.backward(TiaNgan+BanKinhMatTroi)
t.right(45)
t.forward(BanKinhMatTroi)
t.pendown()
t.forward(TiaDai)

t.penup()
t.backward(TiaDai+BanKinhMatTroi)
t.right(45)
t.forward(BanKinhMatTroi)
t.pendown()
t.forward(TiaNgan)

t.penup()
t.backward(TiaNgan+BanKinhMatTroi)
t.right(45)
t.forward(BanKinhMatTroi)
t.pendown()
t.forward(TiaDai)

t.penup()
t.backward(TiaDai+BanKinhMatTroi)
t.right(45)
t.forward(BanKinhMatTroi)
t.pendown()
t.forward(TiaNgan)


turtle.done()
