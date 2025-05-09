import numpy as np
from sklearn.datasets import load_iris
from scipy import stats
# 加载鸢尾花数据集
iris = load_iris()
# 查看数据集的介绍
# print(iris.DESCR)

# 特征（150行4列的二维数组，分别是花萼长、花萼宽、花瓣长、花瓣宽）
x = iris.data
# 标签（150个元素的一维数组，包含0、1、2三个值分别代表三种鸢尾花）
y = iris.target

data = np.hstack((x,y.reshape(-1,1)))
np.random.shuffle(data)
train_size = int(y.size*0.8)
train,test = data[:train_size],data[train_size:]
X_train, y_train = train[:, :-1], train[:, -1]
X_test, y_test = test[:, :-1], test[:, -1]
print('debug')

def euclidean_distance(u, v):
    """计算两个n维向量的欧式距离"""
    return np.sqrt(np.sum(np.abs(u - v) ** 2))

def make_label(X_train, y_train, X_one, k):
    """
    根据历史数据中k个最近邻为新数据生成标签
    :param X_train: 训练集中的特征
    :param y_train: 训练集中的标签
    :param X_one: 待预测的样本（新数据）特征
    :param k: 邻居的数量
    :return: 为待预测样本生成的标签（邻居标签的众数）
    """
    # 计算x跟每个训练样本的距离
    distes = [euclidean_distance(X_one, X_i) for X_i in X_train]
    # 通过一次划分找到k个最小距离对应的索引并获取到相应的标签
    labels = y_train[np.argpartition(distes, k - 1)[:k]]
    # 获取标签的众数
    return stats.mode(labels).mode

def predict_by_knn(X_train, y_train, X_new, k=5):
    """
        KNN算法
        :param X_train: 训练集中的特征
        :param y_train: 训练集中的标签
        :param X_new: 待预测的样本构成的数组
        :param k: 邻居的数量（默认值为5）
        :return: 保存预测结果（标签）的数组
    """
    arr = []
    for X in X_new:
        r = make_label(X_train, y_train, X, k)
        arr.append(r)

    return np.array(arr)

y_pred = predict_by_knn(X_train, y_train, X_test)
y_pred == y_test

# [0. 2. 1. 2. 1. 0. 0. 2. 1. 0. 1. 2. 1. 0. 2. 2. 0. 0. 2. 1. 2. 2. 0. 2.
#  0. 2. 2. 2. 1. 1.]
print(y_pred)