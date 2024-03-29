# -*- coding: utf-8 -*-
"""tensorflow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pXuqsAzPPK0-RZNe0Rg66pdZ4nKEpvRs

## Tensors
Generalization of vectors and matrices to higher dimensions.
Tensorflow represents tensors as n-dimensional arrays of base datatypes.
"""

import tensorflow as tf

"""###Creating Tensors"""

string = tf.Variable("this is a string", tf.string)
number = tf.Variable(123, tf.int16)
floating = tf.Variable(3.5, tf.float64)

"""###Rank/Degree of Tensors"""

rank1_tensor = tf.Variable(["Test"], tf.string)
rank2_tensor = tf.Variable([["test","ok"], ["test","yes"]], tf.string)

tf.rank(rank1_tensor)

rank1_tensor.shape

rank2_tensor.shape

tensor1 = tf.ones([1,2,3])
tensor2 = tf.reshape(tensor1, [2,3,1])
tensor3 = tf.reshape(tensor2, [3,-1])

print(tensor1)
print(tensor2)
print(tensor3)

"""### Types of Tensors
#####1.Variable
#####2.Constant
#####3.Placeholder
#####4.SparseTensor

"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version
print(tf.version)

t = tf.zeros([5,5,5])

print(t)

d = tf.ones([5,5,5])

print(d)

d = tf.reshape(d,[125])

print(d)

