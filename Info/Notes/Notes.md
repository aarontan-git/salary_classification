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