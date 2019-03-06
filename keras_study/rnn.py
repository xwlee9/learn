import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Activation,SimpleRNN
from keras.optimizers import Adam

TIME_STEP = 28
INPUT_SIZE = 28
BATCH_SIZE = 50
BATCH_INDEX = 0
OUTPUT_SIZE =10
CELL_SIZE = 50
LR =0.001

np.random.seed(123)
 # X (6,000 28*28) Y (10,000, )
(X_train,Y_train),(X_test,Y_test) = mnist.load_data()

X_train = X_train.reshape(-1,28,28)/255
X_test = X_test.reshape(-1,28,28)/255
Y_train = np_utils.to_categorical(Y_train,num_classes=10) ### one hot
Y_test = np_utils.to_categorical(Y_test,num_classes=10) ### 0000000001 ===>9

model = Sequential()

 #RNN CELL

model.add(SimpleRNN(batch_input_shape=(BATCH_SIZE,TIME_STEP,INPUT_SIZE),units=CELL_SIZE)) # 50 28 28==》 3d

model.add(Dense(OUTPUT_SIZE))
model.add(Activation('softmax'))

adam = Adam(LR)
model.compile(optimizer=adam,loss='categorical_crossentropy',metrics=['accuracy'])

for step in range(4001):
    X_batch = X_train[BATCH_INDEX:BATCH_INDEX+BATCH_SIZE,:,:]
    Y_batch = Y_train[BATCH_INDEX:BATCH_INDEX+BATCH_SIZE,:]
    cost = model.train_on_batch(X_batch,Y_batch) # train_on_batch：本函数在一个batch的数据上
                                                # 进行一次参数更新，函数返回训练误差的标量值或标量值的list，

    BATCH_INDEX += BATCH_SIZE
    BATCH_INDEX = 0 if BATCH_SIZE >= X_train.shape[0] else BATCH_INDEX
    # print(Y_test.shape[0],'\n',X_test.shape[0])
    if step%500 ==0:
        cost,accuracy=model.evaluate(X_test,Y_test,batch_size=BATCH_SIZE,verbose=False)
        print('\ntest cost:',cost,'\n accuracy:',accuracy)
