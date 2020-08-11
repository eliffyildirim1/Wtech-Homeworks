#!/usr/bin/env python
# coding: utf-8

# # <font color=blue>Assignment for "Grouping and Aggregation Operations on DataFrames"</font>

# For Pandas assignments, you are going to use [Titanic](https://www.kaggle.com/c/titanic/download/GQf0y8ebHO0C4JXscPPp%2Fversions%2FXkNkvXwqPPVG0Qt3MtQT%2Ffiles%2Ftrain.csv) (train.csv) dataset. Download the dataset and load to a data frame.

# 1. Calculate the average age of the passengers for each gender and passenger class by using `groupby()` method.

# In[3]:


import pandas as pd
import numpy as np
titanic = pd.read_csv("train.csv")
titanic


# In[4]:


titanic.groupby(by = 'Sex' )['Age'].mean()


# In[6]:


titanic.groupby(by='Pclass')['Age'].mean()


# 2. Group by embarkation port and print values. (Notice that you get unique values with this.)

# In[7]:


for group_name, group in titanic.groupby(by='Embarked'):
    display(group)
    print(group_name)


# In[ ]:




