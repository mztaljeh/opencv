#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


get_ipython().system('pip install opencv-python')


# In[1]:


import cv2
img = cv2.imread(r"C:\Users\ZaherTaljeh\Desktop\test1.jpg")
cv2.imshow("Pic",img)
img_not = cv2.bitwise_not(img)
cv2.imshow("Invert1",img_not)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




