# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 02:06:09 2017

@author: oguzi
"""

def gradient_descent_update(x, gradx, learning_rate):
    """
    Performs a gradient descent update.
    """
    # TODO: Implement gradient descent.
    
    # Return the new value for x
    x = x - learning_rate * gradx
    return x
