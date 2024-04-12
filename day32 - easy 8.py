#44 Programming questions Code
#Easy questions:
#8) The coordinates of the centres and radii of two circles are chosen randomly. At what points (if any) do the circles intersect?

print("44 Programming questions Code - Easy 8\nhttps://github.com/xsenemy/44-programming-questions\n")

import random
from turtle import Turtle, Screen


def easy_8():
    circle_a = {
        "x" : random.randint(-150, 150),
        "y" : random.randint(-150, 150),
        "radius" : random.randint(50, 100),
    }
    circle_b = {
        "x" : random.randint(0, 100),
        "y" : random.randint(0, 100),
        "radius" : random.randint(50, 100),
    }

    screen = Screen()
    screen.setup(width=600, height=600, startx=900, starty=200)
    global turtle_a
    turtle_a = Turtle()
    global turtle_b
    turtle_b = Turtle()
    global intersections
    intersections = Turtle()
    cross = Turtle()
    turtle_a.speed(0)
    turtle_b.speed(0)
    intersections.speed(0)
    cross.speed(0)
    turtle_a.hideturtle()
    turtle_b.hideturtle()
    intersections.hideturtle()
    cross.hideturtle()

    cross.fd(10)
    cross.bk(20)
    cross.fd(10)
    cross.setheading(90)
    cross.fd(10)
    cross.bk(20)
    cross.fd(10)

    turtle_a.penup()
    turtle_b.penup()
    turtle_a.goto(circle_a["x"], circle_a["y"])
    turtle_b.goto(circle_b["x"], circle_b["y"])


    # d = turtle_a.distance(turtle_b)
    d = ((turtle_a.xcor() - turtle_b.xcor())**2 + (turtle_a.ycor() - turtle_b.ycor())**2)**0.5
    if d > circle_a["radius"] + circle_b["radius"]:
        print("Circles are separate")
    elif d < abs(circle_a["radius"] - circle_b["radius"]):
        print("One circle is contained within the other")
    else:
        a = (circle_a["radius"]**2 - circle_b["radius"]**2 + d**2) / (d * 2)
        h = (circle_a["radius"]**2 - a**2)**0.5

        x2 = turtle_a.xcor() + a * (turtle_b.xcor() - turtle_a.xcor()) / d
        y2 = turtle_a.ycor() + a * (turtle_b.ycor() - turtle_a.ycor()) / d
        p2 = (x2, y2)

        x3_1 = x2 + h * (turtle_b.ycor() - turtle_a.ycor()) / d
        y3_1 = y2 - h * (turtle_b.xcor() - turtle_a.xcor()) / d
        p3_1 = (x3_1, y3_1)

        x3_2 = x2 - h * (turtle_b.ycor() - turtle_a.ycor()) / d
        y3_2 = y2 + h * (turtle_b.xcor() - turtle_a.xcor()) / d
        p3_2 = (x3_2, y3_2)


        intersections.penup()
        intersections.goto(p3_1)
        intersections.dot(7, "black")

        intersections.penup()
        intersections.goto(p3_2)
        intersections.dot(7, "black")

        print("Circle A (red):")
        print(f'Position: ({circle_a["x"]}, {circle_a["y"]})', f'Radius: {circle_a["radius"]}')
        print("Circle B (blue):")
        print(f'Position: ({circle_b["x"]}, {circle_b["y"]})', f'Radius: {circle_b["radius"]}')
        print(f"Distance: {round(d, 2)}")
        # print("Intersections points:")
        print(f"Intersections points: ({round(x3_1, 2)}, {round(y3_1, 2)})", f"({round(x3_2, 2)}, {round(y3_2, 2)})", sep=", ")

    turtle_a.goto(circle_a["x"], circle_a["y"]-circle_a["radius"])
    turtle_b.goto(circle_b["x"], circle_b["y"]-circle_b["radius"])
    turtle_a.pendown()
    turtle_b.pendown()
    turtle_a.pencolor("red")
    turtle_b.pencolor("blue")
    turtle_a.circle(circle_a["radius"])
    turtle_b.circle(circle_b["radius"])
    print("Press r to repeat, press q to quit \n")
    screen.listen()
    screen.onkey(r, "r")
    screen.onkey(q, "q")
    screen.mainloop()


def r():
    turtle_a.clear()
    turtle_b.clear()
    intersections.clear()
    easy_8()


def q():
    quit()


easy_8()
