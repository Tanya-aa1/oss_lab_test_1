#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter,butter

    

minutes=np.linspace(0,10,1440)    
heart_rate_data=np.random.normal(0,0.5,1440)
print("heart rate data ")
print(heart_rate_data)



smooth=lfilter(heart_rate_data,1,minutes)
print("smoothed data")
print(smooth)




# fig,ax=plt.subplots()
plt.plot(minutes,heart_rate_data, label="noisy data")
plt.plot(minutes,smooth, label="smoothed data")
plt.legend()


# In[ ]:




