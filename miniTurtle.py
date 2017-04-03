import turtle

def main():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = create_turtle("turtle", "yellow", 10, "square")

    window.exitonclick()

def create_turtle(t_shape, color, speed, shape):

    my_turtle = turtle.Turtle()
    my_turtle.shape(t_shape)
    my_turtle.color(color)
    my_turtle.speed(speed)

    draw(my_turtle, shape)

def draw(turtle, shape):

    for i in range(36):
        if shape == "square":
            for x in range(4):
                turtle.forward(100)
                turtle.right(90)
        turtle.right(10)
    turtle.right(90)
    turtle.forward(300)

        
main()
