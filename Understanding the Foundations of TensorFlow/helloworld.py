#!/usr/bin/env python3

import tensorflow as tf

hello = tf.constant('Hello World!')
sess = tf.Session()

print(sess.run(hello))

sess.close()