#!/usr/bin/env python
# coding: utf-8

# 1. A prime number is an integer greater than one that is only divisible by one and itself. Write a function that determines whether or not its parameter is prime, returns True if it is and False otherwise. Write a main program that reads an integer from the user and displays a message indicating whether or not it is prime. Ensure that the main program does not run if the file containing your solution is imported into another program.

# In[1]:


def func_prime():
    if (number == 1): 
            print("It is not a prime number")
            return False
            
    elif(number == 2):
            print("It is a prime number")
            return True
        
    for i in range (2, number):

        if(number % i == 0):
            print("It is not a prime number")
            return False

        else:
            print("It is a prime number")
            return True
        

number =int(input("Enter of the number: "))
func_prime()


# 2. Please write a function that passes each element of a list only once to a new list. We usually do this with the `set()` command, but let us not use this command this time,
#      Example:
#             unique_list([1,2,2,3,3,4,4]) = [1,2,3,4]

# In[2]:


def only_func():
    unique_list = [1,2,2,3,3,4,4]
    new_list = []
    for i in unique_list:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
only_func()


# 3. There are many built-in modules in Python. By importing one of the modules on time, write a function that takes the date of birth as a parameter and returns the age.

# In[3]:


import datetime

def age_func():
    year = int(input("Enter year of birth: "))
    now_date = datetime.datetime.now()
    this_year = datetime.datetime.strftime(now_date, '%Y')
    age = int(this_year) - year
    print("Your age is: ",age)
    
age_func()    


# 4. Get a number from the user and calculate the factorial of it by using a function.

# In[4]:


def fact_func(number):
    mult = 1
    for i in range(1,number+1):
        mult *= i
    print(mult)

number = int(input("Enter of the number: "))
fact_func(number)


# 5. Write a function named `perfect()` that determines if the parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.",
# An integer number is said to be a `perfect number` if its factors (including 1, but not the number itself) sum to the number,
#     
# E.g.: 6 is a perfect number because 6 = 1 + 2 + 3

# In[6]:


def perfect():
    perfect_numbers = []
    
    for i in range(1, 1000):
        sum = 0
        
        for j in range(1, i):
            if i % j == 0:
                sum += j
        
        if sum == i:
            perfect_numbers.append(sum)
    
    print(perfect_numbers)    
          
perfect()


# 6. Write a Python function that prints out the first n rows of [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle).",

# In[12]:


def pascalTriangle(height, lines=[]):
    lines.append([1])
    line=[1]
    for i in range(height):
        next = 0
        next_row = []
        for k in line:
            next_row.append(next + k)
            next = k
        next_row.append(1)
        
        line = next_row
        lines.append(line)
    
    return lines

number = int(input("Prints out the first n rows of "))

for x in pascalTriangle(number):
    print(x)


# In[ ]:




