#!/usr/bin/env python
# coding: utf-8

# # Assignments for "basics of NumPy Array"

# 1. Create 3 lists representing house features, each list containing 10 values. First one for squaremeter of house, second one for rooms and last one for price. Then, create an array combining these lists.

# In[2]:


import numpy as np
squaremeter_house = [110,80,96,240,180,156,86,76,182,115]
rooms = ["kitchen","guest_room","garage","study_room","bathroom","living_room","sport_room","parent_room","children_room","garden"]
price = [50000,47550,786520,44582,53110,80000,180000,2000000,178500,180000]
home = np.array([squaremeter_house,rooms ,price])
print(home)


# 2. Transpose the array you have created, so that every line can represent features of one house.

# In[4]:


new_home = home.T
print(new_home)


# 3. Display the shape of the array and explain what it means.

# In[5]:


home.shape


# 4. Write a function that returns an array of ones with zeros where both row and column numbers are even. Sample array is below. Number of rows and columns will be entered as parameters.
# shape(6 x 5) --> [[1   1   1   1   1]
#                       [1   0   1   0   1]
#                       [1   1   1   1   1]
#                       [1   0   1   0   1]
#                       [1   1   1   1   1]
#                       [1   0   1   0   1]]

# In[13]:


import numpy as np
x = int(input("Enter the size of the line: "))
y = int(input("Enter the size of the column: "))
a = np.ones((x, y))
for i in range(0,x):
    for j in range(0,y):
        if( i % 2 == 0 and j % 2 == 0):
            a[i][j]= 0
print(a)
            


# In[ ]:




