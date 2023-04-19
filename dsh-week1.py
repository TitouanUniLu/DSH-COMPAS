import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('compas-scores-raw.csv')

for column in df.columns:
    # Count the occurrences of unique values in the column
    value_counts = df[column].value_counts()

    # Plot a histogram of the frequency
    plt.bar(value_counts.index, value_counts.values)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column}')
    plt.show()

  





    
