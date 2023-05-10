import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# ##Race X Past Crimes
# # Load the data
# data = pd.read_csv('/Users/bn/Library/CloudStorage/OneDrive-Personal/Universities/UniLu/Semester 6/Security 2/SPAKE/DSH-COMPAS/Old_Data_Sets/compas-scores-re_col.csv')

# # Remove duplicates by selecting the first instance of each person
# data = data.drop_duplicates(subset='Case_ID', keep='first')

# # Create a scatter plot
# plt.scatter(data['Ethnic_Code_Text'],data['RecSupervisionLevel'])

# # Add axis labels and a title
# plt.xlabel('Race')
# plt.ylabel('Supervision Level')
# plt.title('Relationship between Race and Supervision Level')

# # Display the plot
# plt.show()


# # Load the data
# data = pd.read_csv('/Users/bn/Library/CloudStorage/OneDrive-Personal/Universities/UniLu/Semester 6/Security 2/SPAKE/DSH-COMPAS/Old_Data_Sets/compas-scores-re_col.csv')

# # Remove duplicates by selecting the first instance of each person
# data = data.drop_duplicates(subset='Case_ID', keep='first')

# # Create a scatter plot
# plt.scatter(data['Sex_Code_Text'],data['RecSupervisionLevel'])

# # Add axis labels and a title
# plt.xlabel('Gender')
# plt.ylabel('Supervision Level')
# plt.title('Relationship between Race and Supervision Level')

# # Display the plot
# plt.show()


# # Load the data
# data = pd.read_csv('compas-scores-recidivism.csv')

# # Define colors based on gender
# colors = {1: 'blue', 0: 'red'}

# # Add some random jitter to the y-coordinates of the data points
# jitter = np.random.normal(0, 10000000, len(data))
# data['Case_ID_jittered'] = data['Case_ID'] + jitter

# # Create the scatter plot
# plt.scatter(data['RawScore'], data['Case_ID_jittered'], c=data['Sex_Code_Text_Male'].apply(lambda x: colors[x]))


# # Add axis labels and title
# plt.xlabel('Raw Score')
# plt.ylabel('Case Id')
# plt.title('Raw Score vs. Case Id by Gender')

# # Show the plot
# plt.show()


# ## Ethnicity X Raw Score
# # Load the data 
# data = pd.read_csv('compas-scores-f1.csv')

# # Define colors based on gender
# colors = {"Caucasian": 'blue', "African-American": 'black', "Hispanic": "brown", "Other": "green", "Asian": "yellow", "Native American": 'red'}

# #Keep only the rows where Scale_ID equals 8
# data = data[data['Scale_ID'] == 8]

# # Add some random jitter to the y-coordinates of the data points
# jitter = np.random.normal(0, 10**10, len(data))
# data['Case_ID_jittered'] = data['Case_ID'] + jitter

# # Create the scatter plot
# plt.scatter(data['RawScore'], data['Case_ID_jittered'], c=data['Ethnic_Code_Text'].apply(lambda x: colors[x]))


# # Add axis labels and title
# plt.xlabel('Raw Score')
# plt.ylabel('Ethnicity')
# plt.title('Raw Score vs. Case Id by Ethnicity')

# # Show the plot
# plt.show()


# # ## Age X Raw Score
# # Load the data 
# data = pd.read_csv('compas-scores-recidivism.csv')


# # Create the scatter plot
# plt.scatter(data['RawScore'], data['DateOfBirth'])

# # Add axis labels and title
# plt.xlabel('Raw Score')
# plt.ylabel('Age')
# plt.title('Raw Score vs. Date of Birth')

# # Show the plot
# plt.show()

# ### bar chart crime across sex
# # Load the data
# data = pd.read_csv('compas-scores-f1.csv')

# # Group the data by sex and count the number of cases
# sex_counts = data.groupby('Sex_Code_Text')['Case_ID'].count()

# # Create a bar chart
# ax = sex_counts.plot(kind='bar')

# # Add a title and labels for the axes
# ax.set_title('Number of Crimes by Sex')
# ax.set_xlabel('Sex')
# ax.set_ylabel('Number of Cases')

# # Show the plot
# plt.show()


# ### Stack Bar Ethnicity X Past Crimes
# # Load the data
# data = pd.read_csv('compas-scores-f1.csv')

# #Keep only the rows where Scale_ID equals 8
# data = data[data['Scale_ID'] == 8]

# # Create a pivot table with ethnicity and past crimes as the rows and columns
# pivot_table = pd.pivot_table(data, values='RawScore', index='Ethnic_Code_Text', columns='CustodyStatus', aggfunc='count')

# # Create a stacked bar chart
# ax = pivot_table.plot(kind='bar', stacked=True)

# # Add a title and labels for the axes
# ax.set_title('Past Crimes by Ethnicity')
# ax.set_xlabel('Ethnicity')
# ax.set_ylabel('Number of Cases')

# # Show the plot
# plt.show()


# # Load data from CSV file
# data = pd.read_csv('Old_Data_Sets/compas-scores-reduced.csv')

# #Keep only the rows where Scale_ID equals 8
# data = data[data['Scale_ID'] == 8]

# # Select relevant columns
# risk_and_race = data[['RecSupervisionLevelText', 'Ethnic_Code_Text']]

# # Group data by risk level and race
# grouped_data = risk_and_race.groupby(['RecSupervisionLevelText', 'Ethnic_Code_Text']).size().reset_index(name='count')

# # Pivot data to create stacked bar chart
# pivot_data = grouped_data.pivot(index='RecSupervisionLevelText', columns='Ethnic_Code_Text', values='count')

# # Set colors for each race category
# colors = {"Caucasian": 'blue', "African-American": 'black', "Hispanic": "brown", "Other": "green", "Asian": "yellow", "Native American": 'red'}

# # Create stacked bar chart
# ax = pivot_data.plot(kind='bar', stacked=True, color=[colors[key] for key in pivot_data.columns], figsize=(10, 6))

# # Set labels and title
# ax.set_xlabel('Recidivism Risk Level')
# ax.set_ylabel('Number of Cases')
# ax.set_title('Distribution of Race Categories by Recidivism Risk Level')

# # Set legend with custom colors
# ax.legend(pivot_data.columns, loc='upper left')

# # Show plot
# plt.show()


# ### Marital status
# # load data from csv file
# data = pd.read_csv('Old_Data_Sets/compas-scores-reduced.csv')

# #Keep only the rows where Scale_ID equals 8
# data = data[data['Scale_ID'] == 8]

# # select relevant columns
# past_crimes_and_marital_status = data[['MaritalStatus', 'DisplayText']]

# # group data by marital status and past crimes
# grouped_data = past_crimes_and_marital_status.groupby(['MaritalStatus', 'DisplayText']).size().reset_index(name='count')

# # pivot data to create stacked bar chart
# pivot_data = grouped_data.pivot(index='MaritalStatus', columns='DisplayText', values='count')

# # set colors for each past crimes category
# colors = {'Past Crimes': 'red'}

# # create stacked bar chart
# ax = pivot_data.plot(kind='bar', stacked=True, color=colors.values(), figsize=(12, 6))

# # set labels and title
# ax.set_xlabel('Marital Status')
# ax.set_ylabel('Number of Cases')
# ax.set_title('Distribution of Past Crimes by Marital Status')

# # set legend with custom colors
# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles, colors.keys(), loc='upper right')

# # show plot
# plt.show()

# # load data from csv file
# data = pd.read_csv('Old_Data_Sets/compas-scores-reduced.csv')

# # Keep only the rows where Scale_ID equals 8
# data = data[data['Scale_ID'] == 8]

# # select relevant columns
# risk_and_marital_status = data[['RecSupervisionLevelText', 'MaritalStatus']]

# # group data by risk level and marital status
# grouped_data = risk_and_marital_status.groupby(['RecSupervisionLevelText', 'MaritalStatus']).size().reset_index(name='count')

# # pivot data to create stacked bar chart
# pivot_data = grouped_data.pivot(index='RecSupervisionLevelText', columns='MaritalStatus', values='count')

# # define a color scheme for each marital status category
# colors = {'Single': 'blue', 'Married': 'green', 'Divorced': 'purple', 'Separated': 'red', 'Widowed': 'gray', "Significant Other": 'yellow'}

# pivot_data = pivot_data[colors.keys()]

# # create stacked bar chart
# ax = pivot_data.plot(kind='bar', stacked=True, color=[colors[key] for key in pivot_data.columns], figsize=(12,6))

# # set labels and title
# ax.set_xlabel('Group Risk Level')
# ax.set_ylabel('Number of Cases')
# ax.set_title('Distribution of Marital Status by Group Risk Level')

# # set legend with custom colors
# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles, colors.keys(), loc='upper right')

# # show plot
# plt.show()

# # load data from csv file
# data = pd.read_csv('Old_Data_Sets/compas-scores-reduced.csv')

# # select relevant columns
# race_and_scores = data[['Ethnic_Code_Text', 'ScoreText']]

# # group data by race and COMPAS score categories
# grouped_data = race_and_scores.groupby(['Ethnic_Code_Text', 'ScoreText']).size().reset_index(name='count')

# # pivot data to create stacked bar chart
# pivot_data = grouped_data.pivot(index='Ethnic_Code_Text', columns='ScoreText', values='count')

# # define a color scheme for each COMPAS score category
# colors = {'Low': 'green', 'Medium': 'orange', 'High': 'red'}

# # reorder columns to match order in dictionary
# pivot_data = pivot_data[colors.keys()]

# # create stacked bar chart
# ax = pivot_data.plot(kind='bar', stacked=True, color=[colors[key] for key in pivot_data.columns], figsize=(12,6))

# # set labels and title
# ax.set_xlabel('Ethnic_Code_Text')
# ax.set_ylabel('Number of Cases')
# ax.set_title('Distribution of COMPAS Score Categories by Race')

# # set legend with custom colors
# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles, colors.keys(), loc='upper right')

# # show plot
# plt.show()


# # Load data from CSV file and select relevant columns
# data = pd.read_csv('Old_Data_Sets/compas-scores-reduced.csv')
# data = data[['Sex_Code_Text', 'DecileScore']]

# # Group data by gender and COMPAS score category
# grouped_data = data.groupby(['Sex_Code_Text', 'DecileScore']).size().reset_index(name='count')

# # Calculate proportion of individuals in each group
# total_counts = grouped_data.groupby(['Sex_Code_Text'])['count'].transform('sum')
# grouped_data['proportion'] = grouped_data['count'] / total_counts

# # Pivot data to create stacked bar chart
# pivot_data = grouped_data.pivot(index='Sex_Code_Text', columns='DecileScore', values='proportion')

# # Define color scheme for each COMPAS score category
# colors = {1: 'green', 2: 'blue', 3: 'red', 4: 'orange', 5: 'purple', 6: 'gray', 7: 'pink', 8: 'brown', 9: 'yellow', 10: 'black'}

# # reorder columns to match order in dictionary
# pivot_data = pivot_data[colors.keys()]

# # Create stacked bar chart
# ax = pivot_data.plot(kind='bar', stacked=True, color=[colors[col] for col in pivot_data.columns], figsize=(12,6))

# # Set labels and title
# ax.set_xlabel('Sex_Code_Text')
# ax.set_ylabel('Proportion')
# ax.set_title('Proportion of Males and Females by COMPAS Score Category')

# # Set legend with custom colors
# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles, labels, loc='upper right')

# # Show plot
# plt.show()

# # Load data from csv file
# data = pd.read_csv('Old_Data_Sets/compas-scores-raw.csv')

# # Keep only the rows where "is_recid" equals 1 or -1
# data = data[(data['is_recid'] == 1) | (data['is_recid'] == -1)]

# # Select relevant columns
# age_and_recid = data[['age', 'is_recid']]

# # Create scatter plot
# sns.scatterplot(data=age_and_recid, x='age', y='is_recid')

# # Set labels and title
# plt.xlabel('Age')
# plt.ylabel('Likelihood of Recidivism')
# plt.title('Relationship Between Age and Likelihood of Recidivism')

# # Show plot
# plt.show()

# ### Relationship Between Age and Likelihood of Recidivism
# # load data from csv file
# data = pd.read_csv('compas-scores-recidivism.csv')

# # select relevant columns
# age_and_score = data[['DateOfBirth', 'DecileScore']]

# # create scatter plot
# plt.scatter(age_and_score['DateOfBirth'], age_and_score['DecileScore'], alpha=0.5)

# # set labels and title
# plt.xlabel('DateOfBirth')
# plt.ylabel('COMPAS Recidicism Decile Score')
# plt.title('Relationship Between Age and Likelihood of Recidivism')

# # show plot
# plt.show()

data = pd.read_csv('compas-scores-recidivism.csv')

# categorize individuals into different age groups
age_bins = [0, 20, 35, 45, 60, 75, 100]
age_labels = ['<20', '20-35', '36-45', '46-60', '61-75', '>75']
data['Age_Group'] = pd.cut(data['DateOfBirth'].astype(str).apply(lambda x: 123 - int(x[-2:])), bins=age_bins, labels=age_labels)

# filter relevant columns
compas_age = data[['Age_Group', 'ScoreText']]

# group data by age group and COMPAS score category
grouped_data = compas_age.groupby(['Age_Group', 'ScoreText']).size().reset_index(name='count')

# pivot data to create stacked bar chart
pivot_data = grouped_data.pivot(index='Age_Group', columns='ScoreText', values='count')

# set colors for each COMPAS score category
colors = {'Low': 'green', 'Medium': 'yellow', 'High': 'red'}

# reorder columns to match order in dictionary
pivot_data = pivot_data[colors.keys()]

# create stacked bar chart
ax = pivot_data.plot(kind='bar', stacked=True, color=[colors[key] for key in pivot_data.columns], figsize=(12,6))

# set labels and title
ax.set_xlabel('Age Group')
ax.set_ylabel('Number of Cases')
ax.set_title('Proportion of Individuals in Different Age Categories by COMPAS Score Category')

# set legend with custom colors
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

# show plot
plt.show()