import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('compas-scores-reduced.csv')



# Drop certain columns from the DataFrame
cols_to_drop = ['Person_ID', 'AssessmentID', 'LastName','FirstName', 'MiddleName', 
                'ScaleSet', "Screening_Date", "RecSupervisionLevelText", "DisplayText", "IsCompleted", "IsDeleted"]
df = df.drop(cols_to_drop, axis=1)

# Export the updated DataFrame to a new CSV file
df.to_csv('compas-scores-re_col.csv', index=False)


# Print the first 5 rows of the updated DataFrame
print('First 5 rows of the updated CSV file:')
print(df.head())