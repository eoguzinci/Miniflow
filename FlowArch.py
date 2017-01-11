# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 18:42:53 2017

@author: oguzi
"""

class Neuron:
    def __init__(self, inbound_neurons=[]):
        # Neuron from which this Neuron receives values
        self.inbound_neurons = inbound_neurons
        # Neuron to which this Neuron passes values
        self.outbound_neurons = []
        # A calculated value
        self.value = None
        # Add this node as an outbound node on its inputs.
        for n in self.inbound_neurons:
            n.outbound_neurons.append(self)

    def forward(self):
        """
        Forward propagation.

        Compute the output value based on `inbound_neurons` and
        store the result in self.value.
        """
        raise NotImplemented

    def backward(self):
        """
        Backward propagation.

        You'll compute this later.
        """
        raise NotImplemented
        
class Input(Neuron):
    def __init__(self):
        # An Input neuron has no inbound neurons,
        # so no need to pass anything to the Neuron instantiator.
        Neuron.__init__(self)

    # NOTE: Input neuron is the only node where the value
    # may be passed as an argument to forward().
    #
    # All other neuron implementations should get the value
    # of the previous neuron from self.inbound_neurons
    #
    # Example:
    # val0 = self.inbound_neurons[0].value
    def forward(self, value=None):
        # Overwrite the value if one is passed in.
        if value is not None:
            self.value = value
            
class Add(Neuron):
    def __init__(self, x, y):
        Neuron.__init__(self, [x, y])

    def forward(self):
        """
        You'll be writing code here in the next quiz!
        """
        
def forward_pass(output_neuron, sorted_neurons):
    """
    Performs a forward pass through a list of sorted neurons.

    Arguments:

        `output_neuron`: The output neuron of the graph (no outgoing edges).
        `sorted_neurons`: a topologically sorted list of neurons.

    Returns the output neuron's value
    """

    for n in sorted_neurons:
        n.forward()

    return output_neuron.value