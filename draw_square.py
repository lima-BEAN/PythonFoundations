# draws 
import turtle

def main():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = create_turtle("turtle", "yellow", 2, "square")
    angie = create_turtle("arrow", "green", 4, "circle")
    rome = create_turtle("triangle", "blue", 3, "triangle")

    window.exitonclick()

def create_turtle(t_shape, color, speed, shape):

    my_turtle = turtle.Turtle()
    my_turtle.shape(t_shape)
    my_turtle.color(color)
    my_turtle.speed(speed)

    draw(my_turtle, shape)

def draw(turtle, shape):

    if shape == "square":
        for x in range(4):
            turtle.forward(100)
            turtle.right(90)
    elif shape == "circle":
        turtle.circle(100)
    elif shape == "triangle":
        turtle.backward(100)
        turtle.left(45)
        turtle.forward(70)
        turtle.right(90)
        turtle.forward(70)
        
main()
