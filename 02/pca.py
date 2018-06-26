# -*- encoding = utf-8 -*-
# -*- coding: utf-8 -*-

'''
    一個PCA降維範例
    @author whuang022

'''

from sklearn.decomposition import PCA

import numpy as np 

X = np.array([[-1, -1], [-2, -1],[-3, -2],  [ 1,  1], [ 2,  1], [ 3,  2]])
pca = PCA(n_components=1)
newX = pca.fit_transform(X)
print(newX)
