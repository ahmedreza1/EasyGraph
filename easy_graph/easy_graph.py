import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def set_theme(theme=None):
    """Set the theme for the plots."""
    if theme:
        if theme in plt.style.available:
            plt.style.use(theme)
        else:
            sns.set_style(theme)
    else:
        sns.set_style("whitegrid")  # Set to seaborn default

def bar_chart(data, x_col, y_col, title='Bar Chart', xlabel='X-axis', ylabel='Y-axis', theme=None):
    """Generate a bar chart from a pandas DataFrame."""
    set_theme(theme)
    plt.bar(data[x_col], data[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    set_theme()  # Reset to default theme after plotting

def line_chart(data, x_col, y_col, title='Line Chart', xlabel='X-axis', ylabel='Y-axis', theme=None):
    """Generate a line chart from a pandas DataFrame."""
    set_theme(theme)
    plt.plot(data[x_col], data[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    set_theme()  # Reset to default theme after plotting

def scatter_plot(data, x_col, y_col, title='Scatter Plot', xlabel='X-axis', ylabel='Y-axis', theme=None):
    """Generate a scatter plot from a pandas DataFrame."""
    set_theme(theme)
    plt.scatter(data[x_col], data[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    set_theme()  # Reset to default theme after plotting

def histogram(data, col, bins=10, title='Histogram', xlabel='X-axis', ylabel='Frequency', theme=None):
    """Generate a histogram from a pandas DataFrame."""
    set_theme(theme)
    plt.hist(data[col], bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    set_theme()  # Reset to default theme after plotting

def boxplot(data, col, title='Boxplot', ylabel='Y-axis', theme=None):
    """Generate a box plot from a pandas DataFrame."""
    set_theme(theme)
    plt.boxplot(data[col])
    plt.title(title)
    plt.ylabel(ylabel)
    plt.show()
    set_theme()  # Reset to default theme after plotting

def pie_chart(data, col, labels_col, title='Pie Chart', theme=None):
    """Generate a pie chart from a pandas DataFrame."""
    set_theme(theme)
    plt.pie(data[col], labels=data[labels_col], autopct='%1.1f%%')
    plt.title(title)
    plt.show()
    set_theme()  # Reset to default theme after plotting

def stacked_bar_chart(data, x_col, y_cols, title='Stacked Bar Chart', xlabel='X-axis', ylabel='Y-axis', theme=None):
    """Generate a stacked bar chart from a pandas DataFrame."""
    set_theme(theme)
    ax = data.plot(x=x_col, kind='bar', stacked=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    set_theme()  # Reset to default theme after plotting

def area_chart(data, x_col, y_col, title='Area Chart', xlabel='X-axis', ylabel='Y-axis', theme=None):
    """Generate an area chart from a pandas DataFrame."""
    set_theme(theme)
    plt.fill_between(data[x_col], data[y_col])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    set_theme()  # Reset to default theme after plotting

def hexbin_plot(data, x_col, y_col, gridsize=50, title='Hexbin Plot', xlabel='X-axis', ylabel='Y-axis', theme=None):
    """Generate a hexbin plot from a pandas DataFrame."""
    set_theme(theme)
    plt.hexbin(data[x_col], data[y_col], gridsize=gridsize, cmap='Greens')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar()
    plt.show()
    set_theme()  # Reset to default theme after plotting

def violin_plot(data, col, title='Violin Plot', ylabel='Y-axis', theme=None):
    """Generate a violin plot from a pandas DataFrame using Seaborn."""
    set_theme(theme)
    sns.violinplot(y=data[col])
    plt.title(title)
    plt.ylabel(ylabel)
    plt.show()
    set_theme()  # Reset to default theme after plotting

def correlation_matrix(data, title='Correlation Matrix', theme=None):
    """Generate a correlation matrix from a pandas DataFrame using Seaborn."""
    set_theme(theme)
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title(title)
    plt.show()
    set_theme()  # Reset to default theme after plotting

def pair_plot(data, title='Pair Plot', theme=None):
    """Generate a pair plot from a pandas DataFrame using Seaborn."""
    set_theme(theme)
    sns.pairplot(data)
    plt.suptitle(title, y=1.02)
    plt.show()
    set_theme()  # Reset to default theme after plotting

# Additional functions for other chart types can be added here.
