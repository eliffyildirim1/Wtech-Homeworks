#!/usr/bin/env python
# coding: utf-8

# Assignments for "Tuples and Sets"

# 1. Create a tuple named "week" containing weekdays.

# In[1]:


week =  ("sunday", "monday", "tuesday","wednesday","thursday","friday","saturday")


# 2. Create a set named "fruits" containing followings: apple, mango, orange

# In[2]:


fruits = {'apple', 'mango', 'orange'}


# 3. Create a new set named "new_fruits" containing followings: cherry, peach, apple, mango

# In[3]:


new_fruits = {'cherry', 'peach', 'apple','mango'}


# 4. Find the fruits which are in new_fruits but not in fruits."
# 

# In[4]:


print(new_fruits.difference(fruits))


# 5. Find the fruits which are in both new_fruits and fruits.

# In[5]:


print(new_fruits.intersection(fruits))


# In[ ]:




