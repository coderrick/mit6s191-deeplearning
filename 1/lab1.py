import tensorflow as tf
tf.enable_eager_execution()
import numpy as np
import matplotlib.pyplot as plt

a = tf.constant(15, name="a")
b = tf.constant(61, name="b")

# Add them!
c = tf.add(a,b, name="c")
tf.print(c)

#tensor is mainly used for the graph computation of expressions while Keras does the bulk is the MLp