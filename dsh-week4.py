import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

''' LOGISTIC REGRESSION '''
# Load the data
def logRegression(df):
    # Define features and target
    features = df.iloc[: , 9:]
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


def supportVectorMachine(df):
    # Define features and target
    features = df.iloc[: , 9:]
    target = df['RawScore']

    # SVM algorithms are not scale invariant, so it is highly recommended to scale your data
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

    # Create a Support Vector Regression model
    # We use the Radial basis function (RBF) kernel 
    model = SVR(kernel='rbf')

    # Train the model
    model.fit(X_train, y_train)

    # Predict the test set results
    y_pred = model.predict(X_test)

    # Evaluate the model using Root Mean Squared Error (RMSE)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    print('Root Mean Squared Error: ', rmse)

df = pd.read_csv('compas-scores-recidivism.csv')
#logRegression(df)
supportVectorMachine(df)
