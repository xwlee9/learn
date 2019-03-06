import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
def add_layer(inputs,in_size,out_size,activation_function=None):
    Weight = tf.Variable(tf.random_normal([in_size,out_size]))
    biase = tf.Variable(tf.zeros([1,out_size])+0.1)
    Wx_plus_b = tf.matmul(inputs,Weight)+biase
    Wx_plus_b = tf.nn.dropout(Wx_plus_b,keep_prob)
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

x_data = np.linspace(-1,1,300,dtype=np.float32)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data)-0.5+noise
# print (x_data)
xs = tf.placeholder(dtype=tf.float32,shape=[None,1])
ys = tf.placeholder(dtype=tf.float32,shape=[None,1])
keep_prob = tf.placeholder(dtype=tf.float32)
# zs = tf.placeholder()
l1 = add_layer(xs,1,10,activation_function=tf.nn.relu)
prediction = add_layer(l1,10,1,activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.scatter(x_data,y_data)


with tf.Session() as sess:
    sess.run(init)
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data,keep_prob:0.8})
    for i in range(1000):

        sess.run(train_step,feed_dict={xs:x_data,ys:y_data,keep_prob:0.8})
        if i%50 == 0:
            print(sess.run(loss,feed_dict={xs:x_data,ys:y_data,keep_prob:1}))
