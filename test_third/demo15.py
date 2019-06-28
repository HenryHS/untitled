import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('../data/input_data')
print(mnist.train.images.shape)
print(mnist.train.labels.shape)
print(mnist.train.images[0])
print(mnist.train.labels[0])

