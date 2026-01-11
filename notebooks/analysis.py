#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# In[12]:


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "cleaned" / "isro_mission_launches_cleaned.csv"
# df=pd.read_csv(r'../data/cleaned/isro_mission_launches_cleaned.csv')
df=pd.read_csv(DATA_PATH)
df.head()


# In[13]:


df['Application'].unique()


# In[14]:


df['Application'].value_counts()


# In[15]:


applications=df['Application'].unique()
count_of_applications=df['Application'].value_counts()
application_labels=count_of_applications.index.tolist()
count_by_application=count_of_applications.values.tolist()
xs=[i+1.5 for i in range(len(applications))]
applications
plt.figure(figsize=(14,6))
plt.bar(xs,count_by_application)
plt.xticks(xs,application_labels,rotation=90)
plt.show()


# In[16]:


remarks=df['Remarks'].unique()
count_of_remarks=df['Remarks'].value_counts()
remark_labels=count_of_remarks.index.tolist()
count_by_remark=count_of_remarks.values.tolist()
# xs=[i+1.5 for i in range(len(remarks))]
count_by_remark
plt.figure(figsize=(14,7))
plt.pie(count_by_remark,labels=remark_labels,explode=[0.1,0.2,0.2,0.1,0.1],rotatelabels=90,startangle=45)
# plt.xticks(xs,remark_labels,rotation=90)
plt.show()


# In[17]:


df['Launch Date']=pd.to_datetime(df['Launch Date'])


# In[18]:


year_groups=df.groupby('Launch Date').size()
plt.figure(figsize=(14,6))
year_groups.plot(kind='line')
plt.show()


# In[19]:


df['Orbit Type'].value_counts()


# In[20]:


orbit_type_counts=df['Orbit Type'].value_counts()
orbit_type_labels=orbit_type_counts.index.tolist()
xs_orbit_type=[i+0.5 for i in range(len(orbit_type_counts))]
y_orbit_count=orbit_type_counts.values
plt.figure(figsize=(14,6))
plt.bar(xs_orbit_type,y_orbit_count)
plt.xticks(xs_orbit_type,orbit_type_labels,rotation=90)
plt.show()

