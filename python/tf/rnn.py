import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data',one_hot = True)

lr = 0.001
traing_iters = 100000
batch_size = 128

n_inputs = 28 # each row has 28 collum
n_step = 28
n_hidden_unis = 128
n_classes = 10

#tf Grapg input
x = tf.placeholder(tf.float32,[None,n_step,n_input])
y = tf.placeholder(tf.float32,[None,n_classes])

#Define weight
weights = {
    'in':tf.Variable(tf.random_normal([n_input,n_hidden_unis]))
    'out':tf.Variable(tf.random_normal([n_hidden_unis,n_classes]))
}
biases = {
    'in': tf.Variable(tf.constant(0.1,shape=[n_hidden_unis,]))
    'out': tf.Variable(tf.constant(0.1,shape=[n_classes,])
}

def RNN(X,weights,biases):
# X(128batch,28step,28inputs)==>(128*28,28)
    X = tf.reshape(X,[-1,n_inputs])
    # ==>(128*28,128hidden)
    X_in = tf.matmul(X,weights['in'])+biases['in']
    # ==>(128,28,128)
    X_in = tf.reshape(X_in,[-1,n_step,n_hidden_unis])

# cell
    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden_unis,forget_bias=1,state_is_tuple=True)
    # lstm cell is divided into 2 parts(c_state,m_state) ==> states
    __init__state = lstm_cell.zero_state(batch_size,dtype=tf.float32)

    outputs,states = tf.nn.dynamic_rnn(lstm_cell,X_in,initial_state=__init__state,time_major=False)
    # X_in step 维度 time_major 是不是第一个 ???

# hidden layer for outputs as final result
    result = tf.matmul(states[1],weights['out']) + biases['out']

# OR
    # outputs = tf.unstack(tf.transpose(outputs,[1,0,2]))
    # result = tf.matmul(outputs[-1],weights['out'])+biases['out']

    return result




pred = RNN(x,weights,biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred,y))
train_op = tf.train.AdamOptimizer(lr).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred,1).tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred,tf.float32))

init = global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    step = 0
    while step*batch_size < training_iters:
        batch_xs,batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape([batch_size,n_step,n_inputs])
        sess.run([train_op],feed_dict={x:batch_xs,y:batch_ys})
        if step%20 == 0:
            print(sess.run(accuracy,feed_dict{x:batch_xs,y:batch_ys}))
        step += 1
