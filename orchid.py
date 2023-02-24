
import numpy as np
import matplotlib.pyplot as plt

def cart2sph(x,y,z):
    azimuth = np.arctan2(y,x)
    elevation = np.arctan2(z,np.sqrt(x**2 + y**2))
    r = np.sqrt(x**2 + y**2 + z**2)
    return azimuth, elevation, r

def sph2cart(azimuth,elevation,r):
    x = r * np.cos(elevation) * np.cos(azimuth)
    y = r * np.cos(elevation) * np.sin(azimuth)
    z = r * np.sin(elevation)
    return x, y, z
def cool_color(N,rep,alpha):
    out=np.vstack((np.linspace(0,1,N),1-np.linspace(0,1,N),np.ones(N),np.ones(N)*alpha)).transpose()
    out=np.repeat(out[np.newaxis,:],rep,0)
    return out

a=np.arange(-np.pi,np.pi,0.02)
aa=a[np.newaxis,:]
S=np.random.random([315,315])
S[157,157]=-0.3
g=np.abs(np.fft.ifft2(S/np.abs(aa+1j*aa.transpose())**2.1))*2-3.1
g=g+g.transpose()
u,v,w=cart2sph(aa,aa.transpose(),np.pi)
x,y,z=sph2cart(u,v,w+g*2)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init( azim=-127,elev=30)

c=cool_color(315,315,0.8)

surf = ax.plot_surface(x,y,z, rstride=1, cstride=1, facecolors=c, antialiased=True)
surf2 = ax.plot_surface(x,-z,y, rstride=1, cstride=1, facecolors=c, antialiased=True)
surf3 = ax.plot_surface(-z,x,y, rstride=1, cstride=1, facecolors=c, antialiased=True)

#Show the plot
plt.show()
