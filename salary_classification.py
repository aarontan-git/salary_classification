import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


data = pd.read_csv('Kaggle_Salary.csv')

# # show heatmap of all the nan values
# fig, ax = plt.subplots(figsize=(12,8))
# sns.heatmap(data.isnull(), cmap='coolwarm', yticklabels=False, cbar=False, ax=ax)
# plt.show()

# number of unique countries
# countries_count = data.Q3.value_counts()
# print(countries_count)

# countries_count.index[countries_count <100]

# print(data.Q3.nunique())

salary_count = data.Q9.value_counts()
salary_count.plot