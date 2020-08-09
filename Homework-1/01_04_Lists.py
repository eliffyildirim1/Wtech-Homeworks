#!/usr/bin/env python
# coding: utf-8

#  Assignments for Lists

# 1. Write a code to compute the sum of the two lowest numbers and the two highest numbers in the following list.

# In[1]:


my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]


# In[4]:


my_list.sort()


# In[5]:


print(my_list)


# In[19]:


new_list=my_list[:2] + my_list[-2:]


# In[24]:


print("The sum of the two lowest numbers : ",new_list[0]+new_list[1])


# In[23]:


print("The sum of the two highest numbers : ",new_list[2]+new_list[3])


# 2. The following two lists contain student names and scores. Write a code that gets the name from the user and prints the score of that student.

# In[9]:


names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", 
          "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]

scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]
i = input('Please enter a name  : ')
j = names.index(i)
print("{}'s note : {}".format(names[j],scores[j]))


# 3. By using the two lists above, what is the maximum score and how many students got that score?

# In[16]:


scores.sort()
x=scores[-1]
y=scores.count(x)
print("Maximum score :{} number of students :{}".format(x,y))


# 4. We can confuse about how many days a month is. Create a list to handle it. You will have month names and day counts in your list together as a nested list.
#    

# In[20]:


months_days = [["January","February","March","April","May","June","July","August","September","October","November","December"], [31, 28, 31,30,31,30,31,31,30,31,30,31]]


# 5. Now create lists of months for each season. Get month names and day counts from the list that you create before with slicing. Name the lists with seasons.

# In[22]:


Winter = [months_days[0][0:3],months_days[1][0:3]]
Spring = [months_days[0][3:6],months_days[1][3:6]]
Summer = [months_days[0][6:9],months_days[1][6:9]]
Autumn = [months_days[0][9:12],months_days[1][9:12]]
print("Winter months : {}".format(Winter))
print("Spring months : {}".format(Spring))
print("Summer months : {}".format(Summer))
print("Autumn months : {}".format(Autumn))


# 6. Finally, from the list in the previous question, calculate how many days the summer season lasts.

# In[23]:


count = Summer[1][0] + Summer[1][1] + Summer[1][2]
print("Summer season lasts {} days in total.".format(count))


# In[ ]:




