from turtle import *
from utility import *

scale = 1
size = 25
layers = 2

neurons_layer1 = 4
neurons_layer2 = 4

tech_first = ["Python", "Javascript", "Java", "ML"]
tech_second = ["Tensorflow", "Keras", "React Native", "AI"]
tech_third = ["Mohsin Tariq"]

pensize(2)
speed(500)

Screen().bgcolor("black")

# go to starting position
penup()
left(180)
forward(200)
right(90)
pendown()

# draw all neuron in layer one
layer1 = draw_layer( neurons_layer1, 1)


right(90)
penup()
forward(100)
right(90)
pendown()

layer2_in = draw_layer( neurons_layer2, 1)
layer2_out = [(x[0]+50, x[1]) for x in layer2_in]

print(layer2_in)
print(layer2_out)

penup()
left(90)
forward(200)
left(90)
forward(25*5)
pendown()

layer3_out = draw_neuron(1)
layer3_in = [(layer3_out[0]-50, layer3_out[1])]
penup()

color("White")
pensize(1)
connections(layer1, layer2_in)
connections(layer2_out, layer3_in)

penup()

labels(tech_first, layer1)
labels(tech_second, layer2_out)
labels(tech_third, [layer3_out])


done()