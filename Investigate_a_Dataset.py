#!/usr/bin/env python
# coding: utf-8

# # Project: Investigate a Dataset - [TMDB MOVIES DATASET]

# # Introduction
# 
# TMDB movie dataset that contains information about over 10,000 movies collected from The Movie Database (TMDb).This dataset contains different columns .It has a 21 different columns and 10866 rows.
# 
#  QUESTIONS
#  1.Which month are movies released the most?
#  2.What is the relationship between runtime and Popularity?
#  3.What is the correlation between revenue and budget?
#  4.What is the correlation between revenue and vote count?
#  5.What is the correlation between budget and vote count?

# In[34]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you **document your data cleaning steps in mark-down cells precisely and justify your cleaning decisions.**
# 
# 
# ### General Properties
# > **Tip**: You should _not_ perform too many operations in each cell. Create cells freely to explore your data. One option that you can take with this project is to do a lot of explorations in an initial notebook. These don't have to be organized, but make sure you use enough comments to understand the purpose of each code cell. Then, after you're done with your analysis, create a duplicate notebook where you will trim the excess and organize your steps so that you have a flowing, cohesive report.

# In[36]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
df=pd.read_csv('tmdb-movies.csv')
df.head()


# In[37]:


df.info()


# In[38]:


df.dtypes


# In[39]:


df.duplicated().sum()


# In[40]:


df.describe()


# In[41]:


df.shape


# 
# ### Data Cleaning
# > **Tip**: Make sure that you keep your reader informed on the steps that you are taking in your investigation. Follow every code cell, or every set of related code cells, with a markdown cell to describe to the reader what was found in the preceding cell(s). Try to make it so that the reader can then understand what they will be seeing in the following cell(s).
#  

# In[42]:


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.

#Drop unwanted Columns
df=df.drop(['imdb_id','cast','homepage','tagline','keywords','release_year','overview','director','production_companies'],axis=1)


# In[43]:


df.info()


# In[44]:


#Drop duplicates
df=df.drop_duplicates()


# In[45]:


#Fill Nan 
df=df.fillna('Nan')


# In[46]:


#Check the shape
df.shape


# In[47]:


#Check if there are still null values
df.info()


# In[48]:


#Change dtype of the date column
df['release_date']=pd.to_datetime(df['release_date'])
df.dtypes


# ## Exploratory Data Analysis
# 
# ### Research Question 1 (Which month are movies released the most)

# In[49]:


#Month on which movies are released the most
#First extract the month,since its only month we will use.
total_released=df['release_date'].dt.month.value_counts().sort_index()
months=['January','February','March','April','May','June','July','August','September','October','November','December']
total_released = pd.DataFrame(total_released)
total_released['month'] = months


# In[50]:


#Bar chart showing the month movies were posted mostly!
total_released.plot(x='month',kind='bar',figsize=(15,8))
plt.title("MONTHS WITH MOST POST",fontsize = 15)
plt.xlabel('MONTH',fontsize = 15)
plt.ylabel('TOTAL RELEASED MOVIES',fontsize = 15)


# ### Research Question 2  (Whats the relationship between runtime and popularity!)

# In[51]:


#Whats the relationship between runtime and popularity
#Does runtime affect the popularity of the movie .
#Group by runtime

df.groupby('runtime')['popularity'].mean().plot(figsize = (10,6),xticks=np.arange(0,1000,100))


plt.title("Runtime Against Popularity")
plt.xlabel('Runtime')
plt.ylabel('Mean Popularity')
#This shows that movie within 100-200 minutes are the most watched movies


# ### Summary of findings
# The plot above indicates that movies with runtime between 100 and 200 has higher popularity,which 
# indicates they're the most watched movies .
# 

# ## Research Question 3(What is the correlation between revenue and budget?)

# In[52]:


def To_plot(x,y,a,b,e):
    plt.scatter(x,y)
    plt.xlabel(a)
    plt.ylabel(b)
    plt.title(e)
    plt.show()


# In[53]:


#Correlation between revenue and budget
#revenue against budget
a="Budget"
b="Revenue"
e="Revenue Against Budget"
To_plot(df['revenue'],df['budget'],a,b,e)


# ### Summary of findings
# The plot above shows a positive correlation between budget and revenue
# Which indicates the more budget you spend the more revenue you earn.

# ## What is the correlation between revenue and Vote Counts?

# In[54]:


#Correlation between revenue and vote count
#revenue against vote_count
m="Revenue"
n="Vote Count"
o="Revenue Against Vote Count"
To_plot(df['revenue'],df['vote_count'],m,n,o)


#shows positive correlation between budget spent and Revenue earned:The higher the budget the higher the revenue


# ### Summary of findings
# This plot indicates a positive correlation between Revenue and Vote Counts.Which indicates the higher the rating ,the higher the revenue it generates

# ## What is the correlation between budget and Vote Counts?

# In[55]:


#BUDGET AGAINST VOTE COUNT
#are highly rated movies vs budget
i="Budget"
j="Vote Count"
k="Vote Count With Budget"
To_plot(df['budget'],df['vote_count'],i,j,k)


# ### Summary of findings
# The scatter plot above indicates a positive correlation between vote count and budget.This implies 
# the higher the budget spent ,the higher vote counts(rate)

# ## Conclusions

# 1.September and October is the month most movies are released.
# 2.Movies between 100 and 200 runtime are more popular,People tend to like short movies more than longer ones.
# 3.Revenue and budget has a positive correlation,which actually implies the higher budget you spend the higher revenue you make. 
# 4.Revenue and Vote Count also has a positive correlation,which implies the more people rate the movie the higher the revenue
# 

# ## Limitation
# 1.We don't know how correct this data is.
# 2.We drop so many columns which we can actually make more insights on.

# ## References
# 1.https://github.com/hima888/Investigate-a-Dataset-TMDB-Movie-Data-/blob/master/investigate-a-dataset-template.ipynb
# 2.https://www.python-graph-gallery.com/basic-time-series-with-matplotlib
# 3.https://jovian.ai/rathodajay1202/tmdb-5000-movie-analysis

# In[215]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




