import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)

t = turtle.Turtle()

for i in range(99999):
  t.shape("classic")

  x = random.randint(-200, 200)
  height = random.randint(100,350)

  t.left(90)
  t.penup()
  t.goto(x,-150)
  t.pendown()
  t.speed(1)
  t.color(100, 100, 100)
  t.forward(height)

	
  size = 50 
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  t.color(r, g, b)

  type = random.randint(1, 3)
  
  t.clear()

  if type == 2 :

  	t.speed(2)
  	t.color(0, 0, 0)
  	t.shape("circle")

  	for i in range(12):
  	  turn = random.randint(1, 360)
  	  d = random.randint(10,50)
  	  t.color(r, g, b)
  	  t.left(90)
  	  t.color(0, 0, 0)
  	  t.forward(d)


  if type == 1 :

  	t.speed(100)
  	for i in range(36):
  		t.forward(size)
  		t.backward(size)
	  	t.left(10)
	  	
	  	
  if type == 3 :
    t.penup()
    screen.bgcolor(r, g, b)
    time.sleep(0.3)
    screen.bgcolor("black")
    
    
    
  wait = random.randint(0, 2)
  time.sleep(wait)
  t.clear()
  t.right(90)
