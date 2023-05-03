#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# In[3]:


data = pd.read_csv('C:/Users/student/Downloads/Salary_Data.csv')
data.head(10)


# In[4]:


data.shape


# In[5]:


data.describe()


# In[6]:


sns.pairplot(y_vars = 'Salary' , x_vars = 'YearsExperience' , data = data)


# In[7]:


data.corr()


# In[8]:


x = data['YearsExperience']
y = data['Salary']


# In[10]:


x_train,x_test,y_train,y_test = train_test_split(x,y, train_size = 0.7, test_size = 0.3, random_state = 100)


# In[11]:


x_train.shape


# In[12]:


x_test.shape


# In[17]:


x_train_sm = sm.add_constant(x_train)
model = sm.OLS(y_train,x_train_sm).fit()


# In[18]:


print(model.summary())


# In[19]:


plt.scatter(x_train,y_train)


# In[20]:


y_train_pred = model.predict(x_train_sm)


# In[21]:


y_train_pred.head()


# In[23]:


residual = (y_train - y_train_pred)


# In[24]:


residual.head()


# In[25]:


sns.distplot(residual)


# In[26]:


sns.scatterplot(x=x_train, y=residual)


# In[28]:


x_test_sm = sm.add_constant(x_test)


# In[29]:


y_pred = model.predict(x_test_sm)


# In[32]:


RMSE = np.sqrt(mean_squared_error(y_test,y_pred))
RMSE
#RMSE(ROOT MEAN SQUARE ERROR)


# In[33]:


r2_score(y_test,y_pred)


# In[34]:


plt.scatter(x_test,y_test)
plt.plot(x_test, 25200 + x_test * 9731.2038,'r')
plt.show()
        


# In[ ]:




