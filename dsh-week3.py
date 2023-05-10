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

# load data from csv file
data = pd.read_csv('Old_Data_Sets/compas-scores-reduced.csv')

# Keep only the rows where Scale_ID equals 8
data = data[data['Scale_ID'] == 8]

# select relevant columns
risk_and_marital_status = data[['RecSupervisionLevelText', 'MaritalStatus']]

# group data by risk level and marital status
grouped_data = risk_and_marital_status.groupby(['RecSupervisionLevelText', 'MaritalStatus']).size().reset_index(name='count')

# pivot data to create stacked bar chart
pivot_data = grouped_data.pivot(index='RecSupervisionLevelText', columns='MaritalStatus', values='count')

# define a color scheme for each marital status category
colors = {'Single': 'blue', 'Married': 'green', 'Divorced': 'purple', 'Separated': 'red', 'Widowed': 'gray', "Significant Other": 'yellow'}

# create stacked bar chart
ax = pivot_data.plot(kind='bar', stacked=True, color=[colors[key] for key in pivot_data.columns], figsize=(12,6))

# set labels and title
ax.set_xlabel('Recidivism Risk Level')
ax.set_ylabel('Number of Cases')
ax.set_title('Distribution of Marital Status by Recidivism Risk Level')

# set legend with custom colors
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, colors.keys(), loc='upper right')

# show plot
plt.show()





