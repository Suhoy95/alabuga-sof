import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(10)

n = 50
iterations = 360 // 16

for i in range(iterations):
    t.forward(15)
    t.left(15)
