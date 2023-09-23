import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pandas.plotting as pd_plot

def set_theme(theme=None):
    """Set the theme for the plots."""
    try:
        if theme:
            if theme in plt.style.available:
                plt.style.use(theme)
            else:
                sns.set_style(theme)
        else:
            sns.set_style("whitegrid")  # Set to seaborn default
    except Exception as e:
        print(f"An error occurred: {e}")

def bar_chart(data, x_col, y_col, title='Bar Chart', xlabel='X-axis', ylabel='Y-axis', theme=None, interactive=False):
    set_theme(theme)
    try:
        if interactive:
            fig = px.bar(data, x=x_col, y=y_col, title=title, labels={x_col: xlabel, y_col: ylabel})
            fig.show()
        else:
            plt.bar(data[x_col], data[y_col])
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def line_chart(data, x_col, y_col, title='Line Chart', xlabel='X-axis', ylabel='Y-axis', theme=None, interactive=False):
    set_theme(theme)
    try:
        if interactive:
            fig = px.line(data, x=x_col, y=y_col, title=title, labels={x_col: xlabel, y_col: ylabel})
            fig.show()
        else:
            plt.plot(data[x_col], data[y_col])
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def scatter_plot(data, x_col, y_col, title='Scatter Plot', xlabel='X-axis', ylabel='Y-axis', theme=None, interactive=False):
    """Generate a scatter plot from a pandas DataFrame."""
    set_theme(theme)
    try:
        if interactive:
            fig = px.scatter(data, x=x_col, y=y_col, title=title, labels={x_col: xlabel, y_col: ylabel})
            fig.show()
        else:
            plt.scatter(data[x_col], data[y_col])
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme() # Reset to default theme after plotting

def histogram(data, col, bins=10, title='Histogram', xlabel='X-axis', ylabel='Frequency', theme=None, interactive=False):
    """Generate a histogram from a pandas DataFrame."""
    set_theme(theme)
    try:
        if interactive:
            fig = px.histogram(data, x=col, nbins=bins, title=title, labels={col: xlabel})
            fig.update_yaxes(title_text=ylabel)
            fig.show()
        else:
            plt.hist(data[col], bins=bins)
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def boxplot(data, col, title='Boxplot', ylabel='Y-axis', theme=None, interactive=False):
    """Generate a box plot from a pandas DataFrame."""
    set_theme(theme)
    try:
        if interactive:
            fig = px.box(data, y=col, title=title)
            fig.update_yaxes(title_text=ylabel)
            fig.show()
        else:
            plt.boxplot(data[col])
            plt.title(title)
            plt.ylabel(ylabel)
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def pie_chart(data, col, labels_col, title='Pie Chart', theme=None, interactive=False):
    """Generate a pie chart from a pandas DataFrame."""
    set_theme(theme)
    try:
        if interactive:
            fig = px.pie(data, values=col, names=labels_col, title=title)
            fig.show()
        else:
            plt.pie(data[col], labels=data[labels_col], autopct='%1.1f%%')
            plt.title(title)
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def stacked_bar_chart(data, x_col, y_cols, title='Stacked Bar Chart', xlabel='X-axis', ylabel='Y-axis', theme=None, interactive=False):
    """Generate a stacked bar chart from a pandas DataFrame."""
    set_theme(theme)
    try:
        if interactive:
            fig = px.bar(data, x=x_col, y=y_cols, title=title, labels={'x': xlabel, 'y': ylabel}, height=400)
            fig.show()
        else:
            ax = data.plot(x=x_col, kind='bar', stacked=True)
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def area_chart(data, x_col, y_col, title='Area Chart', xlabel='X-axis', ylabel='Y-axis', theme=None, interactive=False):
    """Generate an area chart from a pandas DataFrame."""
    set_theme(theme)
    try:
        if interactive:
            fig = px.area(data, x=x_col, y=y_col, title=title, labels={x_col: xlabel, y_col: ylabel})
            fig.show()
        else:
            plt.fill_between(data[x_col], data[y_col])
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def hexbin_plot(data, x_col, y_col, gridsize=50, title='Hexbin Plot', xlabel='X-axis', ylabel='Y-axis', theme=None, interactive=False):
    """Generate a hexbin plot from a pandas DataFrame."""
    set_theme(theme)
    try:
        if interactive:
            fig = px.density_heatmap(data, x=x_col, y=y_col, nbinsx=gridsize, nbinsy=gridsize, title=title, labels={x_col: xlabel, y_col: ylabel})
            fig.show()
        else:
            plt.hexbin(data[x_col], data[y_col], gridsize=gridsize, cmap='Greens')
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.colorbar()
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def violin_plot(data, col, title='Violin Plot', ylabel='Y-axis', theme=None, interactive=False):
    """Generate a violin plot from a pandas DataFrame using Seaborn."""
    set_theme(theme)
    try:
        if interactive:
            fig = px.violin(data, y=col, title=title, box=True)
            fig.update_yaxes(title_text=ylabel)
            fig.show()
        else:
            sns.violinplot(y=data[col])
            plt.title(title)
            plt.ylabel(ylabel)
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def correlation_matrix(data, title='Correlation Matrix', theme=None, interactive=False):
    """Generate a correlation matrix from a pandas DataFrame using Seaborn."""
    set_theme(theme)
    try:
        if interactive:
            corr = data.corr()
            fig = px.imshow(corr, title=title)
            fig.show()
        else:
            corr = data.corr()
            sns.heatmap(corr, annot=True, cmap='coolwarm')
            plt.title(title)
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def pair_plot(data, title='Pair Plot', theme=None, interactive=False):
    """Generate a pair plot from a pandas DataFrame using Seaborn."""
    set_theme(theme)
    try:
        if interactive:
            fig = px.scatter_matrix(data, title=title)
            fig.show()
        else:
            sns.pairplot(data)
            plt.suptitle(title, y=1.02)
            plt.show()
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

# Additional functions for other chart types can be added here.
