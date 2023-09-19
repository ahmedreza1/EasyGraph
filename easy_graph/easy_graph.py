import matplotlib.pyplot as plt
import pandas as pd

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

# Additional functions for other chart types (e.g., scatter_plot, histogram) can be added here.
