# !usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy import stats
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target


# # 数据集划分
# data = np.hstack((X, y.reshape(-1, 1)))
# # 打乱顺序
# np.random.shuffle(data)
# train_size = int(y.size * 0.8)
# train, test = data[:train_size], data[train_size:]
# X_train, y_train  = train[:, :-1], train[:, -1]
# X_test, y_test = test[:, :-1], test[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=3)


def euclidean_distance(i1,i2):
    return np.sqrt(np.sum((i1-i2)**2))


def euclidean_distance2(u, v):
    return np.sqrt(np.sum(np.abs(u - v) ** 2))

def make_label(x_data, y_data,xt_one,k):
  distances = np.array([euclidean_distance(a1,xt_one) for a1 in x_data])
  # 通过一次划分找到k个最小距离对应的索引并获取到相应的标签
  labels = y_train[np.argpartition(distances, k - 1)[:k]]
  # 获取标签的众数
  return stats.mode(labels).mode

# print(np.array([make_label(X_train, y_train, X, 5) for X in X_test]) == y_test)


model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(y_pred == y_test)

print(model.score(X_test, y_test))



