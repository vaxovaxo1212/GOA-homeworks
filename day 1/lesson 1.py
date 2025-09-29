from turtle import *


#we want to paint a house

width(7)
color("red")
#step 1: draw a square
speed(5)
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()
end_fill
color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
forward(50)
color("blue")
begin_fill()
right(940)
goto(50, 150)
pendown()
right(20)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()
left(90)
penup()
forward(98)
begin_fill()
pendown()
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()


exitonclick()