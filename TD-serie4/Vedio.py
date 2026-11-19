import turtle
import colorsys

def draw_lumine_color():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Luminous Fractal Art")
    screen.setup(800, 600)
    t = turtle.Turtle()
    t.speed(0)
    turtle.tracer(50)
    t.hideturtle()
    start_hue = 0.1
    end_hue = 0.55

    for i in range(400):
        progress = i / 400
        current_hue = start_hue + (progress * (end_hue - start_hue))
        color = colorsys.hsv_to_rgb(current_hue, 0.9, 1.0)
        t.pencolor(color)
        t.penup()
        t.goto(0, 0)
        t.setheading(i * 15)
        t.pendown()
        t.forward(i * 0.8)
        t.right(45)
        t.circle(i * 0.3 , 99)
        t.width(i // 100 + 1)
        t.left(90)
        t.circle(i * 0.3 , 99)

draw_lumine_color()



