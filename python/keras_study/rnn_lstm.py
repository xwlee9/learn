import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM,TimeDistributed,Dense
from keras.optimizers import Adam

BATCH_START = 0
TIME_STEP = 20
BATCH_SIZE = 50
INPUT_SIZE = 1
OUTPUT_SIZE = 1
CELL_SIZE = 20
LR = 0.006

np.random.seed(123)

def get_batch():
    global BATCH_START,TIME_STEP
    xs = np.arange(BATCH_START,BATCH_START+TIME_STEP*BATCH_SIZE).reshape((BATCH_SIZE,TIME_STEP))/(10*np.pi)
    seq = np.sin(xs)
    res = np.cos(xs)
    BATCH_START += TIME_STEP
    return [seq[:,:,np.newaxis],res[:,:,np.newaxis],xs]

model = Sequential()
model.add(LSTM(batch_input_shape=(BATCH_SIZE,TIME_STEP,INPUT_SIZE),units=CELL_SIZE,
                return_sequences = True,stateful=True)) #return_sequences 每个都返回
                # statuful 每个batch是否有联系

model.add(TimeDistributed(Dense(OUTPUT_SIZE)))

adam =Adam(LR)

model.compile(optimizer=adam,loss='mse')

print('training------------------------------------------')
for step in range(501):
    X_batch,Y_batch,xs=get_batch()
    cost = model.train_on_batch(X_batch,Y_batch)
    pred = model.predict(X_batch,BATCH_SIZE)
    plt.plot(xs[0,:],Y_batch[0].flatten(),'r',xs[0,:],pred.flatten()[:TIME_STEP],'b--')
    plt.ylim((-1.2,1.2))
    plt.draw()
    plt.pause(0.5)
    if step % 10 == 0:
        print("train cost is :", cost)
