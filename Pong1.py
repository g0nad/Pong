# This is Pong

from curses import window
import turtle

# Create a new window
wn = turtle.Screen()
# Title of the window
wn.title("James' Pong Game")
# Background color of the window
wn.bgcolor("black") 
# Window size
wn.setup(width=800, height=600)
# Stop the window from updating
wn.tracer(0)
# Paddle A
# Name the function
paddle_a = turtle.Turtle()
# set the speed of the paddle as fast as it will go
paddle_a.speed(0)
# set the shape of the paddle
paddle_a.shape("square")
# Set the color of the paddle 
paddle_a.color("white")
# Make the paddle longer 
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# Makes the paddle start at the center
paddle_a.goto(350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(-350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Main game loop
while True:
    wn.update()
