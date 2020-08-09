#!/usr/bin/env python
# coding: utf-8

# # Assignments for "File Operations"
# 

# 1. Please write a poem you wanted in a `.txt` file and save it to the disk.

# In[ ]:


with open("poem.txt", "w") as f:
    f.write(""""Sana gitme demeyeceğim.\nÜşüyorsun ceketimi al.\nGünün en güzel saatleri bunlar.\nYanımda kal.\nSana gitme demeyeceğim.\nGene de sen bilirsin.\nYalanlar istiyorsan yalanlar söyleyeyim,\nİncinirsin.\nSana gitme demeyeceğim,\nAma gitme, Lavinia.\nAdını gizleyeceğim\nSen de bilme, Lavinia.""")


# 2. Append a new poem into the file you have created.

# In[ ]:


with open("poem.txt", "a") as f:
    f.write("\n")
    f.write("------------------")
    f.write("\n")
    f.write("""Seni saklayacağım inan\n
Yazdıklarımda, çizdiklerimde,\n
Şarkılarımda, sözlerimde.\n
Sen kalacaksın kimse bilmeyecek\n
Ve kimseler görmeyecek seni,\n""")


# 3. Read and print all poems.

# In[1]:


poem = open("poem.txt")
print(poem.read())


# In[ ]:




