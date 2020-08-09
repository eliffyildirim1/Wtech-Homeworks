#!/usr/bin/env python
# coding: utf-8

# # Assignments for "Errors and Exception Handling"

# 1. Let us define a division operation inside a function (using `def`) but to get an error, define the denominator as 0. So, type properly except statement.

# In[1]:


def division(number1, number2):
    try:
        result = number1 // number2
        print("Result :", result)
    except Exception as e:
        print ("'{}' hatası oluştu ! ".format(e))
        
number1 = int(input("Enter the number to divide:"))
number2 = int(input("Enter the divisor:"))
division(number1,number2)


# 2. It is possible to get multiple errors after the execution of one try block. So, please define an error-exception issue with `NameError`

# In[2]:


try:
    print(x)
except Exception as e:
        print ("'{}' hatası oluştu ! ".format(e))


# 3. Please define a function and with this function, generate a `ValueError` exception simply by entering a string instead of numerical value.

# In[4]:


def num():
    try:
        x=int(input("Bir sayı girin   : "))
        print(x)
    except ValueError:
        print (ValueError)
num()


# In[ ]:





# In[ ]:




