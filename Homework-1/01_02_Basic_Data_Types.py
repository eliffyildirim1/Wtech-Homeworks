#!/usr/bin/env python
# coding: utf-8

# Assignments for "Basic Data Types"

# 1. Suppose you invested in Bitcoin at the end of 2017 when Bitcoin gained a lot of value. What would be your money at the end of a week if you had invested \\$1000 with an average daily increase of 12\\% ? You can solve the problem using Python.

# In[3]:



# Create a variable capital ($1000)

# Create a variable for daily growth (12%)

# Create a variable for period (7)

# Calculate the final growth rate

# Calculate result

# Print result


# In[4]:


capital = 1000
daily_growth = 0.12
period = 7


# In[5]:


# For this question, we need to use a compound interest formula.Our formula :
# Result = capital * (1 + daily_growth)**period


# In[6]:


print("Our capital : ", capital)
result = capital * ((1 + daily_growth)** period)
print ("Result : {}  ".format(result))
final_growth_rate = result - capital
print ("Final growth rate : {}  ".format(final_growth_rate))


# 2.Print the text in quotes with Python. However, you must get the numbers from variables using .format() notation.
# Because the text is long, you might consider writing in two lines:
# 
#  `"When we buy bitcoin with 1000 USD at the beginning of the week, we would earn 1210.68 USD at the end of the week, with an average gain of 12\%."`

# In[7]:


ratio = 12


# In[8]:


print("`""When we buy bitcoin with {} USD at the beginning of the week, we would earn {} USD at the end of the week, \n with an average gain of {}\ %.""`".format(capital,final_growth_rate,ratio))


# Get the temperature in Fahrenheit from user and write a code to convert it to Celcius. For conversion, you can use this formula: C = (5/9) * (F - 32)
# 
#  Enter the temperature in Fahrenheit: 
#  user --> 26
#  output --> Temperature (C) : -3.33

# In[9]:


F = int(input('Enter the temperature value in type Fahrenheit : '))
C = (5/9) * (F - 32)
print('Temperature value in Celcius type : {}'.format(C))


# 4. Get a three digit number the from user and calculate the sum of the digits in the integer.
# 
#  user --> 365
#  output --> "The sum of digits in the number is 14

# In[10]:


number = int(input('Please enter a number : '))
sum_of_digits = 0
for digit in str(number):
    sum_of_digits += int(digit)
    
print("The sum of digits in the number is {}".format(sum_of_digits))


# 5. Write some code to calculate the hypotenuse of a right angled triangle. Get the side lengths from the user.
# 
#  user --> first side lenth : 6
#  user --> first side lenth : 8
#  output --> "The length of the hypotenuse is 10

# In[11]:


import math
number1 = int(input('Please enter first length : '))
number2 = int(input('Please enter second length : '))
hypotenuse = math.sqrt((number1**2) + (number2**2))
print('The length of the hypotenuse is %d' % (hypotenuse))


# In[ ]:




