#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Heloo");
print("riya is a good girl");


# In[7]:


a = int(input("Marks in First Subject"));
b = int(input("Marks in Second Subject"));
c = int(input("Marks in Third Subject"));

average = (a+b+c)/3
print(average);


# In[17]:


a = int(input("Enter a number"));
if(a/2 == 0) :
    print("This is an even number");
else:
    print("This is an odd number");
    a;


# In[21]:


a = int(input("Enter a number"));
if(a > 0 and a<=10) :
    print("This is an small number");
elif ( a>10 and a<=50):
    print("This is an medium sized number");
else :
    print("This is a huge number");
    a;


# In[23]:


# print upto n natural numbers
a = int(input("Enter a number: "))
count = 1;
while(count <=a):
    print(count);
    count = count+1;
    


# In[24]:


# print 1 n times
a = int(input("Enter a number: "))
count = 1;
while(count <=a):
    print(1);
    count = count+1;


# In[35]:


# either a number is prime or not
n = int(input("Enter a number"));
d = 2;
flag = False;
while (d<n):
    if(n % d == 0):
        flag = True;
    d = d+1; 
if flag == True:
     print("number is not prime");
else :
    print("Number is prime!!!!");


# In[ ]:


# prime numbers till n
n = int(input("Enter a number"));
k = 2;
while k<=n:
    d = 2;
    flag = False;
    while (d<k):
        if(k % d == 0):
            flag = True;
        d = d+1; 
    if flag == False:
    print(k);
    k = k+1;


# In[ ]:





# In[ ]:




