import turtle

def draw_square():
    # need a window
    window = turtle.Screen()
    window.bgcolor("yellow")

    franklin = turtle.Turtle()
    
    franklin.shape("turtle")
    franklin.color("red")
    franklin.speed(5)

    move_turtle(4, franklin)

    window.exitonclick()

def move_turtle(move, t):
    for m in range(move):
        t.forward(200)
        t.right(90)

draw_square()
