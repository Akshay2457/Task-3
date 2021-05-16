#!/usr/bin/env python
# coding: utf-8

# # Author: Kodoori Akshay
# ##Task3- To perform 'Exploratory Data Analysis' on 'SampleSuperStore' dataset

# # importing libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# # Data loading and Cleaning

# In[2]:


#read the dataset
data = pd.read_csv("C:/Users/Akshay/Downloads/SampleSuperstore.csv")
data


# In[3]:


data.info()


# In[4]:


data.shape


# In[5]:


data.describe()


# In[6]:


data.isnull().sum()


# In[7]:


unique = data.nunique()
unique = unique[unique.values==1]
unique


# In[8]:


data.columns


# In[9]:


data.duplicated().sum()


# In[10]:


data.nunique()


# In[11]:


data['Postal Code'] = data['Postal Code'].astype('object')


# In[12]:


data.drop_duplicates(subset=None,keep='first',inplace=True)
data.duplicated().sum()


# # Exploratory Data Analysis

# In[14]:


corr = data.corr()
sns.heatmap(corr,annot=True,cmap='Greens')


# In[15]:


#dropping postal code columns
data = data.drop(['Postal Code'],axis = 1)


# In[16]:


sns.pairplot(data, hue = 'Ship Mode')


# In[17]:


data['Ship Mode'].value_counts()


# In[18]:


sns.countplot(x=data['Ship Mode'])


# In[19]:


#valuecounts for segment
data['Segment'].value_counts()


# In[20]:


#plotting pair plot
sns.pairplot(data,hue = 'Segment')


# In[21]:


sns.countplot(x = 'Segment',data = data, palette = 'rainbow')


# In[22]:


data['Category'].value_counts()


# In[23]:


sns.countplot(x='Category',data=data,palette='tab10')


# In[24]:


sns.pairplot(data,hue='Category')


# In[25]:


data['Sub-Category'].value_counts()


# In[26]:


plt.figure(figsize=(15,12))
data['Sub-Category'].value_counts().plot.pie(autopct='dark')
plt.show()


# In[27]:


data['State'].value_counts()


# In[28]:


data.hist(figsize=(10,10),bins=50)
plt.show()


# In[29]:


fig,ax=plt.subplots(figsize=(20,8))
ax.scatter(data['Sales'],data['Profit'])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
plt.show()


# In[30]:


plt.figure(figsize=(10,8))
data['Region'].value_counts().plot.pie(autopct = '%1.1f%%')
plt.show()


# In[31]:


data.groupby('Segment')[['Profit','Sales']].sum().plot.bar(color=['orange','darkblue'],figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# In[32]:


ps = data.groupby('State')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['red','blue'],figsize=(15,8))
plt.title('Profit/loss & Sales across states')
plt.xlabel('States')
plt.ylabel('Profit/loss & Sales')
plt.show()


# In[33]:


ps = data.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['purple','pink'],figsize=(15,8))
plt.title('Profit/loss & Sales across states')
plt.xlabel('Sub-Category')
plt.ylabel('Profit/loss & Sales')
plt.show()


# In[34]:


t_states = data['State'].value_counts().nlargest(10)
t_states

