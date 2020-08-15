#!/usr/bin/env python
# coding: utf-8

# # <font color=blue>Assignments for \"Main Statistical Concepts\"</font>

# 1. Analyze the central tendency and distribution measurements with the mathematical formula given above and the built-in codes available in python through 3 different data that you will generate using the numpy library !!!"

# In[2]:


import pandas as pd
import numpy as np


# In[7]:


df = pd.DataFrame()
df['height'] = np.append(np.random.normal(69, 8, 50), np.random.normal(64, 5, 50))
df['weight'] = np.append(np.random.normal(195, 25, 50), np.random.normal(166, 15, 50))
df


# In[8]:


df.info()


# In[10]:


sum(df['height']) / len(df['height'])
print(np.mean(df['height']))

sum(df['weight']) / len(df['weight'])
print(np.mean(df['weight']))


# In[15]:


import statistics
print(statistics.median(df['height']))
print(statistics.median(df['weight']))

(values, counts) = np.unique(df['height'], return_counts=True)
ind = np.argmax(counts)
values[ind]

(values, counts) = np.unique(df['weight'], return_counts=True)
ind = np.argmax(counts)
values[ind]


# In[ ]:





# In[ ]:




