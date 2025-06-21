import numpy as np
a = np.array([[45, 60], [30, 80]])
print(a)
for i in range(2):
    for j in range(2):
        if a[i][j]>50:
            a[i][j]=100
print(a)
m1=(a[0][0]+a[1][0])/2
m2=(a[0][1]+a[1][1])/2
print(m1,m2)
