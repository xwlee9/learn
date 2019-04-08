import tensorflow as tf
import numpy as np
x_data = np.linspace(-1,1,300,dtype=np.float32)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data)-0.5+noise
Weight = tf.Variable(tf.random_normal([1,10]))
biase = tf.Variable(tf.zeros([1,10])+0.1)
Wx_plus_b = tf.matmul(x_data,Weight)+biase
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # print(x_data)
    # print(Weight)
    print(sess.run(Wx_plus_b))

    # sess.run(print(1+1))
# tf.matmul()
