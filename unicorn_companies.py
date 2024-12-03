#!/usr/bin/env python
# coding: utf-8

# ## Introduction
# 
# In this activity, I will discover characteristics of a dataset and use visualizations to analyze the data. This will utilize skills in **exploratory data analysis (EDA)** and functions that visualize data. 
# 
# In this activity, I will provide insights to an investing firm. To help them decide which companies to invest in next, the firm wants insights into **unicorn companies**–companies that are valued at over one billion dollars. The data I used for this task provides information on over 1,000 unicorn companies, including their industry, country, year founded, and select investors. I will use this information to gain insights into how and when companies reach this prestigious milestone and to make recommendations for next steps to the investing firm.

# ### Import libraries and packages 
# 
# First, I import the relevant Python libraries and modules. Use the `pandas` library and the `matplotlib.pyplot` module.

# In[1]:


# Import libraries and packages

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


# ### Load the dataset into a DataFrame
# 

# In[2]:


# Load data from the csv file into a DataFrame and save in a variable

companies = pd.read_csv("Unicorn_Companies.csv")


# ### Explore the dataset

# In[3]:


# Display the first 10 rows of the data

companies.head(10)


# 
# 
# - The "Select Investors" column represents the top investors in the company.

# In[4]:


# How large the dataset is

companies.size


# 
# - The size of the dataset is 10740. This means that there are 10740 values in total across the whole dataset.

# In[5]:


# Shape of the dataset

companies.shape


# 
# - According to this dataset, there are 1074 unicorn companies as of March 2022, and this dataset also shows 10 aspects of each company. 

# In[6]:


# Get information


companies.info()


# 
# - `Dtype` is listed as `int64` in the `Year Founded` column. This means that the year a company was founded is represented as an integer. I will need to switch this to datetime.

# - `Dtype` is listed as `object` for the `Date Joined` column. This means that the date a company became a unicorn is represented as an object, another issue. 

# ## Find descriptive statistics

# In[7]:


### Get descriptive statistics

companies.describe()


# - The minimum value in the `Year Founded` column is 1919. This means that this dataset does not contain data on unicorn companies founded before 1919.

# 
# - The maximum value in the `Year Founded` column is 2021. This means that this dataset does not include data on unicorn companies founded after 2021.

# In[8]:


# Use pd.to_datetime() to convert Date Joined column to datetime 
# Update the column with the converted values

companies["Date Joined"] = pd.to_datetime(companies["Date Joined"])


# In[9]:


# Use .info() to confirm that the update actually took place

companies.info()


# In[10]:


# I am going to create a year joined column. Use .dt.year to extract year component from Date Joined column
# Add the result as a new column named Year Joined to the DataFrame

companies["Year Joined"] = companies["Date Joined"].dt.year


# In[11]:


# Use .head() to confirm that the new column did get added

companies.head()


# ## Results and evaluation

# In[12]:


# Sample the data

companies_sample = companies.sample(n = 50, random_state = 42)


# In[13]:


# Prepare data for plotting

# Create new `years_till_unicorn` column 
companies_sample["years_till_unicorn"] = companies_sample["Year Joined"] - companies_sample["Year Founded"]

# Group the data by `Industry`. For each industry, get the max value in the `years_till_unicorn` column.
grouped = (companies_sample[["Industry", "years_till_unicorn"]]
           .groupby("Industry")
           .max()
           .sort_values(by="years_till_unicorn")
          )
grouped


# Now, create a bar plot.

# In[14]:


# Create bar plot
# with Industry column as the categories of the bars
# and the difference in years between Year Joined column and Year Founded column as the heights of the bars

plt.bar(grouped.index, grouped["years_till_unicorn"])

# Set title


plt.title("Bar plot of maximum years taken by company to become unicorn per industry (from sample)")

# Set x-axis label

plt.xlabel("Industry")

# Set y-axis label

plt.ylabel("Maximum number of years")

# Rotate labels on the x-axis as a way to avoid overlap in the positions of the text  

plt.xticks(rotation=45, horizontalalignment='right')

# Display the plot

plt.show()


# - This bar plot shows that for this sample of unicorn companies, the largest value for maximum time taken to become a unicorn occurred in the Heath and Fintech industries, while the smallest value occurred in the Consumer & Retail industry.

# In[15]:


# Create a column representing company valuation as numeric data

# Create new column
companies_sample['valuation_billions'] = companies_sample['Valuation']
# Remove the '$' from each value
companies_sample['valuation_billions'] = companies_sample['valuation_billions'].str.replace('$', '')
# Remove the 'B' from each value
companies_sample['valuation_billions'] = companies_sample['valuation_billions'].str.replace('B', '')
# Convert column to type int
companies_sample['valuation_billions'] = companies_sample['valuation_billions'].astype('int')
companies_sample.head()


# In[16]:


# Prepare data for modeling
grouped = (companies_sample[["Industry", "valuation_billions"]]
           .groupby("Industry")
           .max()
           .sort_values(by="valuation_billions")
          )
grouped


# In[17]:


# Create bar plot
# with Industry column as the categories of the bars
# and new valuation column as the heights of the bars


plt.bar(grouped.index, grouped["valuation_billions"])

# Set title


plt.title("Bar plot of maximum unicorn company valuation per industry (from sample)")

# Set x-axis label

plt.xlabel("Industry")

# Set y-axis label

plt.ylabel("Maximum valuation in billions of dollars")

# Rotate labels on the x-axis as a way to avoid overlap in the positions of the text  

plt.xticks(rotation=45, horizontalalignment='right')

# Display the plot

plt.show()


# 
# - This bar plot shows that for this sample of unicorn companies, the highest maximum valuation occurred in the Artificial Intelligence industry, while the lowest maximum valuation occurred in the Auto & transportation, and Consumer & retail industries.

# ## Considerations
# 
# **Findings**
# 
# - There are 1074 unicorn companies represented in this dataset.
# - Some companies took longer to reach unicorn status but have accrued high valuation as of March 2022. Companies could take longer to achieve unicorn status for a number of reasons, including requiring more funding or taking longer to develop a business model. 
# 
# **Recommendations**
# 
# - Identify the main industries that the investing firm is interested in investing in. 
# - Select a subset of this data that includes only companies in those industries. 
# - Analyze that subset more closely. Determine which companies have higher valuation but do not have as many investors currently. They may be good candidates to consider investing in. 

# **References**
# 
# Bhat, M.A. (2022, March). [*Unicorn Companies*](https://www.kaggle.com/datasets/mysarahmadbhat/unicorn-companies). 
# 
