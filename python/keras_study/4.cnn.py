import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Convolution2D, MaxPooling2D, Flatten
from keras.optimizers import SGD, Adam
from keras.regularizers import l2
from keras.models import load_model


(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape)
print(y_train.shape)
# (60000, 28, 28)  ==> (60000, 28, 28, 1)
# (60000,)
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0
# 更换成one hot 模式
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

# 定义顺序模型
model = Sequential()
# model = load_model("model.h5")

# 第一个卷积层
model.add(Convolution2D(
    input_shape = (28,28,1),
    filters = 32,
    kernel_size = 5,
    strides = 1,
    padding = 'same',
    activation = 'relu'   
))

# 第一个池化层
model.add(MaxPooling2D(
    pool_size = 2,
    strides = 2,
    padding = 'same'
))

# 第二个卷积层
model.add(Convolution2D(64, 5, strides=1, padding='same', activation='relu'))

# 第二个池化层
model.add(MaxPooling2D(pool_size=2, strides=2, padding='same'))

# 扁平化为1维
model.add(Flatten())

# 第一个全连接层
model.add(Dense(1024, activation='relu'))

model.add(Dropout(0.3))

model.add(Dense(10, activation='softmax'))

adam = Adam(lr = 1e-4)

model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=64, epochs=10)

loss, accuracy = model.evaluate(x_test, y_test)

print(loss, "   ", accuracy)

# model.save("model.h5")

"""
保存网络参数
model.save_weights('my_model.h5')
model.load_weights('my_model.h5')

保存网络结构
from keras.model import model_from_json
json_string = model.to_json()
mode = model_from_json(json_string)

pydot graphviz
"""

