from turtle import *
#We want to paint a house

#step1 : draw a square
speed(30)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#End of square


#Drawing a door


forward(70)
color("yellow")
begin_fill()
left(90)

forward(120)  #height of the door
right(90)

forward(60)
right(90)

forward(120)
end_fill()
#End of the door drawing 


#start of the roof drawing
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()



#end of the roof drawing 

#start of the windows drawing 

#window 1
penup()
goto(20,140)
pendown()
color("brown")
begin_fill()

right(150)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)
end_fill()

penup()
goto(40, 140)
color("black")
width(2)
pendown()
right(90)
forward(40)

penup()
goto(20,160)
pendown()
right(90)
forward(40)

#window2

penup()
goto(180,140)
pendown()
color("brown")
begin_fill()
width(7)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)
end_fill()

penup()
goto(160,140)
pendown()
color("black")
width(2)

left(90)
forward(40)

penup()
goto(180,160)
pendown()
left(90)
forward(40)
penup()
goto(0,0)




exitonclick()


