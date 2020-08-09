#!/usr/bin/env python
# coding: utf-8

# Assignments for "Dictionaries"

# 1. Create a dictionary with 7 days. Ask the user to choose 2 different days by listing the (e.g. \"12\" for Monday and Tuesday). Delete the user-selected days from the dictionary and print the remaining 5 days on the screen.

# In[4]:


week = {"1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday",
        "7": "Sunday"}
day1 = input('Please enter the number of the day you want to delete first: ')
del week[day1]
day2 = input('Please enter the number of the day you want to delete second: ')
del week[day2]
new_days = list(week.values())
print("New days of the week: {}".format(new_days))


# 2. Create a dictionary with the following personnel. Use names as keys.![Screenshot_1.png](attachment:Screenshot_1.png)
# 

# In[5]:


personnel ={'John': {'age': '25', 'sex': 'Male'},
            'Lisa': {'age': '28', 'sex': 'Female'},
            'Linda': {'age': '32', 'sex': 'Female'},
            'Micheal': {'age': '41', 'sex': 'Male'}
           }


# 3.Add child information to Michael and Linda. Michael has two children (Karen (age : 12, female) and Greg (age : 7, male) and Linda has one child (Susan (age: 6, female))"

# In[6]:


personnel ={'John': {'age': '25', 'sex': 'Male'},
            'Lisa': {'age': '28', 'sex': 'Female'},
            'Linda': {'age': '32', 'sex': 'Female','child': {'Susan': {'age': '6', 'sex': 'Female'}}},
            'Micheal': {'age': '41', 'sex': 'Male','child': {'Karen': {'age': '12', 'sex': 'Female'},'Greg': {'age': '7', 'sex': 'Male'}}}
           }


# 4. Print the names of Michael's children in a list.

# In[7]:


children = list(personnel['Micheal']['child'])
print(children)


# In[ ]:




