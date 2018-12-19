#!/usr/bin/env python3

import tensorflow as tf

a = tf.constant(6, name='constant_a')
b = tf.constant(3, name='constant_b')
c = tf.constant(10, name='constant_c')
d = tf.constant(5, name='constant_d')

mul = tf.multiply(a, b, name="mul")
div = tf.div(c, d, name="div")
addn = tf.add_n([mul, div], name="addn")

print("The addn tensor contains: ")
print(addn)

print(a)

print(mul)

sess = tf.Session()

print(sess.run(addn))
print(sess.run(mul))
print(sess.run(div))

writer = tf.summary.FileWriter('./m2_example1', sess.graph)

writer.close()

sess.close()

# To view the graph open the log in tensorboard
# tensorboard --logdir="m2_example1"