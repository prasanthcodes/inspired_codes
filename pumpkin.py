
import numpy as np
import matplotlib.pyplot as plt

def sphere(n):
    theta = (np.arange(-n,n,2)/n)*np.pi
    phi = (np.arange(-n,n,2)/n)*(np.pi/2)
    theta=theta[np.newaxis,:]
    phi=phi[:,np.newaxis]
    cosphi = np.cos(phi)
    cosphi[0,0] = 0
    cosphi[n-1,0] = 0
    sintheta = np.sin(theta)
    sintheta[0,0] = 0
    sintheta[0,n-1] = 0

    x = cosphi*np.cos(theta)
    y = cosphi*sintheta
    z = np.ones([1,n])*np.sin(phi)
    return x,y,z
def cool_colormap(N,rep,alpha):
    out=np.vstack((np.linspace(0,1,N),1-np.linspace(0,1,N),np.ones(N),np.ones(N)*alpha)).transpose()
    out=np.repeat(out[np.newaxis,:],rep,0)
    return out

x1,y1,z1=sphere(160)
R=1+(-1*(1-np.mod(np.arange(0,16,0.1),2))**2)/40+(-1*(1-np.mod(np.arange(0,32,0.2),2))**2)/40
x=R*x1
y=R*y1
z=R*1.2*z1*(0.8+(0-(np.arange(1,-1,-0.0125)**4))*0.3)

xx=x1/15
yy=y1/15
zz=(z1/2)+0.6

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init( azim=-37,elev=11)

#---- colors to plot---
c1=[0.9297,    0.3984,         0]
c1=np.repeat([c1],161,axis=0)
c1=np.repeat([c1],161,axis=0)
c2=[0,0.2656,0]
c2=np.repeat([c2],161,axis=0)
c2=np.repeat([c2],161,axis=0)

#---plot ---
surf = ax.plot_surface(x,y,z, rstride=1, cstride=1, facecolors=c1, antialiased=True)
surf2 = ax.plot_surface(xx,yy,zz, rstride=1, cstride=1, facecolors=c2, antialiased=True)

#Show the plot
plt.show()
