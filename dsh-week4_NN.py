import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import confusion_matrix
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the dataset
data = pd.read_csv('compas-scores-recidivism.csv')  # Replace with the actual path to your dataset file

# Separate features and target variable
X = data[['RawScore', 'Sex_Code_Text_Female']]
# y = data['Ethnic_Code_Text_Caucasian']
y = data['Ethnic_Code_Text_African-American']
# y = data['Sex_Code_Text_Male']

# # Perform one-hot encoding for the 'ScoreText' feature
# onehot_encoder = OneHotEncoder(sparse=False, drop='first')
# score_text_encoded = onehot_encoder.fit_transform(data[['ScoreText']])
# score_text_columns = onehot_encoder.get_feature_names_out(['ScoreText'])
# X = pd.concat([X, pd.DataFrame(score_text_encoded, columns=score_text_columns)], axis=1)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the neural network model
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='softmax'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, y_train, epochs=100, batch_size=32)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f'Test Loss: {loss:.4f}')
print(f'Test Accuracy: {accuracy:.4f}')


# Make predictions on the test set
y_pred_probs = model.predict(X_test_scaled)
y_pred = (y_pred_probs > 0.5).astype(int)

# Create a confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)