import numpy as np
import matplotlib.pyplot as plt

def cool_colormap(m):
    r=np.arange(0,m,1)/np.max([m-1,1])
    g=1-r
    b=np.ones(m)
    rgb = np.vstack((r, g, b)).transpose()
    return rgb
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)
def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)
def normalize_data(data):
    return ((data-np.min(data))/(np.max(data)-np.min(data)))

a=716
v=255
x=np.linspace(10,-10,a)
c=np.flipud(cool_colormap(256))
c[:,2]=np.linspace(1,0.2,v+1)
c[0,:]=[0,0,0]
x1,y1=np.meshgrid(x,x[np.newaxis,:].transpose()-10)
r,t=cart2pol(x,x[np.newaxis,:].transpose())
y1[y1<(0.05*(x1+np.random.random(a))**2)-15]=0
f=np.zeros([a,a])
im1=-1*normalize_data(y1)*v
im2=y1*np.abs(np.fft.ifft2(r**-2.2*np.cos(7*np.random.random([a,a]))))
im2=normalize_data(im2)

img=im1
sz=img.shape
#---apply colors to the pixels---
normalized_img=((img.flatten()-np.min(img))/(np.max(img)-np.min(img)))
idx=np.round((c.shape[0]-1)*normalized_img).astype(np.int)
idx[idx<0]=0
img=c[idx].reshape([sz[0],sz[1],3])
img=np.concatenate((img,im2[:,:,np.newaxis]),axis=2)#add alpha channel
plt.imshow(img)
plt.show()

