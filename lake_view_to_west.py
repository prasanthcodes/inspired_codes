import numpy as np
import matplotlib.pyplot as plt

def gray_colormap(m):
    v=np.arange(0,m,1)/np.max([m-1,1])
    rgb = np.repeat(v[:, np.newaxis], 3, 1)
    return rgb

def hot_colormap(m):
    n=int(np.floor((3.0/8.0)*m))
    r=np.hstack((np.arange(1,n+1)/n,np.ones(m-n)))
    g=np.hstack((np.zeros(n),np.arange(1,n+1)/n,np.ones(m-2*n)))
    b=np.hstack((np.zeros(2*n),np.arange(1,m-2*n+1)/(m-2*n)))
    rgb = np.vstack((r, g, b)).transpose()
    return rgb
def pink_colormap(m):
    rgb=np.sqrt((2*gray_colormap(m)+hot_colormap(m))/3)
    return rgb
def autumn_colormap(m):
    r=np.ones(m)
    g = np.arange(0, m, 1) / np.max([m - 1, 1])
    b=np.zeros(m)
    rgb = np.vstack((r, g, b)).transpose()
    return rgb
def normalize_data(data):
    return ((data-np.min(data))/(np.max(data)-np.min(data)))
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

a=508
x=np.linspace(-164,164,a)
r,t=cart2pol(x,x[np.newaxis,:].transpose()-140)
b=np.flipud(pink_colormap(256)*autumn_colormap(256))
c=normalize_data(b)*0.93
j=[1,1,0.9]
c_value1=b[np.arange(0,256,2),:]
c_value2=c[np.arange(0,256,2),:]
c_value=np.vstack((j,c_value1,j,j,j,j,j,c_value2))
s=r
s[s<8]=1

f=np.zeros([508,508])
for k in range(508):
    f[k,:]=np.roll(s[460,:],int(np.round(15*np.random.random(1)-0.5)),axis=0)+k/6-5

img=np.vstack((s,f))
interval=1
ind1=np.arange(0,img.shape[0],interval)
img=img[ind1,:]
sz=img.shape
#---apply colors to the pixels---
normalized_img=((img.flatten()-np.min(img))/(np.max(img)-np.min(img)))
idx=np.round((c_value.shape[0]-1)*normalized_img).astype(np.int)
idx[idx<0]=0
img=c_value[idx].reshape([sz[0],sz[1],3])
img=img[349:650,94:410]
plt.imshow(img)
plt.show()
