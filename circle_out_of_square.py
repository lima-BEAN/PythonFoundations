import turtle

def main():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = create_turtle("turtle", "yellow", 2, "square")
    window.exitonclick()

def create_turtle(t_shape, color, speed, shape):

    my_turtle = turtle.Turtle()
    my_turtle.shape(t_shape)
    my_turtle.color(color)
    my_turtle.speed(speed)

    draw(my_turtle, shape)

def draw(turtle, shape):

# circle out of squares
    if shape == "square":
        for i in range(36):
            for x in range(4):
                turtle.forward(100)
                turtle.right(90)
            turtle.right(10)
        
main()
