# Notes
## Types of Questions in Survey
0. Duration
1. Gender
2. Age
3. Country
4. Highest Level of Education
5. Undergraduate major
6. Title most similar to your current role
7. What industry are you currently in
8. How many years of experience in current role
9. What is your current yearly compensation
10. Does your current employer incorporate ML methods into their business
    - 1 column of different sentences ("i do not know", "we are exploring ML methods", "We recently started .."...etc.)
11. Select an activity that makes up an import part of your role at work
    - 11 choices (11th one is others)
12. What is the primary tool that you use at work to analyze data
    -  6 parts filled with numbers
13. Which of the following IDE have you used in the last 5 years
    - 16 parts (showing different IDES in texts)
14. Which of the following hosted notebooks have you used in the last 5 years
    - 14 parts (Showing different notebooks in texts)
15. Which of the following cloud computing services have you used in the last 5 years
    - 8 parts
16. What programming language do you use on a regular basis
    - 19 parts
17. What specific programming language do you use most often
    - 1 part showing different languages in the same column (not separated as seen in previous questions) + other
18. What programming language would you recommend an aspiring data scientist to learn first?
    - 1 column showing different languages in the same column + other
19. What ML frameworks have you used in the past 5 years
    - 20 columns
20. of the choices that you selected in the previous question, which ML library have you used the most + other
    - 1 column showing different frameworks 
21. what data visualization libraries/tools have you used in the past 5 years
    - 14 columns
22. of the choices you selected in the previous selection, which specific data visualization library tool do you use the most
    - 1 column showing different framework + other
23. Approximately what percent of your time at work is spent actively coding
24. How long have you been writing code to analyze data
25. For how many years have you used ML methods?
26. Do you consider yourself to be a data scientist
27. Which of the following cloud computing products have you used at work in the last 5 years
    - 21 columns
28. which of the following ML products have you used at work in the last 5 years
    - 44 columns
29. which of the following relational database products have you used at work in the last 5 years
    - 29 columns
30. which of the following big data and anlytics products have you used at work in the last  5 years
    - 26 columns
31. Which types of data do you currently interact with most often at work
    - 13 columns
32. What is the type of data that you currently interact with most often at work
    - one column with different words
33. where do you find public datasets?
    - 12 columns
34. during a typical data science project at work, approximately what proportion of your time is devoted to 
    - 6 parts each for gathering data, cleaning data, visualizing data, model building, putting model into production, finding insights in the data and communicating with stakeholders, 
35. What percentage of your current ML/DS training falls under each category
    - self taught, online courses, work, university, kaggle competitions, other, (7 columns)
36. On which online platforms have you begun or completed data science courses
    - 14 columns (Ex. Udacity column, data holds 'udacity' for those thats used it)
37. on which online platform have you spent the most amount of time?
    - 1 column showing different options
38. what are your favorite media sources that report on data science topics
    - 23 columns
39. How do you perceive the quality of online learning platforms and in person bootcamps as compared to the quality of the education provided by traditional brick and mortar institutions
    - 2 parts (online learning platforms vs in person boot camps)
40. which better demonstrates expertise in DS, academic achievements or independent projects?
    - 1 column with different types of text answers
41. How do you perceive the importance of the following topics
    - 3 columns
42. what metrics do you or your organization use to determine whether or not your modelsl were successful
    - 6 columns
43. approximately what percent of your data projects involved exploring unfair bias in the dataset and/or algorithm
    - 1 column ('10-20')
44. what do you find most difficult about ensuring that your algorithms are fair and unbiased
    - 6 columns
45. In what circumstances would you explore model insights and interpret your model's predictions?
    - 6 columns
46. Approximately what percent of your data projects involve exploring model insights?
47. What methods do you prefer for explaining and/or interpreting decisions that are made by ML models?
    - 16 columns
48. Do you consider ML models to be "black boxes" with outputs that are difficult or impossible to explain?
    - various text answers in one column
49. What tools and methods do you use to make your work easy to reproduce?
    - 13 columns
50. what barriers prevent you from making your work even easier to reuse and reproduce?
    - 9 columns


# Notes from Tutorial

## Tutorial 2

### Handling Nan Values
1. drop them
2. fill them with mode or mean
3. replace with "other" values

``` python
# see how many null values are in each column
Salaries.isnull().sum(axis=0)
```

- One row has a missing title = can just remove since its only one row

- what should we do with nan values in the contract type?
    1. replace nan values with "full time" job since there are more of those
    2. replace nan with the mode of the data (mode is full time?)
        - it is possible to have multiple modes = take the most frequent one

- what to do with missing company names?
    1. can look in the posting description

### Cleaning Text data
- vectorizer = CountVectorizer