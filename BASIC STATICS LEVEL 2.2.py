#!/usr/bin/env python
# coding: utf-8

# #                 Assignment 2 – BASIC STATICS LEVEL 2.2                        

# # Normal distribution, Functions of Random Variables
# 

# 1) The time required for servicing transmissions is normally distributed with  = 45 minutes 
# and  = 8 minutes. The service manager plans to have work begin on the transmission of 
# a customer’s car 10 minutes after the car is dropped off and the customer is told that 
# the car will be ready within 1 hour from drop-off. What is the probability that the 
# service manager cannot meet his commitment?

# In[1]:


from scipy import stats
from scipy.stats import norm


# In[2]:


# to find the value of the z-score at x=50.
#z=(x-mu)/ sigma
z = (50-45)/8
z


# In[3]:


# to find the probabality p(x>50) = 1-stats.norm.cdf(abs(Z_score))
1-stats.norm.cdf(abs(0.625))


# In[5]:


# to find the probablity p(x<=50)
# p_value = stats.norm.cdf(abs(z_score))
p_value = stats.norm.cdf(abs(0.625))
p_value


# In[6]:


# p(x>50) = 1 - p(x<=50)
1 - 0.734


# # ANS: B) 0.2676

# 2) The current age (in years) of 400 clerical employees at an insurance claims processing center is normally distributed with mean  = 38 and Standard deviation  =6. For each statement below, please specify True/False. If false, briefly explain why.

# In[7]:


from scipy import stats
from scipy.stats import norm


# # A. More employees at the processing center are older than 44 than between 38 and 44.

# In[8]:


# p(x>44); employees older than 44 years of age
1 - stats.norm.cdf(44,loc=38,scale=6)


# In[9]:


# p(38<x<44); employees older between 38 and 44 years of age
stats.norm.cdf(44,loc=38,scale=6) - stats.norm.cdf(38,loc=38,scale=6)


# a. More employees at the processing center are older than 44 than between 38 and 44.
# 
# Ans ➔ False because prob(38<x<44) > prob(x>44)
#  prob(x>44) = 0.1586 
#  prob(38<x<44) = 0.3414

# B. A training program for employees under the age of 30 at the center would be expected to attract about 36 employees.

# In[10]:


# p(x<30); employees less than 30 years of age
stats.norm.cdf(30,loc=38,scale=6)


# In[11]:


# number of employees attending training program from 400 numbers is N * P(X<30)
400*stats.norm.cdf(30,38,)


# b. A training program for employees under the age of 30 at the center would be expected to attract about 36 employees.
# Ans ➔ True because prob(x<30) = 9.12%, and 9.125 0f 400 = 36.48 which is around 36.

# 3) If X1~ N(μ, σ2) and X2 ~ N(μ, σ2) are informal random variables, then what is the difference between 2 X1 and X1 + X2? 
# Discuss both their distributions and parameters. 
# 

# For 2X1,
#  = N((2mu), (2sigma)^2) = N(2(mu), 4(sigma)^2)
#  For X1+X2,
#  = N((mu), (sigma)^2) + N((mu), (sigma)^2) = N(2(mu), 2(sigma)^2)
#  For (2X1 - (X1+X2)),
#  =~N(4(mu), 6(sigma)^2)
# 

# 4) Let X ~ N (100, 202). Find two values, a and b, symmetric about the mean, such that the 
# probability of the random variable taking a value between them is 0.99.
# 
# A. 90.5, 105.9 
# B. 80.2, 119.8 
# C. 22, 78 
# D. 48.5, 151.5 
# E. 90.1, 109.9

# In[12]:


from scipy import stats
from scipy.stats import norm


# In[13]:


stats.norm.interval(0.99, 100, 20)


# D - 48.5, 151.5

# 5) Consider a company that has two different divisions. The annual profits from the two divisions are independent and have distributions Profit1 ~ N(5, 32) and Profit2 ~ N(7, 42) 
# respectively. Both the profits are in Million. Answer the following questions about the total profit of the company in Rupees. Assume that $1 = Rs. 45
# 
# A. Specify a Rupee range (centered on the mean) such that it contains 95% probability 
# for the annual profit of the company.
# 
# B. Specify the 5th percentile of profit (in Rupees) for the company
# 
# C. Which of the two divisions has a larger probability of making a loss in a given year

# In[14]:


import numpy as np
from scipy import stats
from scipy.stats import norm


# In[15]:


# variance of profit from two different divisions of a company = SD**2 = SD1**2 + SD2**2
SD = np.sqrt((9)+(16))
print('standard deviation is', SD*45, 'Million')


# In[18]:


#A. Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.

print('range is Rs',(stats.norm.interval(0.95,540,225)),'in Millions')


# In[19]:


#B. Specify the 5th percentile of profit (in Rupees) for the company

#to compute 5th percentile, we use the formula x=mu + z(sigma); where in from z table, 5 percentile is -1.645
x=540+(-1.645)*(225)
print('5th percentile of profit (in Millin Rupees) is',np.round(x,))


# In[20]:


#C. Which of the two divisions has a larger probability of making a loss in a given year

#Probablity of 1 division making a loss (x<0)
stats.norm.cdf(0,5,3)


# In[21]:


#Probablity of 1 division making a loss (x<0)
stats.norm.cdf(0,7,4)


# In[ ]:




