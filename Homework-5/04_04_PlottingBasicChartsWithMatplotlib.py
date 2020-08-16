#!/usr/bin/env python
# coding: utf-8

#  <font color=blue>Assignments for \"Plotting Basic Charts With Matplotlib\"</font>

# In this assignment, you will continue work with the [Coronavirus Source Data](https://ourworldindata.org/coronavirus-source-data). You will plot different chart types. Don't forget to set titles and axis labels.

# 1. Plot a bar chart for total cases of the 20 countries that have biggest numbers.

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime


# In[50]:


covid=pd.read_csv('covid_data.csv',index_col=0)

total_case=covid.groupby(by='location')['new_cases'].sum()

tc=(total_case.sort_values(ascending=False)).head(20)
country = tc.drop("World", axis=0)
locations= []
for location in country.index[0:21]:
    locations.append(location)


plt.figure(figsize=(12,7))
plt.xlabel('Total Cases')
plt.ylabel('Countries')
plt.title('Total cases of the highest 20 countries')

plt.barh(locations,country,color="#FF914D")


#  2. Plot a histogram for daily deaths for any country you choose. Make three subplots for different bins.

# In[60]:


import warnings
warnings.filterwarnings('ignore')

covid = pd.read_csv("covid_data.csv", index_col=0)

title_style_small = {'family': 'Century Gothic', 'color': 'green', 'size': 10 }
axis_style_small  = {'family': 'Century Gothic', 'color': 'blue', 'size': 10 }

plt.figure(figsize=(15, 5))

plt.subplot(1,3,1)
plt.title("New deaths", fontdict = title_style_small )
for city in ["Turkey"]:
    plt.hist(covid[covid.location == city].new_deaths,color = "green",bins = 50)
    plt.xlabel("Daily deaths", fontdict = axis_style_small)

plt.subplot(1,3,2)
plt.title("New deaths", fontdict = title_style_small )
for city in ["Turkey"]:
    plt.hist(covid[covid.location == city].new_deaths,color = "yellow",bins = 20)
    plt.xlabel("Daily deaths", fontdict = axis_style_small)

plt.subplot(1,3,3)
plt.title("New deaths", fontdict = title_style_small )
for city in ["Turkey"]:
    plt.hist(covid[covid.location == city].new_deaths,color = "blue",bins = 60)
    plt.xlabel("Daily deaths", fontdict = axis_style_small)


# 3. Plot a scatter plot of new cases and new death for Germany and France.
# 

# In[63]:


import warnings
warnings.filterwarnings('ignore')

covid = pd.read_csv("covid_data.csv", index_col=0)

title_style_small = {'family': 'Century Gothic', 'color': 'green', 'size': 10 }
axis_style_small  = {'family': 'Century Gothic', 'color': 'blue', 'size': 10 }

plt.figure(figsize=(15, 5))

plt.subplot(1,3,1)
plt.title("New death for Germany and France", fontdict = title_style_small )
for city in ["Germany", "France"]:
    plt.scatter(covid[covid.location == city].new_deaths,
                covid[covid.location == city].new_cases,
                color = "green")
    plt.xlabel("Daily deaths", fontdict = axis_style_small)


# 4. Plot a boxplot for daily deaths for any country you choose.

# In[66]:


import warnings
warnings.filterwarnings('ignore')

covid = pd.read_csv("covid_data.csv", index_col=0)

title_style_small = {'family': 'Century Gothic', 'color': 'green', 'size': 10 }
axis_style_small  = {'family': 'Century Gothic', 'color': 'blue', 'size': 10 }

plt.figure(figsize=(15, 5))

plt.subplot(1,3,1)
plt.title("New deaths", fontdict = title_style_small )
for city in ["Turkey"]:
    plt.boxplot(covid[covid.location == city].new_deaths)
    plt.xlabel("Daily deaths", fontdict = axis_style_small)


# 5. Calculate the total case for each continent and plot a pie chart

# In[67]:


covid = pd.read_csv("covid_data.csv",index_col=0)

total_cases = covid.groupby(by="continent")["new_cases"].sum()

continents = []                             
for continent in total_cases.index:
    continents.append(continent)

plt.figure(figsize=(15, 5))
plt.title('Total case for each Continent', fontdict = title_style)

plt.pie(total_cases,labels=continents, autopct='%1.2f%%',
        shadow=True, startangle=90)
plt.show()


# In[ ]:




