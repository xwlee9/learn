# from sklearn.model_selection import learning_curve
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
X = digits.data
Y = digits.target
param_range = np.logspace(-6,-2.3,5)
# train_sizes,train_loss,test_loss = learning_curve(SVC(gamma=0.001),X,Y,cv=10,
#                                     scoring='neg_mean_squared_error',
#                                     train_sizes=[0.1,0.25,0.5,0.75,1])
train_loss,test_loss = validation_curve(SVC(),X,Y,cv=10,param_name='gamma',
                                    param_range=param_range,
                                    scoring='neg_mean_squared_error',)
train_loss_mean = -np.mean(train_loss,axis=1)
test_loss_mean = -np.mean(test_loss,axis=1)

plt.plot(param_range,train_loss_mean,'o-',color="r",label ="training")
plt.plot(param_range,test_loss_mean,'o-',color="g",label ="cross_validation")
# plt.plot(train_sizes,train_loss_mean,'o-',color="r",label ="training")
# plt.plot(train_sizes,test_loss_mean,'o-',color="g",label ="cross_validation")
plt.xlabel("training examples")
plt.ylabel("loss")
plt.legend(loc='best')
plt.show()
