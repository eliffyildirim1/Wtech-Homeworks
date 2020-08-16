#!/usr/bin/env python
# coding: utf-8

# # <font color=blue>Assignments for \"Main Statistical Concepts\" </font>

# It has been found that some of the computers sold by Company A are defective. Assuming that there are 3 computer-producing companies (A, B, and C), the amount of computer production of these companies and the probabilities of defective production are as follows",
# 
# 
#     "Total production percentage : 
#     "$P(A)=0.40$
#     "$P(B)=0.40$ 
#     "$P(C)=0.20$
#     "Possibility of defective production :
#     "$P(D|A)=0.015$
#     "$P(D|B)=0.020$
#     "$P(D|C)=0.010$",
# 
#     "What is the probability that a randomly selected defective computer will be produced by company B?"

# In[5]:


""""
D = Defective Production
P(D/B) = P(B∩D)/P(B)

P(D/B) = 0.20/(0.40*0.020+0.40*0.98)

"""
probability = 0.20/((0.40*0.02)+(0.40*0.98))
print(probability)


# In[ ]:




