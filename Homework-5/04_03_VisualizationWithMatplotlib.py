#!/usr/bin/env python
# coding: utf-8

# <font color=blue>Assignments for \"Visualization with Matplotlib\"</font>

# 1. In this assignment, you will make some plots about Corona. First, download the Coronavirus Source Data.
# 
# First, filter the data for four countries (Spain, France, Germany, Italy) and the last 100 days.
# Create a figure with two subplots. The left subplot will show total cases, and the right one will show total deaths for these countries
# 
# Set titles, X and Y labels, change the font, font size, and font color for each subplot.
# 
# Change color, width, and type of lines.
# 
# Put a legend to bottom right.
# 
# Change the color and rotation of the X-axis ticks.
# 
# And set a title for the figure (not for the plots).

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[6]:


covid = pd.read_csv("covid_data.csv")
covid


# In[7]:


covid.columns


# In[8]:


covid.tail(100)


# In[10]:


covid[covid['location'].isin(["Spain","France","Germany","Italy"])].tail(100)


# In[36]:


plt.figure(figsize=(17, 4))

plt.subplot(1, 2, 1)
plt.plot(covid['total_cases'], c = "green", lw = 1)
plt.xlabel('Total Cases',
           fontstyle = 'normal',
           fontsize = 12,
           color = 'green',
           fontfamily = 'Times New Roman'
          )
plt.ylabel('Case',
           fontstyle = 'normal',
           fontsize = 12,
           color = 'green',
           fontfamily = 'Times New Roman'
          )
plt.title("Total Cases Graph", color = "Green")
plt.xticks(rotation = 45, fontsize = 9)
plt.legend(title = 'Covid Total Cases', loc = 4)

plt.subplot(1, 2, 2)
plt.plot(covid['total_deaths'], c = "blue", lw = 1)
plt.xlabel('Total deaths',
          fontstyle = 'normal', 
          fontsize = 20,
          fontweight = 'normal', 
          color = "blue",
          fontfamily = 'Times New Roman'
          )

plt.ylabel('Death',
          fontstyle = 'normal', 
          fontsize = 12,
          color = "blue",
          fontfamily = 'Times New Roman')

plt.legend(title = 'Covid Total Deaths', loc = 4)
plt.title("Total Deaths Graph", color = "Blue")
plt.xticks(rotation = 45, fontsize = 9)


# In[ ]:




