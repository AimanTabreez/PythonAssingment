#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1 = pd.read_csv("Downloads/2015.csv",float_precision='round_trip')


# In[3]:


df1.head()


# In[5]:


df2=df1.round({"Happiness Score":2, "Health (Life Expectancy)":2, "Trust (Government Corruption)":2,"Generosity":2})


# In[6]:


df2


# In[7]:


df3=df2.drop(['Region','Happiness Rank','Standard Error','Economy (GDP per Capita)','Family','Freedom','Dystopia Residual'],axis=1)


# In[30]:


df3.head()


# In[9]:


df3=df3.rename(columns={"Trust (Government Corruption)":"Trust",
                        "Health (Life Expectancy)":"Healthy Life Expectancy",
                        "Country":"Country Name"})


# In[31]:


df3.head()


# In[11]:


dg1= pd.read_csv("Downloads/2020.csv",float_precision='round_trip')


# In[12]:


dg1.head()


# In[14]:


dg1=dg1.drop(['Regional indicator',
              'Standard error of ladder score',
              'upperwhisker',
              'lowerwhisker',
              'Logged GDP per capita',
              'Social support',
              'Freedom to make life choices',
              'Ladder score in Dystopia',
              'Explained by: Log GDP per capita',
              'Explained by: Social support',
              'Explained by: Healthy life expectancy',
              'Explained by: Freedom to make life choices',
              'Explained by: Generosity',
              'Explained by: Perceptions of corruption',
              'Dystopia + residual'],axis=1)


# In[15]:


dg1


# In[16]:


dg2=dg1.round({"Ladder score":2, "Healthy life expectancy":2, "Generosity":2,"Perceptions of corruption":2})


# In[17]:


dg2


# In[19]:


dg2=dg2.rename(columns={"Country name":"Country Name"})


# In[20]:


dg2


# In[27]:


x1 = pd.merge(df3,dg2,on="Country Name")
x1.head()


# In[28]:


x1=x1.rename(columns={"Generosity_x":"Generosity_2015",
                        "Generosity_y":"Generosity_2020",
                        "Healthy Life Expectancy":"Healthy Life Expectancy(2015)",
                      "Healthy life expectancy":"Healthy Life Expectancy(2020)"})


# In[29]:


x1.head()


# In[32]:


get_ipython().system('pip install alchemy')


# In[41]:


from sqlalchemy import create_engine
p_engine=create_engine("postgresql://postgres:root@localhost:5432/world_happiness")


# In[43]:


df = pd.DataFrame(df3)
df.to_csv('Downloads/2015sql.csv')


# In[45]:


qq=pd.read_csv('Downloads/2015sql.csv',index_col=False)
qq.to_sql('2015sql',p_engine,if_exists='replace',index=False)   #only 2015 data


# In[49]:


df = pd.DataFrame(dg2)
df.to_csv('Downloads/2020sql.csv')


# In[50]:


qqq=pd.read_csv('Downloads/2020sql.csv',index_col=False)
qqq.to_sql('2020sql',p_engine,if_exists='replace',index=False)     #only 2020 data


# In[51]:


df = pd.DataFrame(x1)
df.to_csv('Downloads/1520sql.csv')


# In[52]:


qqqq=pd.read_csv('Downloads/1520sql.csv',index_col=False)
qqqq.to_sql('1520sql',p_engine,if_exists='replace',index=False)    #Both 2015 and 2020 data after merging,transforming and cleaning the data  


# In[ ]:




