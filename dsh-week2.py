import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('compas-scores-re_col.csv')



### Use the below to drop the irrelevant columns of the csv reduced file(2000 lines).
# # Drop certain columns from the DataFrame
# cols_to_drop = ['Person_ID', 'AssessmentID', 'LastName','FirstName', 'MiddleName', 
#                 'ScaleSet', "Screening_Date", "RecSupervisionLevelText", "DisplayText", "IsCompleted", "IsDeleted"]
# df = df.drop(cols_to_drop, axis=1)

# # Export the updated DataFrame to a new CSV file
# df.to_csv('compas-scores-re_col.csv', index=False)


# # Print the first 5 rows of the updated DataFrame
# print('First 5 rows of the updated CSV file



### One-Hot Encoding 
# # Define the columns for which to perform one-hot encoding
# cols_to_encode = ['Agency_Text', 'Sex_Code_Text', 'Ethnic_Code_Text', "Language", "LegalStatus", 
#                     "CustodyStatus", "MaritalStatus"]

# # Perform one-hot encoding for the selected columns
# df_encoded = pd.get_dummies(df, columns=cols_to_encode)

# # Print the first 5 rows of the encoded DataFrame
# print('First 5 rows of the one-hot encoded DataFrame:')
# print(df_encoded.head())

# # Export the updated DataFrame to a new CSV file
# df_encoded.to_csv('compas-scores-encoding.csv', index=False)



### Deal with continuous features and round them up to 4 digits after decimal point
# Load the dataset into a pandas DataFrame
# df_cf = pd.read_csv('compas-scores-encoding.csv')

# # Define the columns to scale
# cols_to_scale = ['RawScore']

# # Perform min-max scaling for the selected columns
# scaler = MinMaxScaler()
# df_cf[cols_to_scale] = scaler.fit_transform(df_cf[cols_to_scale])

# # Round all values in a specific column to 4 digits after the decimal point
# df_cf['RawScore'] = df_cf['RawScore'].round(4)

# df_cf.to_csv('compas-scores-cf.csv', index=False)

