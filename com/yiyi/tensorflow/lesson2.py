#coding=utf-8
import tensorflow as tf

x = tf.placeholder(tf.float32)
W = tf.Variable(tf.zeros([1]))
b = tf.Variable(tf.zeros([1]))
y_ = tf.placeholder(tf.float32)

y = W * x + b

lost = tf.reduce_mean(tf.square(y_-y))
optimizer = tf.train.GradientDescentOptimizer(0.00000005)
train_step = optimizer.minimize(lost)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

steps = 2000
for i in range(steps):
    xs = [i]
    ys = [3 * i]
    feed = { x: xs, y_: ys }
    sess.run(train_step, feed_dict=feed)
    if i % 100 == 0 :
        print("After %d iteration:" % i)
        print("W: %f" % sess.run(W))
        print("b: %f" % sess.run(b))
        print("lost: %f" % sess.run(lost, feed_dict=feed))