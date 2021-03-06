# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:36:24 2017

@author: oguzi
"""

"""
Modify Linear#forward so that it linearly transforms
input matrices, weights matrices and a bias vector to
an output.
"""

import numpy as np

class Layer:
    def __init__(self, inbound_layers=[]):
        self.inbound_layers = inbound_layers
        self.value = None
        self.outbound_layers = []
        for layer in inbound_layers:
            layer.outbound_layers.append(self)

    def forward():
        raise NotImplementedError


class Input(Layer):
    """
    While it may be strange to consider an input a layer when
    an input is only an individual node in a layer, for the sake
    of simpler code we'll still use Layer as the base class.
    
    Think of Input as collating many individual input nodes into
    a Layer.
    """
    def __init__(self):
        # An Input layer has no inbound layers,
        # so no need to pass anything to the Layer instantiator
        Layer.__init__(self)

    def forward(self):
        # Do nothing because nothing is calculated.
        pass


class Linear(Layer):
    def __init__(self, inbound_layer, weights, bias):
        # Notice the ordering of the input layers passed to the
        # Layer constructor.
        Layer.__init__(self, [inbound_layer, weights, bias])

    def forward(self):
        """
        Set the value of this layer to the linear transform output.
        
        Your code goes here!
        """
        inputs = self.inbound_layers[0].value
        weights = self.inbound_layers[1].value
        bias = self.inbound_layers[2].value
        self.value = np.dot(inputs,weights) + bias

class Sigmoid(Layer):
    """
    You need to fix the `_sigmoid` and `forward` methods.
    """
    def __init__(self, layer):
        Layer.__init__(self, [layer])

    def _sigmoid(self, x):
        """
        This method is separate from `forward` because it
        will be used with `backward` as well.

        `x`: A numpy array-like object.

        Return the result of the sigmoid function.
        
        Your code here!
        """
        return 1. /(1. +np.exp(-x))

    def forward(self):
        """
        Set the value of this layer to the result of the
        sigmoid function, `_sigmoid`.
        
        Your code here!
        """
        # This is a dummy value to prevent numpy errors
        # if you test without changing this method. 
        self.value = self._sigmoid(self.inbound_layers[0].value)
        
class MSE(Layer):
    def __init__(self, y, a):
        """
        The mean squared error cost function.
        Should be used as the last layer for a network.
        """
        # Call the base class' constructor.
        Layer.__init__(self, [y, a])

    def forward(self):
        """
        Calculates the mean squared error.
        """
        # NOTE: We reshape these to avoid possible matrix/vector broadcast
        # errors.
        #
        # For example, if we subtract an array of shape (3,) from an array of shape
        # (3,1) we get an array of shape(3,3) as the result when we want
        # an array of shape (3,1) instead.
        #
        # Making both arrays (3,1) insures the result is (3,1) and does
        # an elementwise subtraction as expected.
        y = self.inbound_layers[0].value.reshape(-1, 1)
        a = self.inbound_layers[1].value.reshape(-1, 1)
        # TODO: your code here
        summ = 0
        for i in range(len(self.inbound_layers[0].value)):
            summ += (y[i]-a[i])**2
        self.value = summ/len(self.inbound_layers[0].value)
        
        # UDACITY SOLUTION
#        y = self.inbound_layers[0].value.reshape(-1, 1)
#        a = self.inbound_layers[1].value.reshape(-1, 1)
#        m = self.inbound_layers[0].value.shape[0]
#
#        diff = y - a
#        self.value = np.mean(diff**2)


def topological_sort(feed_dict):
    """
    Sort the layers in topological order using Kahn's Algorithm.

    `feed_dict`: A dictionary where the key is a `Input` Layer and the value is the respective value feed to that Layer.

    Returns a list of sorted layers.
    """

    input_layers = [n for n in feed_dict.keys()]

    G = {}
    layers = [n for n in input_layers]
    while len(layers) > 0:
        n = layers.pop(0)
        if n not in G:
            G[n] = {'in': set(), 'out': set()}
        for m in n.outbound_layers:
            if m not in G:
                G[m] = {'in': set(), 'out': set()}
            G[n]['out'].add(m)
            G[m]['in'].add(n)
            layers.append(m)

    L = []
    S = set(input_layers)
    while len(S) > 0:
        n = S.pop()

        if isinstance(n, Input):
            n.value = feed_dict[n]

        L.append(n)
        for m in n.outbound_layers:
            G[n]['out'].remove(m)
            G[m]['in'].remove(n)
            # if no other incoming edges add to S
            if len(G[m]['in']) == 0:
                S.add(m)
    return L


def forward_pass(output_layer, sorted_layers):
    """
    Performs a forward pass through a list of sorted Layers.

    Arguments:

        `output_layer`: A Layer in the graph, should be the output layer (have no outgoing edges).
        `sorted_layers`: a topologically sorted list of layers.

    Returns the output layer's value
    """

    for n in sorted_layers:
        n.forward()

    return output_layer.value