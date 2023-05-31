import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('compas-raw-final.csv')

# new_data = df[['Sex_Code_Text', 'Ethnic_Code_Text', 'Scale_ID', 'RawScore', 'DecileScore', 'ScoreText']]

# new_data = new_data[new_data['Scale_ID'] == 8]

# # Define the columns to scale
# cols_to_scale = ['RawScore']

# # Perform min-max scaling for the selected columns
# scaler = MinMaxScaler()
# new_data[cols_to_scale] = scaler.fit_transform(new_data[cols_to_scale])

# # Round all values in a specific column to 4 digits after the decimal point
# new_data['RawScore'] = new_data['RawScore'].round(4)

# cols_to_encode = ['Sex_Code_Text', 'Ethnic_Code_Text']

# df_encoded = pd.get_dummies(new_data, columns=cols_to_encode)

# df_encoded = df_encoded * 1

# # Export the updated DataFrame to a new CSV file
# df_encoded.to_csv('compas-raw-final.csv', index=False)


# print(df_encoded.head(5))

# Count the number of rows in the DataFrame
num_rows = df.shape[0]

print(f'The DataFrame has {num_rows} rows.')
