
# coding: utf-8

# In[211]:


import random
s=0
p=0
a=int(input("Enter the number of tosses to be performed :"))

def toss():
    hort = random.randint(0, 1)
    pos = ["Heads", "Tails"]
    return pos[hort]

for i in range (0, a):
    tores = toss()
    print(tores)
    if tores=='Heads':
        s=s+1
    else:
        p=p+1

print("No of occurance of heads : "+str(s))    
print("No of occurance of tails : "+str(p))
print("The probability of occurance of event heads is : ")
print(s/a)
print("The probability of occurance of event heads is : ")
print(p/a)


# In[18]:


import random
s=0
p=[]
g=0
l=0
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

def toss():
    hort = random.randint(0, 1)
    pos = ["Heads", "Tails"]
    return pos[hort]


for j in a:
    for i in range (0, j):
        tores = toss()
    if tores=='Heads':
        s=s+1
        g=s/j
    p.append(g) 
print(p)


# In[19]:


import matplotlib.pyplot as plt
print(a)
print(p)
plt.plot(a,p)
plt.ylabel("probability of head")
plt.xlabel("input")


# In[17]:


import matplotlib.pyplot as plt
q=[1,2,3,4]
w=[0.0,1.0,0.3333333333333333,0.25]
print(q)
print(w)
plt.plot(q,w)
plt.ylabel("probability of head")
plt.xlabel("input")

