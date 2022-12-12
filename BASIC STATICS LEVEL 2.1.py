#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[31]:


data= {'company':['Allied Signal','Bankers Trust','General Mills','ITT Industries','J.P.Morgan & Co.','Lehman Brothers','Marriott','MCI','Merrill Lynch','Microsoft','Morgan Stanley','Sun Microsystems','Travelers','US Airways','Warner-Lambert'],'Measure':[24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39.42,26.71,35.00]}
df=pd.DataFrame(data)
df


# In[36]:


# to find the mean
df.describe()


# In[37]:


#to find the variance
df.var()


# In[38]:


#to find the standard deviation
df.std()


# In[41]:


# tho show the the outlier
df.plot(x='company', y='Measure',kind='box')
plt.show()

