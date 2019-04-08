import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import  Sequential
from keras.layers import  Dense,Activation
from keras.optimizers import RMSprop

np.random.seed(123)
# X (6,000 28*28) Y (10,000, )
(X_train,Y_train),(X_test,Y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0],-1)/255
X_test = X_test.reshape(X_test.shape[0],-1)/255
Y_train = np_utils.to_categorical(Y_train,num_classes=10) ### one hot
Y_test = np_utils.to_categorical(Y_test,num_classes=10) ### 0000000001 ===>9

model = Sequential([
    Dense(32,input_dim=784),
    Activation('relu'),
    Dense(10),
    Activation('softmax')
    ])

rmsprop = RMSprop(lr=0.001,rho =0.9,epsilon=1e-08,decay=0.0)

model.compile(
    optimizer=rmsprop,loss='categorical_crossentropy',metrics=['accuracy'] )

print('training---------------------------------------------')
model.fit(X_train,Y_train,epochs=2,batch_size=32)

loss,accuracy=model.evaluate(X_test,Y_test)
print(loss)
print(accuracy)
