#!/usr/bin/env python
# coding: utf-8

# In[67]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image 
import PIL 

from sklearn.metrics import mean_absolute_error as mae
img1 = cv2.imread(r'E:\matirial\imagecorse\digital_images_week4_quizzes_frame_1.jpg',cv2.IMREAD_UNCHANGED)
img2 = cv2.imread(r'E:\matirial\imagecorse\digital_images_week4_quizzes_frame_2.jpg',cv2.IMREAD_UNCHANGED)
I1 = np.asarray(img1,dtype=np.float64)
I2 = np.asarray(img2,dtype=np.float64)

print(img2)
print(I2)


# In[40]:


f=-1
x=-1
v=[]
w, h = 31, 31
Matrix = [[0 for x in range(w)] for y in range(h)] 
for i in range(0,287):
    for j in range(0,351):
        if(i>64 and i<97) and (j>80 and j<113):
            f=f+1
            
            print(f)
            
            


# In[88]:


f=-1
x=-1
w, h = 32, 32
block2 = [[0 for x in range(w)] for y in range(h)] 
block1 = [[0 for x in range(w)] for y in range(h)] 

for i in range(0,287):
    if(i>64 and i<97):
        f+=1
        x = -1
        for j in range(0,351):
            if (j>80 and j<113):
                x+=1
                block2[f][x]=I2[i][j]
                block1[f][x]=I1[i][j]

                
cv2.imwrite(r"E:\matirial\imageblock\zaher.jpg",window)


# In[91]:


windowsize_r = 32
windowsize_c = 32
blocks = []
bloksflattern =[]
meas = []
meas1 = []
i = 0
# Crop out the window and calculate the histogram
for r in range(0,I1.shape[0] - windowsize_r, windowsize_r):
    for c in range(0,I1.shape[1] - windowsize_c, windowsize_c):
        i+=1
        window = I1[r:r+windowsize_r,c:c+windowsize_c]
        windowflat=window.flatten()
        blocks.append(window)
        bloksflattern.append(windowflat)
        f = str(i)
      # cv2.imwrite(r"E:\matirial\imageblock\te"+f+".jpg",window)

#rint(mae(blocks[t], block2))


# In[56]:


print(meas)


# In[81]:



for t in range(len(blocks)-1):
    x=mae(blocks[t], block2)
    meas.append(x)


# In[82]:


print(min( meas ))


# In[92]:


f=-1
I=[]
for i in range(0,287):
    if(i>64 and i<97):
        for j in range(0,351):
            if (j>80 and j<113):
                f+=1
                I.append(I2[i][j])
            
for t in range(len(bloksflattern)-1):
    p=mae(bloksflattern[t], I)
    meas1.append(p)
print(meas1)           


# In[60]:


print(min( meas1 ))


# In[94]:


print(mae(blocks[79], block2))


# In[ ]:




