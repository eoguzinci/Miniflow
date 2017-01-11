"""
This script builds and runs a graph with miniflow.

There is no need to change anything to solve this quiz!

However, feel free to play with the network! Can you also
build a network that solves the equation below?

(x + y) + y
"""

from miniflow import *

x, y, z = Input(), Input(), Input()

f1 = Add(x, y, z)
f2 = Mult(x,y,z)

feed_dict = {x: 4, y: 5, z: 10}

sorted_neurons = topological_sort(feed_dict)
output1 = forward_pass(f1, sorted_neurons)
output2 = forward_pass(f2 ,sorted_neurons)
# NOTE: because topological_sort set the values for the `Input` neurons we could also access
# the value for x with x.value (same goes for y).
print("{} + {} + {}= {} (according to miniflow)".format(feed_dict[x], feed_dict[y], feed_dict[z], output1))
print("{} * {} * {}= {} (according to miniflow)".format(feed_dict[x], feed_dict[y], feed_dict[z], output2))