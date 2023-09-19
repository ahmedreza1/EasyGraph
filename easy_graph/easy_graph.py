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

def pie_chart(data, col, labels_col, title='Pie Chart'):
    """Generate a pie chart from a pandas DataFrame."""
    plt.pie(data[col], labels=data[labels_col], autopct='%1.1f%%')
    plt.title(title)
    plt.show()

def stacked_bar_chart(data, x_col, y_cols, title='Stacked Bar Chart', xlabel='X-axis', ylabel='Y-axis'):
    """Generate a stacked bar chart from a pandas DataFrame."""
    ax = data.plot(x=x_col, kind='bar', stacked=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def area_chart(data, x_col, y_col, title='Area Chart', xlabel='X-axis', ylabel='Y-axis'):
    """Generate an area chart from a pandas DataFrame."""
    plt.fill_between(data[x_col], data[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def hexbin_plot(data, x_col, y_col, gridsize=50, title='Hexbin Plot', xlabel='X-axis', ylabel='Y-axis'):
    """Generate a hexbin plot from a pandas DataFrame."""
    plt.hexbin(data[x_col], data[y_col], gridsize=gridsize, cmap='Greens')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar()
    plt.show()

def violin_plot(data, col, title='Violin Plot', ylabel='Y-axis'):
    """Generate a violin plot from a pandas DataFrame using Seaborn."""
    sns.violinplot(y=data[col])
    plt.title(title)
    plt.ylabel(ylabel)
    plt.show()

def correlation_matrix(data, title='Correlation Matrix'):
    """Generate a correlation matrix from a pandas DataFrame using Seaborn."""
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title(title)
    plt.show()

def pair_plot(data, title='Pair Plot'):
    """Generate a pair plot from a pandas DataFrame using Seaborn."""
    sns.pairplot(data)
    plt.suptitle(title, y=1.02)
    plt.show()

# Additional functions for other chart types can be added here.
