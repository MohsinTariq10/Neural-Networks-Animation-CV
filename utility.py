from turtle import *

def draw_layer(num=3, scale = 1):
    starting = []
    for i in range(num):
        starting.append(draw_neuron(scale))
        # don't move cursor if last
        if i == num-1:
            break
        penup()
        forward(50 + 25)
        pendown()
    return starting


def draw_neuron(scale= 2):
    position = pos()
    color("red")
    begin_fill()
    circle(25*scale)
    end_fill()
    return position

def connections(layer_in, layer_out):
    for i in range(len(layer_in)):
        for j in range(len(layer_out)):
            goto(layer_in[i])
            pendown()
            goto(layer_out[j])
            penup()
