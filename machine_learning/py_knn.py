# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
import statistics

import numpy as np
from networkx.classes import neighbors

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

# 通过皮尔逊算法相关系数判断相关性
print(np.corrcoef(x, y)[0, 1])


def predict_by_knn(history_data,param_in,k=5):
     """使用knn 算法做预测
        :history_data: 历史数据
        :param_in: 传入的代预测的数据
        :k: 取最靠近 param_in 值的k个数据的平均值
     """
     neighbors = heapq.nlargest(k, history_data,key= lambda x:(x-param_in)**2)
     return statistics.mean(history_data[neighbor] for neighbor in neighbors)

# 将历史数据一一对应 dict 形式
sample_data = {key: value for key, value in zip(x, y)}
print(type(sample_data))
incomes = [1800, 3500, 5200, 6600, 13400, 17800, 20000, 30000]
for income in incomes:
    print(f'月收入: {income:>5d}元, 月网购支出: {predict_by_knn(sample_data, income):>6.1f}元')
