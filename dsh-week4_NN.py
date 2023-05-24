import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


data = pd.read_csv('compas-scores-recidivism.csv')  # Replace with the actual path to your dataset file

X = data[['Ethnic_Code_Text_Caucasian', 'RawScore']]
y = data['ScoreText']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='softmax'))  # Assuming 3 classes for ScoreText: Low, Medium, High


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

y_train_encoded = pd.get_dummies(y_train)
y_test_encoded = pd.get_dummies(y_test)


model.fit(X_train_scaled, y_train_encoded, epochs=100, batch_size=32)

loss, accuracy = model.evaluate(X_test_scaled, y_test_encoded)
print(f'Test Loss: {loss:.4f}')
print(f'Test Accuracy: {accuracy:.4f}')

