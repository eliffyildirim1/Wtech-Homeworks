#!/usr/bin/env python
# coding: utf-8

# # Assignments for Loops

# 1. Please form a multiplication table from user input.
# Enter a number : 6\n ,
#             6 x 1 = 6                                                               
#             6 x 2 = 12                                                              
#             6 x 3 = 18                                                             
#             6 x 4 = 24                                                              
#             6 x 5 = 30                                                             
#             6 x 6 = 36                                                            
#             6 x 7 = 42                                                             
#             6 x 8 = 48                                                              
#             6 x 9 = 54                                                              
#             6 x 10 = 60 
#             
# 

# In[ ]:


number= int(input("Enter a number :"))
#for i in range(1,10):
for j in range(1,11):
        print("{} x {} = {}".format(number, j, number*j))
    
    


# 2. Simply by using list compherension, form a list by taking square of odds numbers and by calculating cube of even numbers from 1 to 20.
# 

# In[ ]:


list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# In[ ]:


even_numbers = []
for n in range(21):
    if n % 2 == 0:
        even_numbers.append(n*n*n)
    else:
        continue

print(even_numbers)


# 3. Please type a code that inverts the initial user input.
# 
# Example : automobile --> elibomotua
# 

# In[ ]:


word=input("Please, enter the word :")
reverse_word= ""
for i in range(len(word) - 1, -1, -1):
    reverse_word = reverse_word + word[i]
print("Reverse word : {} ".format(reverse_word))


# 4. Using `range(1, 201)`, make two lists. One is containing all even numbers and the other containing all odd numbers.

# In[ ]:


even_numbers = []
odd_numbers = []

for n in range(201):
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)
print(even_numbers)

print(odd_numbers)


# 5. Define a function called `count` that has two arguments called `sequence` and `item`. Return the number of times the item occurs in the list.
#       Example:
#       python
#        count([1,2,1,1], 1)
#   
#       It should return 3. Because `1` appears 3 times in the list.

# In[15]:


def count(sequence, item):
    counter = 0
    
    for i in range(len(sequence)):
        if item == sequence[i]:
            counter += 1
    
    print("{} appears {} times in the list.".format(item,counter))
           
count([1,2,1,1], 1)


# 6. Write a function called `digit_sum` that takes a positive integer n as input and returns the sum of all that number's digits as a single-digit number.\n",
#     "\n",
#     "    Example:\n",
#     "        27684 --> 2 + 7 + 6 + 8 + 4 = 27 --> 2 + 7 = 9

# In[ ]:


n= int(input("Enter the number :"))
sum=0
new_sum=0
while True:
    if n == 0:
        break
    else:
        sum +=int(n%10)
        n /=10
if sum %2 == 0:
    new_sum +=int(sum%10)
    sum /=10
    print("The sum of all that numbers", new_sum)
else:
    print("The sum of all that numbers", sum)


# 7. Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
# 

# In[17]:


number1 = int(input("Enter of the first number: "))
number2 = int(input("Enter of the second number: "))

if (number1 > number2):
    small = number2
else:
    small = number1

for i in range(1, small+1):
    if (number1 % i == 0) and (number2 % i == 0):
        gcd = i

print("GCD = " ,gcd)
print("HCF = " ,(number1*number2) // gcd)


# 8. Write a Python program that iterates integers from 1 to 50. For multiples of three print `fizz` instead of the number and for the multiples of five print `buzz`. For numbers which are multiples of both three and five print `fizzbuzz`"

# In[41]:


for i in range(1, 50):
    if (i % 3 == 0) and (i % 5 == 0):
        print("fizzbuzz")
    elif (i % 3 == 0):
        print("fizz")
        
    elif (i % 5 == 0):
        print("buzz")
        
    else:
        print(i)


# 9. Please form a list out of Fibonacci numbers from 1 to 50. The first two Fibonacci numbers are 1. The next numbers are the sum of the previous two.

# In[42]:


fibonacci_numbers = [0, 1]
for i in range(1,50):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
print(fibonacci_numbers)


# In[ ]:




