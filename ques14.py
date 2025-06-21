import numpy as np
a=np.random.randint(1,100,(3,3))
b=np.random.randint(1,100,(3,3))
print(a,b)
c=np.empty((3,3),dtype=bool)
for i in range(3):
    for j in range(3):
        if a[i][j]==b[i][j]:
            c[i][j]=True
        else:
            c[i][j]=False
print(c)
