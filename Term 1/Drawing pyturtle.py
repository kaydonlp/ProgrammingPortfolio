#The  better than best and cooler than coolest Drawing Turtle
#Kaydon Payne
#10/11/19

import turtle
turtle.setup(width=(1000), height=(1000))
##
##x = turtle.Pen()
##x.shape ("turtle")
##x.color ("blue", "red")
##x.speed (10)
##x.width(1)
##
##y = turtle.Pen()
##y.shape ("turtle")
##y.color ("orange", "yellow")
##y.speed (10)
##y.width(1 )

##x.up()
##x.setposition(150, 150)

##x.down()
##x.begin_fill()
##x.forward(100)
##x. left(90)
##x.forward(100)
##x. left(90)
##x.forward(100)
##x. left(90)
##x.forward(100)
##x. left(90)
##x.end_fill()
##x.reset()


##x.up()
##x.setposition(-0, -194)
##x.down()
##x.circle(100)
##
##x.up()
##x.setposition(-0, 0)
##x.down()
##x.circle(75)
##
##x.up()
##x.setposition(-0, 150)
##x.down()
##x.circle(50)
##x.reset()



turtle.reset()
turtle.shape("turtle")
turtle.speed(0)
turtle.bgcolor('black')

colors = [
#reddish colors
(1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
#orangey colors
(1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
#yellowy colors
(1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
#greenish colors
(0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
#blueish colors
(0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
]

c = 0
p = 0
while True:
    while p < 99:
        idx = int(c)
        color=colors[idx]
        turtle.color(color)
        turtle.hide()
        turtle.forward(p*10)
        turtle.right(144)
        p = p + 1
        c = c + 1

    turtle2= turtle.Pen()
    turtle2.speed(0)
    p=0
    while p < 99:
        turtle2.color("black")
        turtle2.forward(p*10)
        turtle2.right(144)
        p = p + 1
    turtle.reset()
    turtle2.reset()
    p=0
    c=0
    turtle.speed(0)
    turtle2.speed(0)
####while p != 0:
####    print("Test")
##turtle.left(144)
##turtle.left(180)
##turtle.color('black')
##turtle.width(13)
##while p != 0:
##    turtle.forward(p*10+1.5)
##    turtle.left(144)
##    p = p - 1

##
##for i in range(50):
##    x.circle(i*3)
##    x.left(10)
##
##
##
##for i in range(50):
##    y.circle(i*3)
##    y.left(10)

