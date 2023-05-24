import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
import matplotlib.pyplot as plt
from sklearn import svm
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
    print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))


def supportVectorMachine(df, search):
    # Define features and target
    features = df.iloc[: , 9:]
    target = df['RawScore'].apply(lambda x: 1 if x > 0.07 else 0) #if the raw score is medium or high give it one else 0

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    #Code to use to find the best C and gamma values
    if search == True:
        param_distributions = {
            'C': uniform(loc=0, scale=10), 
            'gamma': reciprocal(0.001, 0.1), 
            'kernel': ['rbf', 'poly', 'sigmoid'],
        }
        # Create a SVC model
        model = svm.SVC()

        # Create the RandomizedSearchCV model
        rnd_search_cv = RandomizedSearchCV(model, param_distributions, n_iter=1000, verbose=3, cv=5, random_state=42)

        rnd_search_cv.fit(X_train, y_train)

        print("Best parameters: ", rnd_search_cv.best_params_)

        # Predict the test set results
        y_pred = rnd_search_cv.predict(X_test)

        # Evaluate the model using Root Mean Squared Error (RMSE)
        print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

    else:
        # Create a Support Vector Regression model
        # We use the Radial basis function (RBF) kernel 
        model = svm.SVC(kernel='sigmoid', C=3.7882156555691573, gamma=0.008203523727453832)

        # Train the model
        model.fit(X_train, y_train)

        # Predict the test set results
        y_pred = model.predict(X_test)
        
        print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))
        cm = confusion_matrix(y_test, y_pred)
        print("Confusion Matrix: \n", cm)

        # Plot the confusion matrix
        plot_confusion_matrix(model, X_test, y_test)
        plt.show()


df = pd.read_csv('compas-scores-recidivism.csv')
logRegression(df)
supportVectorMachine(df, False)
