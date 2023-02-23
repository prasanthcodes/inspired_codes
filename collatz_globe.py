
import numpy as np
import matplotlib.pyplot as plt

def fun1(n):
    return ((n%2)*(2*n+1)+n)/2

plt.figure()
ax = plt.axes()
ax.set_facecolor("black")
for i in range(3,9000,5):
    a=[]
    a.insert(0,i)
    while a[0]>1:
        a.insert(0,fun1(a[0]))
    t=np.array(a)
    t=(t%2)*0.3-0.2
    t=np.cumsum(t)
    x=1
    plt.plot(x*np.cumsum(np.sin(t))/6+x,x*np.cumsum(np.cos(t))/6+x,color="white",alpha=0.1)
    x = -1
    plt.plot(x * np.cumsum(np.sin(t)) / 6 + x, x * np.cumsum(np.cos(t)) / 6 + x,color="white",alpha=0.1)

plt.scatter([0,.1,.5],[0,.1,.7],np.array([8,7,1])*2e3,[[.8,.8,.3],[1,1,.5],[1,1,1]],'.')
# plt.axis('off')
ax.set_facecolor("black")
plt.show()