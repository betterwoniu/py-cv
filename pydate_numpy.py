# !/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
import random
import statistics

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# 获取从0到100，并且每个数字之间的差值为3的数组
a1 = np.arange(0,100,3)
# print(a1)


e1 = np.eye(3,3,2,np.int8)
# print(e1)

array19 = np.arange(1, 10)
# array([1, 2, 5, 8, 9])
# print(array19[[True, True, False, False, True, False, False, True, True]]
# )
# print(array19)
array20 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# [[1 2 3]
#  [7 8 9]]
# print(array20[[0, 2]])

# [3 9]
# print(array20[[0,2],[2,2]])

# print(array20[[2,2],[1,1]])


# img = plt.imread('../bus.jpg')
# #
# plt.subplot(111),plt.imshow(img[:-2:])
# plt.show()


#
# print(img)
#
# print(img[::-1])

# a = np.array([
#     [[1,1,1],[2,2,2],[3,3,3]],
#     [[1,1,1],[2,2,2],[3,3,3]],
#     [[1,1,1],[2,2,2],[3,3,3]]
#
# ])
#
# b = np.ones((4,3,5),np.int8)
#
# print(b)

arr1 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
arr2 = np.array([[2, 4, 6],[8, 10, 2],[14, 16, 8]])
corr = np.corrcoef(arr1,arr2)

# 每月收入
x = [9558, 8835, 9313, 14990, 5564, 11227, 11806, 10242, 11999, 11630,
     6906, 13850, 7483, 8090, 9465, 9938, 11414, 3200, 10731, 19880,
     15500, 10343, 11100, 10020, 7587, 6120, 5386, 12038, 13360, 10885,
     17010, 9247, 13050, 6691, 7890, 9070, 16899, 8975, 8650, 9100,
     10990, 9184, 4811, 14890, 11313, 12547, 8300, 12400, 9853, 12890]
# 每月网购支出
y = [3171, 2183, 3091, 5928, 182, 4373, 5297, 3788, 5282, 4166,
     1674, 5045, 1617, 1707, 3096, 3407, 4674, 361, 3599, 6584,
     6356, 3859, 4519, 3352, 1634, 1032, 1106, 4951, 5309, 3800,
     5672, 2901, 5439, 1478, 1424, 2777, 5682, 2554, 2117, 2845,
     3867, 2962,  882, 5435, 4174, 4948, 2376, 4987, 3329, 5002]



def predict_by_knn(history_data,param_in,k=5):
      """用kNN算法做预测
         :param history_data: 历史数据
         :param param_in: 模型的输入
         :param k: 邻居数量（默认值为5）
         :return: 模型的输出（预测值）
      """
      # 选取最小的K个元素的key
      neighbors = heapq.nsmallest(k,history_data,key=lambda n: (n - param_in) ** 2)
      # statistics.mean 计算平均值
      return statistics.mean(history_data[neighbor] for neighbor in neighbors)

# xy 一一对应 组成dict
sample_data = {key: value for key, value in zip(x, y)}
# print(sample_data)
incomes = [1800, 3500, 5200, 6600, 13400, 17800, 20000, 30000]
# for income in incomes:
    # print(f'月收入: {income:>5d}元, 月网购支出: {predict_by_knn(sample_data, income):>6.1f}元')



# 计算损失函数 y = ax+b
#
# def get_loss(xarr,yarr,_ap,_bp):
#      y_hat = [_ap * n + _bp for n in xarr]
#
#      return statistics.mean([ (k1-k2)**2 for k1,k2 in zip(y_hat,yarr)])
#
# # 先将最小损失定义为一个很大的值
# min_loss, a, b = 1e12, 0, 0
#
# for _ in range(100000):
#      _a,_b = random.random(), random.random() * 4000 - 2000
#
#      # 通过随机的a,b 值计算出每一个x 对应的y
#      # y_hat = [_a*_x+_b for _x in x]
#      # cur_loss = statistics.mean([ (k1-k2) **2 for k1,k2 in zip(y_hat,y)])
#      # MSE = 270723.22687905433
#      # a = 0.48203845695089886, b = -1521.5453648697367
#      # MSE = 270715.3752519053
#      # a = 0.4803793705744913, b = -1494.516347967695
#
#      cur_loss = get_loss(x,y,_a,_b)
#      if cur_loss < min_loss:
#           min_loss = cur_loss
#           a,b = _a,_b
#      # MSE = 277268.64563178323
#      # a = 0.45774111904272896, b = -232.45296237879393
#      # MSE = 295504.1990069838
#      # a = 0.44919170092641314, b = 1426.078985087347
#
# print(f'MSE = {min_loss}')
# print(f'{a = }, {b = }')



x_bar, y_bar = np.mean(x), np.mean(y)
a = np.dot((x - x_bar), (y - y_bar)) / np.sum((x - x_bar) ** 2)
b = y_bar - a * x_bar
print(f'{a = }, {b = }')