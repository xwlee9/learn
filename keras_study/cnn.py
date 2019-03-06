import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Activation,Convolution2D,MaxPooling2D,Flatten
from keras.optimizers import Adam

np.random.seed(123)
# X (6,000 28*28) Y (10,000, )
(X_train,Y_train),(X_test,Y_test) = mnist.load_data()

X_train = X_train.reshape(-1,1,28,28)
X_test = X_test.reshape(-1,1,28,28)
Y_train = np_utils.to_categorical(Y_train,num_classes=10) ### one hot
Y_test = np_utils.to_categorical(Y_test,num_classes=10) ### 0000000001 ===>9

model = Sequential()

model.add(Convolution2D(filters=32,
                        kernel_size=(5,5),
                        padding ='same',
                        input_shape=(1,28,28)))
model.add(Activation('relu'))
model.add(MaxPooling2D(
        pool_size=(2,2),
        strides = (2,2),
        padding = 'same'))

model.add(Convolution2D(64,(5,5),padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(
                pool_size=(2,2),
                strides = (2,2),
                padding = 'same'))

model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))

adam = Adam(lr=0.0001)

model.compile(optimizer=adam,
            loss='categorical_crossentropy',
            metrics=['accuracy'])

print('training-------------------------------')
model.fit(X_train,Y_train,batch_size=32,epochs=1)

print('testing ---------------------------------')
loss,accuracy = model.evaluate(X_test,Y_test)

print('\ntest loss:',loss)
print('\ntest accuracy:',accuracy)
