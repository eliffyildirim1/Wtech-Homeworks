#!/usr/bin/env python
# coding: utf-8

# Assignments for Conditional Statements

# 1. Please get Celcius or Fahrenheit degrees from users and type a code to convert these heat units to each other. 
# For conversion, please use this formula: C = (5/9) * (F - 32)
#     Example :  40C --> 104F
#                52F --> 11.1C

# In[1]:


temp = input('Enter the temperature value in type Fahrenheit or Celcius : ')
C= temp.endswith("C")
if C:
    temp = temp.replace('C','')
    temp = int(temp)
    temp = temp * 9/5 + 32
    print ("%d F" % (temp))
else:
    temp = temp.replace('F','')
    temp = int(temp)
    temp = (5/9) * (temp -32)
    print ("%d T" % (temp))


# 2. A company decided to give a bonus of 5% to the employees if his/her year of service is more than 5 years.
#     "Ask the user for their salary and year of service and print the net bonus amount

# In[3]:


salary = float(input('Please enter your salary: '))
year = int(input('Please enter your service year: '))
if year>5:
    bonus = (salary * 5)/100
    print ("%.2f TL" % (bonus))
else:
    print("Since your service year information is under 5 years, you don't have a bonus amount!")


# 3. Take input of ages of 3 people by the user and determine the oldest and youngest among them.

# In[2]:


list= []
person1 = int(input('Please enter age of first person : '))
list.append(person1)
person2 = int(input('Please enter age of second person : '))
list.append(person2)
person3 = int(input('Please enter age of thirth person : '))
list.append(person3)
list.sort()
print("The youngest person is {} years old".format(list[0]))
print("The oldest person is {} years old".format(list[2]))


# 4. A student will not be allowed to attend to the exam if his / her attendance to classes is less than 75%. Take followings input from the user:
# 
# Number of classes held,
# Number of classes attended.
# 
# Then, print the percentage of classes attended and whether the student is allowed to attend in an exam or not.

# In[5]:


held_lesson = int(input('Please enter the number of lesson : '))
attended_lesson =int(input('Please enter the number of courses you attended : '))
i = "%"
percentage_attended = (attended_lesson / held_lesson)*100
if percentage_attended>75:
    print('Your attendance rate %d %s' % (percentage_attended,i))
    print("You can take the exam!")
else:
    print('Your attendance rate %d %s' % (percentage_attended,i))
    print("You can't take the exam!")


# 5. In this exercise, you will create a program that reads a letter of the alphabet from the user. According to the answer:
# 
# If the user enters a, e, i, o, u, then your program should display a message indicating that the entered letter is a vowel.
# 
# If the user enters y, then your program should display a message indicating that y is sometimes a vowel and sometimes a consonant.
# 
# Otherwise, your program should display a message indicating that the letter is a consonant.

# In[ ]:


letter = input('Please enter a letter : ')
vowel = ["a","e","i","o","u"]
if letter in vowel:
    print("You have entered a vowel!")
elif letter == "y":
    print("You entered the letter y; y can act sometimes as a vowel and sometimes as a consonant!")
else:
    print("You have entered a consonant letter!")

