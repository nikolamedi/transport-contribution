#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import numpy as np 
import pandas as pd 
import plotly as py
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('data.csv')


# In[3]:


df.head()


# In[4]:


# Based on guide provided here: https://www.dataquest.io/blog/tutorial-add-column-pandas-dataframe-based-on-if-else-condition/
# Comparing the different columns with the column in focus, setting here the conditions
conditions = [
    (df['Transport'] > df['Power']) & (df['Transport'] > df['Buildings']) & (df['Transport'] > df['Othercomb']) & (df['Transport'] > df['Others']),
    (df['Transport'] < df['Power']) & (df['Transport'] > df['Buildings']) & (df['Transport'] > df['Othercomb']) & (df['Transport'] > df['Others']),
    (df['Transport'] < df['Power']) & (df['Transport'] < df['Buildings']) & (df['Transport'] > df['Othercomb']) & (df['Transport'] > df['Others']),
    (df['Transport'] < df['Power']) & (df['Transport'] < df['Buildings']) & (df['Transport'] < df['Othercomb']) & (df['Transport'] > df['Others']),
    (df['Transport'] < df['Power']) & (df['Transport'] < df['Buildings']) & (df['Transport'] < df['Othercomb']) & (df['Transport'] < df['Others']),
    (df['Transport'] > df['Power']) & (df['Transport'] < df['Buildings']) & (df['Transport'] > df['Othercomb']) & (df['Transport'] > df['Others']),
    (df['Transport'] > df['Power']) & (df['Transport'] < df['Buildings']) & (df['Transport'] < df['Othercomb']) & (df['Transport'] > df['Others']),
    (df['Transport'] > df['Power']) & (df['Transport'] < df['Buildings']) & (df['Transport'] < df['Othercomb']) & (df['Transport'] < df['Others']),
    (df['Transport'] > df['Power']) & (df['Transport'] > df['Buildings']) & (df['Transport'] < df['Othercomb']) & (df['Transport'] > df['Others']),
    (df['Transport'] > df['Power']) & (df['Transport'] > df['Buildings']) & (df['Transport'] < df['Othercomb']) & (df['Transport'] < df['Others']),
    (df['Transport'] < df['Power']) & (df['Transport'] > df['Buildings']) & (df['Transport'] < df['Othercomb']) & (df['Transport'] < df['Others']),
    (df['Transport'] > df['Power']) & (df['Transport'] > df['Buildings']) & (df['Transport'] > df['Othercomb']) & (df['Transport'] < df['Others']),
    (df['Transport'] < df['Power']) & (df['Transport'] < df['Buildings']) & (df['Transport'] > df['Othercomb']) & (df['Transport'] < df['Others']),
    (df['Transport'] < df['Power']) & (df['Transport'] > df['Buildings']) & (df['Transport'] > df['Othercomb']) & (df['Transport'] < df['Others']),
    (df['Transport'] < df['Power']) & (df['Transport'] > df['Buildings']) & (df['Transport'] < df['Othercomb']) & (df['Transport'] > df['Others']),
    (df['Transport'] > df['Power']) & (df['Transport'] < df['Buildings']) & (df['Transport'] > df['Othercomb']) & (df['Transport'] < df['Others'])
    ]

# Setting here for each of the conditions above which value should be added if the condition is met
values = ['Largest sector', 'Second-largest after power', 'Third-largest after power and buildings', 'Fourth-largest after power, buildings and other combustion', 'Fifth-largest after power, building, other combustion and others', 'Second-largest after buildings', 'Third-largest after buildings and other combustion', 'Fourth-largest after buildings, other combustion and others', 'Second-largest after other combustion', 'Third-largest after other combustion and others', 'Fourth-largest after power, other combustions and others', 'Second-largest after others', 'Fourth-largest after power, buildings and others', 'Third-largest after power and others', 'Third-largest after power and other combustion', 'Third-largest after buildings and others']

df['order'] = np.select(conditions, values)

df.head()


# In[5]:


df.to_excel("result.xlsx")

