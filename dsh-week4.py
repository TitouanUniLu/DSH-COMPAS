import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import reciprocal, uniform

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
    print(y_pred)    # Evaluate the model
    print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


def supportVectorMachine(df, search):
    # Define features and target
    features = df.iloc[: , 9:]
    target = df['RawScore']

    # SVM algorithms are not scale invariant, so it is highly recommended to scale your data
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)
    
    #Code to use to find the best C and gamma values
    if search == True:

        param_distributions = {"gamma": reciprocal(0.001, 0.1), "C": uniform(1, 10), "epsilon": uniform(0.01, 1.0)}
        rnd_search_cv = RandomizedSearchCV(SVR(), param_distributions, n_iter=100, verbose=2, cv=5, random_state=42)
        rnd_search_cv.fit(X_train, y_train)

        print("Best parameters: ", rnd_search_cv.best_params_)

        # Predict the test set results
        y_pred = rnd_search_cv.predict(X_test)

        # Evaluate the model using Root Mean Squared Error (RMSE)
        rmse = mean_squared_error(y_test, y_pred, squared=False)

        print('Root Mean Squared Error: ', rmse)
        print(y_pred)
    else:
        # Create a Support Vector Regression model
        # We use the Radial basis function (RBF) kernel 
        model = SVR(kernel='sigmoid', C=7.0642905965958995, epsilon=0.01919705161662965, gamma=0.001595670021065662)

        # Train the model
        model.fit(X_train, y_train)

        # Predict the test set results
        y_pred = model.predict(X_test)

        # Evaluate the model using Root Mean Squared Error (RMSE)
        rmse = mean_squared_error(y_test, y_pred, squared=False)

        print('Root Mean Squared Error: ', rmse)
        print(y_pred)

df = pd.read_csv('compas-scores-recidivism.csv')
#logRegression(df)
supportVectorMachine(df, True)
