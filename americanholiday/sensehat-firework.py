#!/bin/python3
  
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

#C is Cyan, U is blue, R is red, B is black, Y is yellow, W is white, G is green, M is magenta
C = [0, 255, 255]
U = [0, 0, 255]
M = [255, 0, 255]
R = [255, 0, 0]
B = [0, 0, 0]
Y = [255, 255, 0]
W = [255, 255, 255]
G = [0, 255, 0]

fire1 = [
  W, W, W, B, B, W, W, W,
  W, U, B, Y, Y, B, U, W,
  W, B, Y, C, C, Y, B, W,
  B, Y, C, R, R, C, Y, B,
  B, Y, C, R, R, C, Y, B,
  W, B, Y, C, C, Y, B, W,
  W, U, B, Y, Y, B, U, W,
  W, W, W, B, B, W, W, W
  ]
  
fire2 = [
  G, R, R, B, B, R, R, G,
  R, R, B, B, B, B, R, R,
  R, B, B, G, G, B, B, R,
  B, B, G, R, W, G, B, B,
  B, B, G, W, R, G, B, B,
  R, B, B, G, G, B, B, R,
  R, R, B, B, B, B, R, R,
  G, R, R, B, B, R, R, G
  ]
  
fire3 = [
  Y, B, B, B, B, B, B, Y,
  M, B, B, R, R, B, B, M,
  Y, B, R, B, B, R, B, Y,
  U, B, R, B, B, B, B, C,
  U, B, R, R, R, B, B, C,
  Y, B, R, B, B, R, B, Y,
  M, B, B, R, R, B, B, M,
  Y, B, B, B, B, B, B, Y
  ]
  
fire4 = [
  C, C, C, C, C, C, C, U,
  C, C, C, C, C, C, U, U,
  C, C, C, C, C, U, U, C,
  C, C, C, C, U, U, C, C,
  C, C, C, U, U, C, C, C,
  C, C, U, U, C, C, C, C,
  C, U, U, C, C, C, C, C,
  U, U, C, C, C, C, C, C
  ]
  
fire5 = [
  W, W, W, W, R, W, W, W,
  W, W, W, R, W, W, W, W,
  W, W, R, W, W, W, W, W,
  W, R, W, W, R, W, W, W,
  W, R, R, R, R, R, W, W,
  W, W, W, W, R, W, W, W,
  W, W, W, W, R, W, W, W,
  W, W, W, W, W, W, W, W
  ]
  
nofire = [
  W, W, W, W, W, W, W, W,
  W, W, W, W, W, W, W, G,
  W, W, W, W, W, W, G, G,
  W, W, W, W, W, G, G, W,
  W, W, W, W, G, G, W, W,
  G, W, W, G, G, W, W, W,
  G, G, G, G, W, W, W, W,
  W, G, G, W, W, W, W, W
  ]


while True:
  temperature = sense.temperature
  humidity = sense.humidity
  if (temperature < 15 and humidity > 90):
    sense.set_pixels(nofire)
  else:
    sense.set_pixels(fire1)
    time.sleep(0.5)
    sense.set_pixels(fire2)
    time.sleep(0.5)
    sense.set_pixels(fire3)
    time.sleep(1)
    sense.set_pixels(fire4)
    time.sleep(1)
    sense.set_pixels(fire5)
    time.sleep(1)
