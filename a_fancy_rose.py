
import numpy as np
import matplotlib.pyplot as plt

def hypot(A,B):
    C = np.sqrt(np.abs(A)** 2 + np.abs(B)**2)
    return C

m1=np.arange(0,1,0.01)
m2=np.arange(-0.6,20,0.01)
R,T=np.meshgrid(m1,m2)
x=1-(5/4*(1-np.mod(3.6*T,2))**2-1/4)**2/2
P=np.pi*np.exp(-T/8)/2
s=np.sin(P)
c=np.cos(P)
y=2*R**2*(1.3*R-1)**2*s
s2=x*(R*s+y*c)
x2=s2*np.sin(T*np.pi)
y2=s2*np.cos(T*np.pi)
z2=R*c-y*s

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init( azim=-127,elev=30)

#---- colors to plot---
c1=[1,0.3,0.3]
c1=np.repeat([c1],x2.shape[1],axis=0)
c1=np.repeat([c1],x2.shape[0],axis=0)
c2=hypot(hypot(x2,y2),z2*0.9)
cc=np.concatenate((c1,c2[:,:,np.newaxis]),axis=2)
#---Show the plot---
surf = ax.plot_surface(x2,y2,x*z2, rstride=1, cstride=1, facecolors=cc, antialiased=True)
plt.show()

