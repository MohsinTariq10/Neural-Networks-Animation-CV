from turtle import *
from utility import *

scale = 1
size = 25
layers = 2

speed(100)

# go to starting position
penup()
left(90)
left(90)
forward(200)
right(90)
pendown()

# draw all neuron in layer one
layer1 = draw_layer( 3, 1)


right(90)
penup()
forward(100)
right(90)
pendown()

layer2 = draw_layer( 5, 1)


penup()
left(90)
forward(200)
left(90)
forward(25*5)
pendown()

layer3 = draw_neuron(1)

penup()



connections(layer1, layer2)
connections(layer2, [layer3])

write("GeeksForGeeks")



done()