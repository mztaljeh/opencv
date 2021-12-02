#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import math

import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(r"C:\Users\ZaherTaljeh\Desktop\digital_images_week2_quizzes_lena.gif")
ret, img = cap.read()
cap.release()
img=img.astype(float)
##print(rimg)
blur = cv2.blur(img,(5,5))
blur=blur.astype(float)
mse = np.square(np.subtract(img,blur)).mean()
print(255*255)
print(255**2)
psnr = 10 * math.log10(255**2 / mse)
print(mse)

print(psnr)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
#print(dst)

mse1 = np.square(np.subtract(img,dst)).mean()
psnr1 = 10 * math.log10(255**2 / mse1)

print(psnr1)



#rows,cols,colors = img.shape # gives dimensions for RGB array
#img_size = rows*cols*colors
#img_1D_vector = img.reshape(img_size)
#blur_1D_vector = blur.reshape(img_size)

##ablur = shape(blur)
#print(img_1D_vector)
#print(blur_1D_vector)

#cv2.imshow('image',img)
#cv2.imshow('blur',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




