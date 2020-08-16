#!/usr/bin/env python
# coding: utf-8

# # <font color=blue>Assignments for \"Visualization with Seaborn\"</font>

# In this assignment you will continue to make some plots on the [Coronavirus Source Data](https://ourworldindata.org/coronavirus-source-data). For plotting you will use Seaborn library

# 1. Plot a line plot with seaborn for total deaths four the four countries (Spain, France, Germany, Italy) after April 1, 2020.

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime

import warnings
warnings.filterwarnings('ignore')


# In[3]:


title_style = {'family': 'Century Gothic', 'color': 'darkred', 'size': 20 }
axis_style  = {'family': 'Century Gothic', 'color': 'darkblue', 'size': 15 }


covid = pd.read_csv('covid_data.csv', parse_dates=["date"], low_memory=False)
april = pd.to_datetime("2020-04-01")


covid=covid[pd.to_datetime(covid['date']) > april]
locations= pd.DataFrame({'location':['Spain', 'France', 'Germany', 'Italy']})

four_countries=pd.merge(covid, locations, left_on= ['location'], right_on= ['location'],how="inner")
four_countries


plt.figure(figsize=(15,4))
sns.lineplot(four_countries.location ,four_countries.total_deaths, data = four_countries, lw = 5, color ="yellow",estimator = 'min')

plt.title('Total Deaths for the Four Countries',fontdict = title_style)
plt.xlabel('Countries', fontdict = axis_style)
plt.ylabel('Total Deaths',fontdict = axis_style)

plt.xticks(rotation = 0, fontsize = 15)


plt.show()


# In[ ]:




