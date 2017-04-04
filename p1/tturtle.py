import turtle

def draw_rec():
	window = turtle.Screen()
	window.bgcolor("blue")

	boy = turtle.Turtle()
	boy.shape("turtle")
	boy.color("white")

	#boy.right(90)
	i = 0
	while i < 36:
		boy.forward(50)
		boy.right(30)
		boy.forward(50)
		boy.right(150)
		boy.forward(50)
		boy.right(30)
		boy.forward(50)
		boy.right(140)
		i += 1

	boy.right(90)
	boy.forward(200)

	window.exitonclick()
draw_rec()
