#!/usr/bin/env python
# coding: utf-8

# <font color=blue>Assignments for \"Introduction to Matplotlib\"</font>

# 1. Create a blank figure with matplotlib functions. Plot cosine function for the numbers beetwen -3$\\pi$ and 3$\\pi$ with 0.1 intervals.

# In[4]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math


# In[15]:


fig = plt.figure()  
x = np.arange((-3)*(math.pi),3*(math.pi),0.1)
y = np.cos(x)
fig, ax = plt.subplots()
plt.title("Cosine function")
plt.xlabel("X") 
plt.ylabel("Y")
ax.plot(x, y, color = "Green")


# 2. This time, create the same plot in red color with object methods. 

# In[16]:


fig = plt.figure()  
x = np.arange((-3)*(math.pi),3*(math.pi),0.1)
y = np.cos(x)
fig, ax = plt.subplots()
plt.title("Cosine function")
plt.xlabel("X") 
plt.ylabel("Y")
ax.plot(x, y, color = "Red")


# In[ ]:




