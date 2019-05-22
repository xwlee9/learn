import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD, Adam
from keras.regularizers import l2


(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape)
print(y_train.shape)
# (60000, 28, 28)  ==>(60000, 784)
# (60000,)
x_train = x_train.reshape(x_train.shape[0], -1) / 255
x_test = x_test.reshape(x_test.shape[0], -1) / 255
# 更换成one hot 模式
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

# 创建模型 输入784个神经元 输出10个神经元
model = Sequential([
    Dense(units=200, input_dim=784, bias_initializer='one', activation='tanh', kernel_regularizer=l2(0.0002)),
    Dropout(0.3),
    Dense(units=100, bias_initializer='one', activation='tanh', kernel_regularizer=l2(0.0002)),
    Dropout(0.3),
    Dense(units=10, bias_initializer='one', activation='softmax', kernel_regularizer=l2(0.0002))
    ])

sgd = SGD(lr=0.2)
adam = Adam(lr=0.001)
# 定义优化器 loss function 以及训练过程中计算准确率
# model.compile(optimizer=sgd, loss='mse', metrics=['accuracy'])
# model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])


# 训练模型
model.fit(x_train, y_train, batch_size=32, epochs=10)

# 评估模型
loss, accuracy = model.evaluate(x_test, y_test)
print ('\ntest loss', loss)
print ('accuracy', accuracy)

train_loss, train_accuracy = model.evaluate(x_train, y_train)
print ('\ntrain loss', train_loss)
print ('train accuracy', train_accuracy)