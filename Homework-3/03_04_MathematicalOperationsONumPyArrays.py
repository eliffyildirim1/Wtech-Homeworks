#!/usr/bin/env python
# coding: utf-8

# # Assignments for "Mathematical Operations on NumPy Arrays"

# 1. Load the array you saved in the previous lesson from the disk.

# In[1]:


import numpy as np
data2 = np.load("data2.npy")
print(data2)


# 2. Display the mean and the standard deviation for each column.

# In[2]:


print(data2.mean(axis = 1))


# 3. Subtract 1, 25, 25, 10, 4 from columns in order. (Remember it can be subtracted in one line of code.)

# In[3]:


print(data2)
print(data2 - [1, 25, 25, 10, 4])


# 4. Multiply each element by 2. (Remember it can be multiplied in one line of code.)

# In[4]:


print(data2 * 2)


# In[ ]:




