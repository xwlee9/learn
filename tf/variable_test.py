import tensorflow as tf
stat = tf.Variable(0,name='counter')

one = tf.constant(1)

new_value = tf.add(stat,one)
update = tf.assign(stat,new_value)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for i in range(3):
        sess.run(update)
        print(sess.run(stat))
