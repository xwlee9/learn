import tensorflow as tf
import numpy as np

## saver
# W = tf.Variable([[1,2,3],[3,4,5]],dtype=tf.float32)
# b = tf.Variable([[1,2,3]],dtype=tf.float32)
#
# init = tf.global_variables_initializer()
#
# saver = tf.train.Saver()
#
# with tf.Session() as sess:
#     sess.run(init)
#     save_path = saver.save(sess,"saver/saver_net.ckpt")
#     print("Save to path:",save_path)



# ##############################
# tf.reset_default_graph()
W = tf.Variable(np.arange(6).reshape((2,3)),dtype = tf.float32)
b = tf.Variable(np.arange(3).reshape((1,3)),dtype = tf.float32)
# init = tf.global_variables_initializer()
saver = tf.train.Saver()
with tf.Session() as sess:
    # sess.run(init)
    save_path = "saver/saver_net.ckpt"
    saver.restore(sess = sess, save_path = "./saver/saver_net.ckpt")
    print("weight:",sess.run(W))
    print("biase:",sess.run(b))
saver.restore()
