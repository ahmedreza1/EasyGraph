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

# Here we are introducing Time Series Analysis, by adding a Candlestick Chart for stock price analysis, an Autocorrelation Plot, and a Lag Plot.

def candlestick_chart(data, open_col, high_col, low_col, close_col, date_col, title='Candlestick Chart', theme=None, interactive=True):
    set_theme(theme)
    try:
        if interactive:
            fig = go.Figure(data=[go.Candlestick(x=data[date_col],
                                                 open=data[open_col],
                                                 high=data[high_col],
                                                 low=data[low_col],
                                                 close=data[close_col])])
            fig.update_layout(title=title, xaxis_title='Date', yaxis_title='Price')
            fig.show()
        else:
            print("Interactive mode is recommended for Candlestick Chart!")
    except KeyError as e:
        print(f"Column not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme() # Reset to default theme after plotting

def autocorrelation_plot(series, title='Autocorrelation Plot', theme=None):
    set_theme(theme)
    try:
        pd_plot.autocorrelation_plot(series)
        plt.title(title)
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme() # Reset to default theme after plotting

def lag_plot(series, lag=1, title='Lag Plot', theme=None):
    set_theme(theme)
    try:
        pd_plot.lag_plot(series, lag=lag)
        plt.title(title)
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme() # Reset to default theme after plotting

# Here we are introducing Geographical Plotting, by adding three types of maps Choropleth, Scattergeo, and Linegeo

def choropleth_map(data, geojson, locations, color, title='Choropleth Map', theme=None, interactive=True):
    set_theme(theme)
    try:
        if interactive:
            fig = px.choropleth(data, geojson=geojson, locations=locations, color=color,
                                featureidkey="properties.name",
                                title=title)
            fig.update_geos(projection_type="mercator")
            fig.show()
        else:
            print("Interactive mode is recommended for Choropleth Map!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def scattergeo_map(data, lat_col, lon_col, text_col, title='Scattergeo Map', theme=None, interactive=True):
    set_theme(theme)
    try:
        if interactive:
            fig = px.scatter_geo(data, lat=lat_col, lon=lon_col, text=text_col,
                                 title=title)
            fig.update_geos(projection_type="mercator")
            fig.show()
        else:
            print("Interactive mode is recommended for Scattergeo Map!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

def linegeo_map(data, lat_col, lon_col, line_group, title='Linegeo Map', theme=None, interactive=True):
    set_theme(theme)
    try:
        if interactive:
            fig = px.line_geo(data, lat=lat_col, lon=lon_col, line_group=line_group,
                              title=title)
            fig.update_geos(projection_type="mercator")
            fig.show()
        else:
            print("Interactive mode is recommended for Linegeo Map!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        set_theme()  # Reset to default theme after plotting

# Additional functions for other chart types can be added here.
