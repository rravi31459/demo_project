# here some chnaegs are made in this  file now  
# these are the after cahngs that i made   here
# some more

import turtle
# Screen setup
screen = turtle.Screen()
screen.title("Chessboard")

# Turtle setup
board = turtle.Turtle()
board.speed(0)
board.hideturtle()

# Size of each square
square_size = 50

# Starting position
start_x = -200
start_y = 200

# Draw chessboard
for row in range(8):
    for col in range(8):
        x = start_x + col * square_size
        y = start_y - row * square_size

        board.penup()
        board.goto(x, y)
        board.pendown()

        # Alternate colors
        if (row + col) % 2 == 0:
            board.fillcolor("white")
        else:
            board.fillcolor("black")

        board.begin_fill()

        for _ in range(4):
            board.forward(square_size)
            board.right(90)

        board.end_fill()

turtle.done()
