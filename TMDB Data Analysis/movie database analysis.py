
# coding: utf-8

# In[39]:


# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[40]:


# load dataframe
movies_data = pd.read_csv('tmdb-movies.csv')
movies_data.info()


# In[41]:


# dropping usless columns
useless_columns = ['imdb_id' , 'tagline' , 'homepage' , 'budget_adj' , 'revenue_adj' , 'vote_count' , 'vote_average' , 'production_companies' , 'overview' , 'keywords' , 'id']

movies_data = movies_data.drop(useless_columns , 1)


# In[42]:


# checking and dropping duplicates 
sum(movies_data.duplicated())
movies_data.drop_duplicates(keep = 'first' , inplace = True)
sum(movies_data.duplicated())


# In[43]:


# replacing 0's with NaN
change_list = ['revenue' , 'budget']
movies_data[change_list] = movies_data[change_list].replace(0 , np.NAN)

# Now dropping NAN from the particular columns
movies_data.dropna(subset = change_list , inplace = True)
movies_data.info()


# In[44]:


# checking and changing datatypes
movies_data.dtypes

# changing the dtypes of budget and revenue columns
change_dtypes = ['budget' , 'revenue']
movies_data[change_dtypes] = movies_data[change_dtypes].applymap(np.int64)


# In[45]:


# for calculating profit of all movies and then storing them in a seperate column,we will use the .insert() function
movies_data.insert(2 , 'profit_earned' , movies_data['revenue'] - movies_data['budget'])


# In[46]:


# index of the movie which earned the most profit
movies_data['profit_earned'].idxmax()

# getting details about that movie using the idxmax returned
pd.DataFrame(movies_data.loc[1386])


# In[47]:


# index of the movie which earned minimum profit
movies_data['profit_earned'].idxmin()

# getting details about that movie using the idxm returned
pd.DataFrame(movies_data.loc[2244])


# In[48]:


# getting the index for the longest movie
movies_data['runtime'].idxmax()

# getting details for the longest movie
pd.DataFrame(movies_data.loc[2107])


# In[49]:


# getting the index for the shortest movie
movies_data['runtime'].idxmin()

# getting details for the shortest movie
pd.DataFrame(movies_data.loc[5162])


# In[50]:


# getting the index for the movie with higest budget
movies_data['budget'].idxmax()

# getting details for the movie with higest budget
pd.DataFrame(movies_data.loc[2244])


# In[51]:


# getting the index for the movie with lowest budget
movies_data['budget'].idxmin()

# getting details for the movie with lowest budget
pd.DataFrame(movies_data.loc[2618])


# In[52]:


# getting the index for the movie with higest revenue
movies_data['revenue'].idxmax()

# getting details for the movie with higest budget
pd.DataFrame(movies_data.loc[1386])


# In[53]:


# getting the index for the movie with lowest revenue
movies_data['revenue'].idxmin()


# getting details for the movie with lowest revenue
pd.DataFrame(movies_data.loc[5067])


# In[54]:


# getting average runtime for movies
movies_data['runtime'].mean()

# plotting the histograme for runtime of all movies
plt.figure(figsize = (10 , 5))
plt.hist(movies_data['runtime'])
plt.xlabel('runtime')
plt.ylabel('no of movies')
plt.show()


# In[57]:


# plotting a swarmplot of runtime using seaborn

plt.figure(figsize = (10 , 5))
sns.swarmplot(movies_data['runtime'])
plt.xlabel('runtime')
plt.ylabel('no of movies')
plt.show()


# In[58]:


# plotting a boxplot of runtime using seaborn

plt.figure(figsize = (10 , 5))
sns.boxplot(movies_data['runtime'])
plt.xlabel('runtime')
plt.ylabel('no of movies')
plt.show()


# In[59]:


movies_data['runtime'].describe()


# In[65]:


# plotting a graph of year of release vs profits earned

profits_earned_all_years = movies_data.groupby('release_year')['profit_earned'].sum()
plt.figure(figsize = (10 , 5))
plt.plot(profits_earned_all_years)
plt.xlabel('years')
plt.ylabel('profits_earned')
plt.show()


# In[72]:


# now we will analyse the most profitable movies in the light of the fact that we will create a new list which contains only those movies which have earned $ 50 million or more

most_profitable_movies = movies_data[movies_data['profit_earned'] >=50000000]
most_profitable_movies.describe()


# In[77]:


# we will define a function in order to calculate average budge , average profit and average runtime
def average_of(column):
    return most_profitable_movies[column].mean()

# calling the above function
print("the average budget of most profitable movies is $ " + str(int(average_of('budget'))))

print("the average  profit of most profitable movies is $ " + str(int(average_of('profit_earned'))))

print("the average runtime of most profitable movies is (in minutes) " + str(int(average_of('runtime'))))

