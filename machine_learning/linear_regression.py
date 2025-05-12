# !usr/bin/env python3
# -*- coding: utf-8 -*-
# 每月收入
import random
import statistics
import numpy as np
from numpy.polynomial import Polynomial


X = [9558, 8835, 9313, 14990, 5564, 11227, 11806, 10242, 11999, 11630,
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

def get_loss(_a,_b,data):
    """
     损失函数 通过模拟 y= a*x +b 函数 中的a和b; 通过代入历史数据来计算 均方误差
    """
    y_hat = [_a * n + _b for n in data.keys()]
    return statistics.mean([(v1-v2) **2 for v1,v2 in zip(data.values(),y_hat)])


# 先将最小损失定义为一个很大的值
min_loss, a, b = 1e12, 0, 0
sample_data = {key: value for key, value in zip(X, y)}

for _ in range(10000):
    _a, _b = random.random(), random.random() * 4000 - 2000
    cur_loss = get_loss(_a, _b, sample_data)
    if cur_loss < min_loss:
        min_loss = cur_loss
        a,b = _a,_b

print(f'MSE = {min_loss}')
print(f'{a = }, {b = }')

# a, b = np.polyfit(X, y, deg=1)
# print(f'{a = }, {b = }')
#
# b, a = Polynomial.fit(X, y, deg=1).convert().coef
# print(f'{a = }, {b = }')
