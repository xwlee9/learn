import numpy as np
from keras.datasets import mnist
from keras.models import Model
from keras.layers import Dense,Input
import matplotlib.pyplot as plt

np.random.seed(123)

(X_train,_),(X_test,Y_test) = mnist.load_data()

X_train = X_train.astype('float32')/255 - 0.5
X_test = X_test.astype('float32')/255 - 0.5
X_train = X_train.reshape((X_train.shape[0],-1))
X_test = X_test.reshape((X_test.shape[0],-1))
# #(60000, 784)
# print (X_train.shape)
# #(10000, 784)
# print (X_test.shape)

encoding_dim = 2

input_img = Input(shape=(784,))

encoded = Dense(128,activation='relu')(input_img)
encoded = Dense(64,activation='relu')(encoded)
encoded = Dense(16,activation='relu')(encoded)
encoder_output = Dense(encoding_dim)(encoded)

decoded = Dense(16,activation = 'relu')(encoder_output)
decoded = Dense(64,activation = 'relu')(decoded)
decoded = Dense(128,activation = 'relu')(decoded)
decoded = Dense(784,activation = 'tanh')(decoded)

autoencoder = Model(inputs=input_img,outputs=decoded)
# only inputs ===> input_dim=2
encoder = Model(inputs = input_img,outputs = encoder_output)

autoencoder.compile(optimizer='adam',loss='mse')

autoencoder.fit(X_train,X_train,batch_size=256,epochs=20,shuffle=True)

enconded_imgs = encoder.predict(X_test)
plt.scatter(encoded_imgs[:,0],encoded_imgs[:,1],c=Y_test)
plt.show()
