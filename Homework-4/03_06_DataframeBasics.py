#!/usr/bin/env python
# coding: utf-8

# # Assignments for "Dataframe Basics"

# 1. Create a DataFrame whose index is the first 10 letters of the alphabet and contains two more columns with first 10 prime numbers and the first 10 fibonacci numbers.

# In[3]:


import pandas as pd
df = {'letter': ['A', 'B','C', 'D', 'E', 'F', 
                         'G', 'H', 'I','J'],
                'prime_number': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
                'fibonacci_number': [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]}
example_df = pd.DataFrame(df)
example_df


# In[ ]:




