#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[3]:


import numpy


# In[21]:


img = cv2.imread(r'C:\Users\ASUS\Desktop\ya1.jpg',cv2.IMREAD_UNCHANGED)


# In[22]:


print(img)


# In[23]:


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[25]:


cv2.imwrite(r'C:\Users\ASUS\Desktop\messigray.png',img)


# In[29]:


import numpy as np
import cv2

img = cv2.imread(r'C:\Users\ASUS\Desktop\ya1.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(r'C:\Users\ASUS\Desktop\zaher.jpg',img)
    cv2.destroyAllWindows()


# In[3]:


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\ASUS\Desktop\ya1.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()


# In[ ]:




