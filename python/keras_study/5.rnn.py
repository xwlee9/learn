import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.layers.recurrent import SimpleRNN  # LSTM RGU
from keras.optimizers import SGD, Adam

# 数组长度一行为28个像素
input_size = 28

# 序列长度有28行
time_step = 28

# 隐藏层cell的个数
cell_size = 50

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

# one hot
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

model = Sequential()

model.add(SimpleRNN(units=cell_size, input_shape=(time_step, input_size),))

model.add(Dense(10, activation='softmax'))

adam = Adam(lr = 1e-4)
  
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=64, epochs=10)

loss, accuracy = model.evaluate(x_test, y_test)

print(loss, "   ", accuracy)