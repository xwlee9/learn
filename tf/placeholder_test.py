import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)


output = tf.multiply(input1,input2)
with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.0]}))

# 在运行的时候，再给输入值的 由feed_dict 给出 
