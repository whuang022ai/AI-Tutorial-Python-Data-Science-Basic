# -*- coding: utf-8 -*-

#  @about 一個numpy簡易使用範例

#  @auth whuang022ai

#  引用numpy
import numpy as np
#  直接設定矩陣數值
m1 = np.mat([[1, 3, 5], [2, 4, 6]])
m2 = np.mat([[-1, 2, 4], [3, 3, 3]])
#  亂數設定矩陣數值
m3 = np.random.rand(3, 3)
#  矩陣加法
m4 = m1+m2
#  從csv讀取數值資料
m5 = np.genfromtxt('dataTest.csv', delimiter=',')
m6 = np.mat([[9, 2, 4], [3, 11, -4]])
#  矩陣所有元素和
sum1 = np.sum(m1)
#  矩陣所有元素平均
avg1 = np.mean(m1)
#  矩陣所有元素標準差
var1 = np.var(m1)
#  矩陣橫的資料排序
m7 = np.sort(m6)
# 偵測異常值
m8 = np.array([1.0, 1.5, 8.5, 7.7, 1.2, -7.7, -2.1, 200.0, -200.0])
q1 = np.percentile(m8, 25)
q3 = np.percentile(m8, 75)
iqr = q3-q1
low = q1-1.5*iqr
up = q3+1.5*iqr
for i in range(9):
    if m8[i] > up or m8[i] < low:
        print('outlier:')
        print(m8[i])
#  印出來觀察
print(m1)
print(m2)
print(m4)
print(m5)
print(m6)
print(m7)
print(sum1)
print(avg1)
print(var1)
print(q1)
print(q3)
print(iqr)
