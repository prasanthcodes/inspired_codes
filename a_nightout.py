
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
def winter_colormap(m):
    r=np.zeros(m)
    g=np.arange(0,m)/np.max([m-1,1])
    b=0.5+(1-g)/2.0
    rgb = np.vstack((r, g, b)).transpose()
    return rgb
def pink_colormap(m):
    rgb=np.sqrt((2*gray_colormap(m)+hot_colormap(m))/3)
    return rgb

x=np.arange(-164,164,0.646)
r=np.sqrt(x[np.newaxis,:]**2+(x[np.newaxis,:].transpose()-140)**2)
b=np.flipud(pink_colormap(256)*winter_colormap(256))
j=[1,1,0.9]
c_value=b[np.arange(0,256,2),:]
c_value=np.vstack((j,c_value))
f=np.zeros([508,508])
for k in range(508):
    f[k,:]=np.roll(r[460,:],np.random.randint(-7,7,[1]),axis=0)

img=np.vstack((r,f))
interval=2
ind1=np.arange(0,img.shape[0],interval)
img=img[ind1,:]##resizing
sz=img.shape
#---apply colors to the pixels---
normalized_img=((img.flatten()-np.min(img))/(np.max(img)-np.min(img)))
idx=np.round((c_value.shape[0]-1)*normalized_img).astype(np.int)-2
idx[idx<0]=0
img=c_value[idx].reshape([sz[0],sz[1],3])

a=np.arange(-90,90+1,1)
xval=-25*np.cos(a*np.pi/180)
yval=24*np.sin(a*np.pi/180)
xpos=np.vstack((xval+268,xval*.4+268)).transpose()
ypos=np.vstack((yval+468,-yval+468)).transpose()
plt.fill(xpos,ypos/interval,color=j,edgecolor=j)
plt.imshow(img)
plt.show()

