import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('compas-scores-raw.csv')

for column in df.columns:
    # Check if the column contains strings
    if df[column].dtype == 'object':
        # Count the occurrences of unique strings in the column
        value_counts = df[column].value_counts()
        
        # Plot a bar chart of the frequency
        plt.bar(value_counts.index, value_counts.values)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.savefig(f'{column}_bar_chart.png')
        plt.close()

    else:
        # Count the occurrences of unique values in the column
        value_counts = df[column].value_counts()
        
        # Plot a histogram of the frequency
        plt.hist(df[column], bins=10)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.savefig(f'{column}_histogram.png')
        plt.close()

