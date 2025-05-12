# !usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris
import numpy as np
from sklearn.model_selection import train_test_split

iris = load_iris()
x_data,y_data = iris.data,iris.target
x, X_test, y, y_test = train_test_split(x_data, y_data, train_size=0.1, random_state=3)



def kmeans(X, *, k, max_iter=10, tol=1e-4):
    centroids = init_centroids(X, k)
    # print(centroids)
    for _ in range(max_iter):
        # 通过质心将数据划分到不同的簇
        clusters = build_clusters(X,centroids)
        # 重新计算新的质心的位置
        new_centroids = update_centroids(X, clusters)
        # 如果质心几乎没有变化就提前终止迭代
        if np.allclose(new_centroids, centroids, rtol=tol):
            break
        # 记录新的质心的位置
        centroids = new_centroids
    return make_label(X, clusters), centroids

def distance(u, v, p=2):
    """计算两个向量的距离"""
    return np.sum(np.abs(u - v) ** p) ** (1 / p)

def init_centroids(X,k):
    """
     随机选择k个质心
    :param X: 元数据
    :param k:
    :return:
    """
    # np.random.choice 传入的是数组或者整数
    index = np.random.choice(np.arange(len(X)), k,replace=False)
    return X[index]

def closest_centroid(sample, centroids):
    """找到跟样本最近的质心"""
    distances =[]
    for i, centroid in enumerate(centroids):
        d = distance(sample, centroid)
        distances.append(d)

    return np.argmin(distances)  # 返回其中最近，最小的质心的下标

def build_clusters(X,centroids):
    """根据质心将数据分成簇"""
    clusters = [[] for _ in range(len(centroids))]
    for i, sample in enumerate(X):
        centroid_index = closest_centroid(sample, centroids)
        clusters[centroid_index].append(i)
    return clusters


def update_centroids(X, clusters):
    """更新质心的位置"""
    xc_list = []
    for i, cluster in enumerate(clusters):
        xc = X[cluster]
        d = np.mean(xc, axis=0)
        xc_list.append(d)
    return np.array(xc_list)
def make_label(X, clusters):
    """生成标签"""
    labels = np.zeros(len(X))
    for i, cluster in enumerate(clusters):
        for j in cluster:
            labels[j] = i
    return labels

kmeans(x, k=3)