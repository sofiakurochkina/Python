# Imports

import math
print ("It's math! It has type {}".format(type(math)))
# It's math! It has type <class 'module'>

# math is a module ( a collection of variables (a namespace) defined by someone else)
# see all names in math using dir()

print(dir(math))
print("pi to 4 significant digits = {:.4}".format(math.pi))
# pi to 4 significant digits = 3.142

# functions
# math.log
math.log(32,2)
# 5.0
# log(x[, base])

import math as mt
mt.pi
# 3.141592653589793
# You may have seen code that does this with certain popular libraries like Pandas, Numpy, Tensorflow, or Matplotlib. 
# For example, it's a common convention to import numpy as np and import pandas as pd.
# as simply renames the imported module 

import math
mt = math

# import * makes all the module's variables directly accessible to you (without any dotted prefix)
from math import *
print (pi, log(32,2))
# 3.141592653589793 5.0

#  import only the specific things we'll need from each module
from math import log,pi
from numpy import asarray 

# Submodules
import numpy 
print ("numpy.random is a",type (numpy.random))
print ("it contains names such as...",
dir(numpy.random)[-15:]
)
#numpy.random is a <class 'module'>
# it contains names such as... ['set_state', 'shuffle', 'standard_cauchy', 'standard_exponential', 'standard_gamma', 'standard_normal', 'standard_t', 'test', 'triangular', 'uniform', 'vonmises', 'wald', 'warnings', 'weibull', 'zipf']

# So if we import numpy as above, then calling a function in the random "submodule" will require two dots.

# Roll 10 dice
rolls=numpy.random.randint(low=1, high=6, size=10)
rolls
# array([4, 1, 2, 2, 1, 3, 1, 1, 5, 2])

# For example, if you work with the graphing library matplotlib, you'll be coming into contact with objects it defines which represent Subplots, Figures, TickMarks, and Annotations.
# pandas functions will give you DataFrames and Series


# !!! a quick survival guide for working with strange types
# THREE TOOLS FOR UNDERSTANDING STRANGE OBJECTS

# 1 
# type()

type(rolls)
# numpy.ndarray

# 2
# dir()

print(dir(rolls))
rolls.mean()
# 2.2
rolls.tolist()
# [4, 1, 2, 2, 1, 3, 1, 1, 5, 2]

# 3
# help ()

help(rolls.ravel)

rolls + 10
# array([14, 11, 12, 12, 11, 13, 11, 11, 15, 12])

# At which indices are the dice less than or equal to 3?
rolls <= 3
# array([False,  True,  True,  True,  True,  True,  True,  True, False, True])

xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))

# xlist = [[1, 2, 3], [2, 4, 6]]
# x =
# [[1 2 3]
# [2 4 6]]

# Get the last element of the second row of our numpy array
x[1,-1]
# 6

# When does 1+1 not equal 2?
#  tensorflow, a Python library popularly used for deep learning. It makes extensive use of operator overloading.
import tensorflow as tf
# Create two constants, each with value 1
a = tf.constant(1)
b = tf.constant(1)
# Add them together to get...
a + b

