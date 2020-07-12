import pandas as pd
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset?
    race_count=df['race'].value_counts()

    # What is the average age of men?
    averaga_age_men=round(df.loc[df['sex']=='Male','age'].mean(),1)
    # df.loc access a group of rows and columns by label(s) or a boolean array.

    # What is the percentage of people who have a Bachelors degree?
    percentage_bachelors=round(float(((df['education']== 'Bachelors').sum())/len(df))*100,1)

    # What percentage of the people with AND without 'education' equal to 'Bachelors' and 'Masters', or 'Doctorate' also have a 'salary' of '>50'
    # Note: Every row of data has salary of either '>50K' or '<=50K'

    # with or without 'Bachelors','Masters', or 'Doctorate'
    higher_education=df.loc[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lower_education=df.loc[~df['education'].isin(['Bachelor', 'Masters','Doctorate'])]

    # percentage with salary > 50K
    higher_education_rich=round((higher_education['salary']=='>50K').sum()/len(higher_education)*100,1)
    lower_education_rich=round((lower_education['salary']=='>50K').sum()/len(lower_education)*100,1)