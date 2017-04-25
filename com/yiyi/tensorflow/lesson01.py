import tensorflow as tf

# hello = tf.constant('Hello, Tensorflow!')
# sess = tf.Session()
# print(sess.run(hello))

# # placehoder（占位符）
# x = tf.placeholder(tf.float32, [2, 2])
#
# # Variable（变量）
# y = tf.Variable(tf.zeros([2, 2]))
# y1 = tf.Variable(1.0, tf.float32)
#
# # Constant（常量）
# z = tf.constant(3.0, tf.float32)


x = tf.Variable(3, tf.int16)
y = tf.Variable(6, tf.int16)

z = tf.add(x, y)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(z))


