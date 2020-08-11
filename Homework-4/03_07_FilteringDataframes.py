#!/usr/bin/env python
# coding: utf-8

# # Assignments for "Filtering Dataframes"

# 1. By using conditional selection methods, calculate the survival rate for all passengers under 30 years old.

# In[6]:


import pandas as pd
import numpy as np

df = pd.read_csv("train.csv", sep = ',')
df[(df['Age'] < 30 ) & (df['Survived'] == 1)]


# 2. Calculate the survival rate by gender.

# In[7]:


len(df[(df['Age'] < 30) ])


# In[8]:


rate = (len(df[(df['Age'] < 30) & (df['Survived'] == 1)]))/(len(df[(df['Age'] < 30) ]))
print("Survival rate of passengers under 30 : {}".format(rate))


# In[9]:


df[(df['Sex'] == "female") & (df['Survived'] == 1)]


# In[10]:


len(df[(df['Sex'] == "female") & (df['Survived'] == 1)])


# In[11]:


df[(df['Sex'] == "female")]
len(df[(df['Sex'] == "female")])


# In[12]:


df[(df['Sex'] == "male") & (df['Survived'] == 1)]


# In[15]:


len(df[(df['Sex'] == "male") & (df['Survived'] == 1 )])


# In[ ]:




