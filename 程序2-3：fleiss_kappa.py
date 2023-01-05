# -*- coding: utf-8 -*-
"""
演示内容：fleiss_kappa的计算（用于衡量多个评价者之间的一致性）
"""
import numpy as np  
def fleiss_kappa(testData, N, k, n): 
    dataMat = np.mat(testData, float)  
    oneMat = np.ones((k, 1))  
    sum = 0.0  
    P0 = 0.0  
    for i in range(N):  
        temp = 0.0  
        for j in range(k):  
            sum += dataMat[i, j]  
            temp += 1.0*dataMat[i, j]**2  
        temp -= n  
        temp /= (n-1)*n  
        P0 += temp  
    P0 = 1.0*P0/N  
    ysum = np.sum(dataMat, axis=0)  
    for i in range(k):  
        ysum[0, i] = (ysum[0, i]/sum)**2  
    Pe = ysum*oneMat*1.0  
    ans = (P0-Pe)/(1-Pe)  
    return ans[0, 0]  
  

ratingdata = [[0, 0, 0, 0, 14],  
                [0, 2, 6, 4, 2],  
                [0, 0, 3, 5, 6],  
                [0, 3, 9, 2, 0],  
                [2, 2, 8, 1, 1],  
                [7, 7, 0, 0, 0],  
                [3, 2, 6, 3, 0],  
                [2, 5, 3, 2, 2],  
                [6, 5, 2, 1, 0],  
                [0, 2, 2, 3, 7]]  
    
f_kappa = fleiss_kappa(ratingdata, 10, 5, 14)  
print ("fleiss_kappa value:", f_kappa)