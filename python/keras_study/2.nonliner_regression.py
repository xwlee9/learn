import keras 
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential  # 按照顺序构成的模型
from keras.layers import Dense,Activation  # 全连接层
from keras.optimizers import SGD

x_data = np.linspace(-0.5, 0.5, 200)
noise = np.random.normal(0, 0.02, x_data.shape)
y_data = np.square(x_data) + noise

# plt.scatter(x_data, y_data)
# plt.show()

model = Sequential()
model.add(Dense(units=10, input_dim=1, activation='relu'))
# model.add(Activation('tanh'))
model.add(Dense(units=1, activation='relu'))
# model.add(Activation('tanh'))
model.compile(optimizer='sgd', loss='mse')

sgd = SGD(lr=0.3)
model.compile(optimizer=sgd, loss='mse')

for step in range(3001): 
    cost = model.train_on_batch(x_data, y_data)
    if step % 500 == 0:
        print('cost:', cost)

# 权值 偏置值
W,b = model.layers[0].get_weights()
print('W:', W, 'b:', b)

# x_data输入到网络中， 得到预测值y_pred
y_pred = model.predict(x_data)

# 现实随机点
plt.scatter(x_data, y_data)
plt.plot(x_data, y_pred, 'r-')
plt.show()