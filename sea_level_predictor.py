import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = range(1880, 2051)
    y_values = slope*x_values + intercept
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(x_values, y_values, 'r', label='Line of best fit')


    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_values_2000 = range(2000, 2051)
    y_values_2000 = slope_2000*x_values_2000 + intercept_2000
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(x_values_2000, y_values_2000, 'g', label='Line of best fit from year 2000')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()