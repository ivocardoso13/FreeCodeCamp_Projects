import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x= df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.5)

    # Create first line of best fit
    res = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope*x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'r')

    # Create second line of best fit
    df_new = df.loc[df['Year'] >= 2000]
    x_new = df_new['Year']
    y_new = df_new['CSIRO Adjusted Sea Level']

    res_new = linregress(x_new, y_new)
    x_new_pred = pd.Series([i for i in range(2000, 2051)])
    y_new_pred = res_new.slope*x_new_pred + res_new.intercept
    plt.plot(x_new_pred, y_new_pred, 'green')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()