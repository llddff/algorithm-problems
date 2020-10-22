def best_goldmining(w,n,p,g):
    # w工人数量，n金矿数量，p每个金矿需要的人数列表，g每个金矿含金量列表
    if w==0 or n==0:
        return 0
    if w<p[n-1]:
        return best_goldmining(w,n-1,p,g)
    return max(best_goldmining(w,n-1,p,g),best_goldmining(w-p[n-1],n-1,p,g)+g[n-1])

import numpy as np
def best_goldmining_v2(w,p,g):
    # 非递归
    n=len(p)
    result_table=np.zeros((n+1,w+1))
    for i in range(1,n+1):
        for j in range(1,w+1):
            if j<p[i-1]:
                result_table[i,j]=result_table[i-1,j]
            else:
                result_table[i,j]=max(result_table[i-1,j],result_table[i-1][j-p[i-1]]+g[i-1])
    return result_table[-1,-1]


w=10
n=5
p=[5,5,3,4,3]
g=[400,500,200,300,350]
a=best_goldmining(w,n,p,g)
print(a)
b=best_goldmining_v2(w,p,g)
print(b)