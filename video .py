#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install opencv-python')


# In[2]:


import numpy as np
import cv2

cap = cv2.VideoCapture(r'C:\Users\ASUS\Desktop\WorldWar.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,1)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[44]:


import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(100,100,0),5)
pts = np.array([[100,50],[80,120],[280,80],[200,40]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,40), font, 4,(100,0,99),2)
cv2.rectangle(img,(384,0),(510,128),(255,255,0),1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:





# In[ ]:





# In[ ]:




