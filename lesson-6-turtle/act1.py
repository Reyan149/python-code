import turtle

turtle.Screen().bgcolor("lightblue")

sc = turtle.Screen()
sc.setup(500,500)

turtle.title("Turtle Graphics")

board = turtle.Turtle()


for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1

turtle.done()