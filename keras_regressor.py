from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-1,1,200)
np.random.shuffle(X)

Y = 0.5*X+2+np.random.normal(0,0.05,(200,))

# plt.scatter(X,Y)
# plt.show()

X_train,Y_train = X[:160],Y[:160]
X_test ,Y_test =X[160:],Y[160:]

model = Sequential()
model.add(Dense(units=1,input_dim=1))
model.compile(loss='mse',optimizer='sgd')
print('training-----------------')
for step in range(301):
    cost = model.train_on_batch(X_train,Y_train)
    if step%100 == 0:
        print('cost is :',cost)
print('testing----------------------')
cost = model.evaluate(X_test,Y_test,batch_size=40)
print('test cost',cost)
W,b = model.layers[0].get_weights()
print('the weight is:',W ,'the biase is :',b)

Y_pred = model.predict(X_test)
plt.scatter(X_test,Y_test)
plt.plot(X_test,Y_pred)
plt.show()
