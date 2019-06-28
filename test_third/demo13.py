import tensorflow as tf

a = tf.Variable(initial_value=3.14,dtype=tf.float32,name='a')
b = tf.Variable(initial_value=3.14,dtype=tf.float32,name='b')

c = a+b

d = tf.Variable(initial_value=3.14,dtype=tf.float32,name='d')

sess = tf.Session()

sess.run(tf.global_variables_initializer())


e = tf.add(c,d,name='e')

print(sess.run(e))

sess.close()

