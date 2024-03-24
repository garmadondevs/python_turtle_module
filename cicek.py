import turtle
import time

tm = turtle.Turtle()
ts = turtle.Screen()
time.sleep(2)
ts.bgcolor("black")
tm.hideturtle()
tm.speed(0)
colors = ["pink","blue","green","red","yellow"]

def flower():
    for i in range(440):
        tm.color(colors[i % 5])
        tm.circle(190 - i, 90)
        tm.left(90)
        tm.circle(190 - i, 90)
        tm.left(18)

flower()

tm.penup()
tm.goto(210, 210) 
tm.pendown()
tm.pencolor("white") 
tm.write("garmadon.dev", font=("Arial", 18, "bold")) 
turtle.done()
