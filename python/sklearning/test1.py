import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt


iris = datasets.load_iris()
iris_X = iris.data
iris_Y = iris.target

# print(iris_X[:2,:])
# print(iris_Y)

# X_train,X_test,Y_train,Y_test = train_test_split(iris_X,iris_Y,test_size=0.3)
#
# # print(Y_train)
#
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train,Y_train)
# # print(knn.predict(X_test))
# # print(Y_test)
# print(knn.score(X_test,Y_test))

#######################################################
# knn = KNeighborsClassifier(n_neighbors=5)
# scores = cross_val_score(knn,iris_X,iris_Y,cv=5,scoring='accuracy') ## cv ==> 5set
# print (scores.mean())
#######################################################
k_range = range(1,31)
k_score = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,iris_X,iris_Y,cv=10,scoring='accuracy') # calssification
    loss =-cross_val_score(knn,iris_X,iris_Y,cv=10,scoring='neg_mean_squared_error')    # regression
    k_score.append(loss.mean())

plt.plot(k_range,k_score)
plt.xlabel('value of k for knn')
plt.ylabel('cross_validated accuracy')
plt.show()
