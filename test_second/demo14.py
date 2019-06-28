import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100).astype(np.float32)
y = np.sin(x) + np.random.uniform(-0.5, 0.5, 100).astype(np.float32)
x3 = [[i*i*i,i*i,i] for i in x]
# plt.scatter(x,y)
# plt.show()
w = tf.Variable(initial_value=[[0.0], [0.0], [0.0]], dtype=tf.float32, name='W')
w1 = tf.Variable(initial_value=0.0, dtype=tf.float32, name='W1')
w2 = tf.Variable(initial_value=0.0, dtype=tf.float32, name='W2')
w3 = tf.Variable(initial_value=0.0, dtype=tf.float32, name='W3')
b = tf.Variable(initial_value=0.0, dtype=tf.float32, name='B')
# predict = tf.add(tf.matmul(x3, w), b, name='Predict')
predict = tf.add(tf.multiply(x, w1), b, name='Predict1b')
predict = tf.add(tf.multiply(tf.pow(x, 2), w2), predict, name='Predict2')
predict = tf.add(tf.multiply(tf.pow(x, 3), w3), predict, name='Predict3')
error = tf.reduce_mean(tf.square(y - predict), name='Error')
op = tf.train.GradientDescentOptimizer(0.008).minimize(error)
tf.summary.scalar('err', error)
merge = tf.summary.merge_all()

with tf.Session() as sess:
    fw = tf.summary.FileWriter('../data',sess.graph)
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        fw.add_summary(merge.eval(),i)
        sess.run(op)
        if i % 10 == 0:
            print(error.eval())
    print(w2.eval(),w1.eval(),b.eval())
    plt.scatter(x, y)
    plt.plot(x, predict.eval())
    plt.show()
