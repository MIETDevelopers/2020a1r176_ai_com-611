#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data=pd.DataFrame(data=pd.read_csv('C:/Users/rikit/Downloads/my data.csv'))
print(data)
                  


# In[3]:


concepts= np.array(data.iloc[:,0:-1])
print(concepts)


# In[4]:


target = np.array(data.iloc[:,-1])
print(target)


# In[5]:


def learn(concepts, target):
    specific_h = concepts[0].copy()
    print("\nInitialization of specific_h and general_h")
    print(specific_h)
    general_h =[["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print(general_h)
    for i, h in enumerate(concepts):
        if target[i] =="yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        if target[i] == "no":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
        print("\nSteps of Candidate Elimination Algorithm",i+1)
        print(specific_h)
        print(general_h)
    indices = [i for i, val in enumerate(general_h) if val == ['?','?','?','?','?','?']]
    for i in indices:
               general_h.remove(['?','?','?','?','?','?'])
    return specific_h, general_h
s_final, g_final = learn(concepts, target)
print("\nfinal specific_h:", s_final, sep="\n")
print("\nfinal general_h:", g_final, sep="\n")


# In[ ]:




