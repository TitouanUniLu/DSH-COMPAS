import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import reciprocal, uniform
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


''' LOGISTIC REGRESSION '''
# Load the data
def logRegression(df, search):
    # Define features and target
    features = df.iloc[: , 9:]
    target = df['RawScore'].apply(lambda x: 1 if x > 0.07 else 0) #if the raw score is medium or high give it one else 0
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    if search == True:
        # Define the hyperparameter search space
        param_grid = {
            'C': np.logspace(-4, 4, 20),  # creates a range of 20 values evenly spaced on a log scale between 10^-4 and 10^4
            'tol': reciprocal(0.0001, 0.1),
            'penalty': ['l1', 'l2', 'elasticnet'],  # 'elasticnet' and 'none' are also valid options we decided to opt out of None as it was introducing too many error messages
            'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
            'l1_ratio': np.linspace(0, 1, 10)  # only used when penalty='elasticnet'
        }

        

        # Create a Logistic Regression model
        model = LogisticRegression(max_iter=100000)

        '''# Create a RandomizedSearchCV instance
        random_search = GridSearchCV(model, param_grid, cv=3)'''
        # Create a RandomizedSearchCV instance
        random_search = RandomizedSearchCV(
            estimator=model,
            param_distributions=param_grid,
            n_iter=1000,
            cv=5,
            random_state=42
        )

        # Fit the RandomizedSearchCV instance to the data
        random_search.fit(X_train, y_train)

        # Get the best parameters and best score
        best_params = random_search.best_params_
        best_score = random_search.best_score_

        print(best_params)
        print(best_score)

    else:
        # Create a Logistic Regression model
        model = LogisticRegression(solver='liblinear', penalty='l1', C=0.03359818286283781, l1_ratio = 0.3333333333333333, tol = 0.02183096839052459)

        # Train the model
        model.fit(X_train, y_train)

        # Predict the test set results
        y_pred = model.predict(X_test)
        print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))
        cm = confusion_matrix(y_test, y_pred)
        print("Confusion Matrix: \n", cm)

        # Plot the confusion matrix
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
        disp.plot()
        plt.show()

        # Calculate precision
        precision = precision_score(y_test, y_pred)

        # Calculate recall
        recall = recall_score(y_test, y_pred)

        # Calculate F1 score
        f1 = f1_score(y_test, y_pred)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)

        print("Precision: ", precision)
        print("Recall: ", recall)
        print("F1 Score: ", f1)
        print("Accuracy: ", accuracy)




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
        model = svm.SVC(kernel='sigmoid', C=3.745401188473625, gamma=0.07969454818643928)

        # Train the model
        model.fit(X_train, y_train)

        # Predict the test set results
        y_pred = model.predict(X_test)
        
        print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))
        cm = confusion_matrix(y_test, y_pred)
        print("Confusion Matrix: \n", cm)

        # Plot the confusion matrix
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
        disp.plot()
        plt.show()

        # Calculate precision
        precision = precision_score(y_test, y_pred)

        # Calculate recall
        recall = recall_score(y_test, y_pred)

        # Calculate F1 score
        f1 = f1_score(y_test, y_pred)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)

        print("Precision: ", precision)
        print("Recall: ", recall)
        print("F1 Score: ", f1)
        print("Accuracy: ", accuracy)


df = pd.read_csv('compas-raw_data-final.csv')
#logRegression(df, True)
supportVectorMachine(df, False)
