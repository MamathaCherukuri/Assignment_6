#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ###1 Read the dataset using pandas

# In[2]:


tags_df=pd.read_csv("tags.csv")


# In[3]:


tags_df.head()


# In[4]:


ratings_df=pd.read_csv("ratings.csv")


# In[5]:


ratings_df.head()


# In[50]:


movies_df=pd.read_csv("movies.csv")


# In[51]:


movies_df.head()


# ###2 Extract the first row from tags and print its type

# In[9]:


tags_df.iloc[0,:]


# ###3 Extract row 0,11,2000 from tags and print its type

# In[11]:


tags_df.iloc[0,:]


# In[12]:


tags_df.iloc[11,:]


# In[13]:


tags_df.iloc[2000,:]


# ###4 print index columns of a data frame

# In[15]:


tags_df.index


# In[16]:


tags_df.columns.values.tolist()


# ###5Calculate descriptive statistics for the ratings column of the ratings data data frame
# verify using describe

# In[18]:


ratings_df["rating"].describe()


# ###6 Filter out ratings with rating >5

# In[25]:



rating_gt_5=ratings_df[ratings_df.rating >5.0]
rating_gt_5


# ###7 Find how many null values, missing values are present.Deal
# with them. Print out how many rows have been modified.

# In[28]:


ratings_df.isnull().values.any()


# In[29]:


tags_df.isnull().values.any()


# In[30]:


movies_df.isnull().values.any()


# In[31]:


ratings_df.isnull().sum()


# In[32]:


tags_df.isnull().sum()


# In[33]:


movies_df.isnull().sum()


# ###8 Filter out movies from the movies DataFrame that are 
# of type "Animation"

# In[35]:


movies_df_Anim=movies_df[movies_df.genres =="Animation"]
movies_df_Anim


# In[ ]:


###9 Find the avarage rating of movies


# In[37]:


ratings_df["rating"].mean()


# In[ ]:


###10 Perform an inner join of movies and tags based on movieid


# In[40]:


merged_df=pd.merge(movies_df,tags_df,on="movieId")
merged_df.head()


# In[41]:


merged_df1=pd.merge(movies_df,ratings_df,on="movieId")
merged_df1.head()


# ###11 Print out the 5 movies that belong to the Comedy genre and have a rating greater than 4

# In[43]:


merged_df1[(merged_df1.rating >= 4.0) & (merged_df1.genres == 'Comedy')]


# In[ ]:


### 12.Split "genres in to multiple columns"


# In[52]:


from sklearn.preprocessing import MultiLabelBinarizer


# Binarise labels
mlb = MultiLabelBinarizer()
expandedLabelData = mlb.fit_transform(movies_df["genres"])
labelClasses = mlb.classes_


# Create a pandas.DataFrame from our output
expandedLabels = pandas.DataFrame(expandedLabelData, columns=labelClasses)


# In[46]:


movies_df.head()


# In[ ]:


###13. Extract year from title (1995)


# In[ ]:





# In[ ]:




