import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

''' LOGISTIC REGRESSION '''
# Load the data
df = pd.read_csv('compas-scores-recidivism.csv')

# Define features and target
#features = df.drop(['RawScore', 'Scale_ID', 'Case_ID', 'ScaleSet_ID', 'AssessmentReason', 'ScoreText'], axis=1)
features = df.iloc[: , 9:]
print(features.head)
target = df['RawScore'].apply(lambda x: 1 if x > 0.07 else 0) #if the raw score is medium or high give it one else 0


# Split the data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Create a Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predict the test set results
y_pred = model.predict(X_test)

# Evaluate the model
print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

''' SUPPORT VECTOR MACHINE'''