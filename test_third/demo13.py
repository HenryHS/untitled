import tensorflow as tf

a = tf.Variable(initial_value=3.14,dtype=tf.float32,name='a')
b = tf.Variable(initial_value=3.14,dtype=tf.float32,name='b')

c = a+b

d = tf.Variable(initial_value=3.14,dtype=tf.float32,name='d')
e = tf.add(c, d, name='e')


with tf.Session() as sess:
    tf.summary.FileWriter('../data',sess.graph)
    sess.run(tf.global_variables_initializer())
    print(sess.run(e))


