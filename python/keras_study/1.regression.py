import keras 
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential  # 按照顺序构成的模型
from keras.layers import Dense  # 全连接层


# 使用numpy生成100个随机的点
x_data = np.random.rand(100);
noise = np.random.normal(0, 0.01, x_data.shape)
y_data = x_data * 0.1 + 0.2 + noise

# 显示随机点
# plt.scatter(x_data, y_data)
# plt.show()

# 构建一个顺序模型
model = Sequential()
model.add(Dense(units=1, input_dim=1))
model.compile(optimizer='sgd', loss='mse')

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