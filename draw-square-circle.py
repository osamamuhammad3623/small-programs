import turtle

def draw_square(shape):
    for i in range(0,4):
        shape.forward(100)
        shape.right(90)

window = turtle.Screen()
window.bgcolor(1,0,0)

arrow = turtle.Turtle()
arrow.speed(0)

for i in range(0,360,10):
    arrow.right(10)
    draw_square(arrow)
    
window.exitonclick()