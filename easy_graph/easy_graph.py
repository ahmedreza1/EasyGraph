import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def bar_chart(data, x_col, y_col, title='Bar Chart', xlabel='X-axis', ylabel='Y-axis'):
    """Generate a bar chart from a pandas DataFrame."""
    plt.bar(data[x_col], data[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def line_chart(data, x_col, y_col, title='Line Chart', xlabel='X-axis', ylabel='Y-axis'):
    """Generate a line chart from a pandas DataFrame."""
    plt.plot(data[x_col], data[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def scatter_plot(data, x_col, y_col, title='Scatter Plot', xlabel='X-axis', ylabel='Y-axis'):
    """Generate a scatter plot from a pandas DataFrame."""
    plt.scatter(data[x_col], data[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def histogram(data, col, bins=10, title='Histogram', xlabel='X-axis', ylabel='Frequency'):
    """Generate a histogram from a pandas DataFrame."""
    plt.hist(data[col], bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def boxplot(data, col, title='Boxplot', ylabel='Y-axis'):
    """Generate a box plot from a pandas DataFrame."""
    plt.boxplot(data[col])
    plt.title(title)
    plt.ylabel(ylabel)
    plt.show()



# Additional functions for other chart types can be added here.
