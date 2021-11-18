#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
img1 = cv2.imread(r'C:\Users\ASUS\Desktop\z1.jpg')
img2 = cv2.imread(r'C:\Users\ASUS\Desktop\z2.jpg')
dst = cv2.addWeighted(img1, 0.3, img2, 0.7, 0.0)
cv2.imwrite(r'C:\Users\ASUS\Desktop\z44.jpg',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




