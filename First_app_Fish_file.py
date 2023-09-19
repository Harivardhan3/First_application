#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv('C:/Users/Checkout/First_app_Fish_file.csv')

Fig = px.bar(df, x= 'Species', y = 'Weight', title = 'Distribution of the dimensions of the Fish')

st.plotly_chart(Fig)


# In[ ]:




