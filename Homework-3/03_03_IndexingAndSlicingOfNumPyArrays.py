#!/usr/bin/env python
# coding: utf-8

# # Assignments for "Indexing and Slicing of NumPy Arrays"

# For the assignment, you are going to use [Earthquakes](https://bootrain-lms-assets.s3.eu-central-1.amazonaws.com/bootrain-lms-static/datasets/Earthquakes.csv) dataset.

# 1. Load the Earthquakes dataset. Export the dataset to an array as you covered in the previous lesson.

# In[2]:


import numpy as np
from numpy import genfromtxt
data = genfromtxt('Earthquakes.csv', delimiter=',')
data


# 2. Slice first 20 rows and column numbers 3, 5, 6, 7, 12. Then, assign the array you sliced to a variable.

# In[3]:


data2=data[0:21 ,[3,5,6,7,12]]
print(data2)


# 3. Display the row numbers where last values are equal to 4.5 or higher

# In[4]:


data2[4.5 <= data2]


# 4. Assign 1 to first row.

# In[7]:


data2[0,:] = 1
data2[0,:]


# 5. Save the final state of the array to disk. You are going to use this in the next assignment."

# In[8]:


np.save("data2.npy", data2)


# In[ ]:




