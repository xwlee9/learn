import tensorflow as tf
import numpy as np

x=tf.placeholder("float")
y=tf.placeholder("float")
w=tf.Variable([1.0,2.0],name='w')
y_pred=tf.multiply(x,w[0])+w[1]
error=tf.square(y-y_pred)

train_op=tf.train.GradientDescentOptimizer(0.02).minimize(error)
model=tf.initialize_all_variables()

with tf.Session() as session:
    session.run(model)
    for i in range(1000):
        x_value=np.random.rand()
        y_value=x_value*2+6
        session.run([train_op],feed_dict={x:x_value,y:y_value})

    w_value=session.run(w)# get w
    print ("ax+b,a=%.3f,b=%.3f"%(w_value[0],w_value[1]))
