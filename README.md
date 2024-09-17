# EasyGraph 📊

**EasyGraph** is your go-to Python package for creating beautiful, intuitive, and now interactive graphs with just a few lines of code. Dive into data visualization with various chart types including line charts, bar charts, scatter plots, and more. With the new interactive functionality, users can now hover over data points to get detailed information, pan, and zoom to explore their graphs in a much more engaging manner.

## Features 🚀

- **Interactive Charts and Graphs**: All your favorite charts and graphs are now interactive, offering dynamic insights with functionalities like hover, pan, and zoom. 
- **Variety of Chart Types**: Supports a wide range of chart types for versatile data visualization.
- **Zero to Hero**: Start creating insightful graphs with no prior experience.
- **Plug and Play**: Easy to install and get started with.
- **Flexible**: Customize your charts with a wide range of parameters.
- **Theming Support**: Adapt the visuals of your charts with seaborn and matplotlib themes.
- **Time Series Analysis**: EasyGraph offers a variety of charts to assist in uncovering patterns, anomalies, and trends in your time series data.
- **Geological Plotting**: EasyGraph offers a variety of charts to help analyze geographical data, uncover insights, and make data-driven decisions.

## Installation 💻

Get it fresh from PyPI:

```bash
pip install EasyGraph-py
```

# Usage 🛠

Here’s a sneak peek at how easy it is to use EasyGraph:

```bash
from easy_graph import bar_chart, line_chart, set_theme
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April'],
    'Sales': [100, 200, 150, 250]
}
df = pd.DataFrame(data)

# Set a theme for your charts (optional)
set_theme('darkgrid')

# Enable interactive mode (new feature!)
interactive=True # False by default

bar_chart(df, x_col='Month', y_col='Sales', title='Monthly Sales', xlabel='Month', ylabel='Sales', interactive=True)

# Boom! A bar chart!
bar_chart(df, 'Month', 'Sales', title='Monthly Sales', xlabel='Month', ylabel='Sales')

# Kaboom! A line chart!
line_chart(df, 'Month', 'Sales', title='Monthly Sales', xlabel='Month', ylabel='Sales')

```

# Documentation 📖

### Interactive Functionality 🔍

The latest update brings interactive functionality to all the chart and graph types in EasyGraph. Now, while visualizing data using any of the chart types, users can hover over individual data points to view detailed information. This not only makes the data analysis process more insightful but also offers a dynamic user experience. Make sure to explore functionalities like panning and zooming to dive deeper into your visualizations!



## set_theme(theme=None)

Sets the theme for your plots globally.
Parameters

    theme (str, optional): The name of the theme. Supports all seaborn and matplotlib themes. Defaults to seaborn's "whitegrid".

## bar_chart(data, x_col, y_col, title='Bar Chart', xlabel='X-axis', ylabel='Y-axis')

Generates a bar chart from a pandas DataFrame.

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.

## line_chart(data, x_col, y_col, title='Line Chart', xlabel='X-axis', ylabel='Y-axis')

Generates a line chart from a pandas DataFrame.

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.

## scatter_plot(data, x_col, y_col, title='Scatter Plot', xlabel='X-axis', ylabel='Y-axis', theme=None)

Creates a scatter plot to visualize the relationship between two variables.
Parameters

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.

## histogram(data, col, bins=10, title='Histogram', xlabel='X-axis', ylabel='Frequency', theme=None)

Generates a histogram to visualize the distribution of a single variable.
Parameters

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.

## boxplot(data, col, title='Boxplot', ylabel='Y-axis', theme=None)

Creates a box plot to depict groups of numerical data through their quartiles.
Parameters

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.

## pie_chart(data, col, labels_col, title='Pie Chart', theme=None)

Generates a pie chart to illustrate numerical proportions in a dataset.
Parameters

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.

## stacked_bar_chart(data, x_col, y_cols, title='Stacked Bar Chart', xlabel='X-axis', ylabel='Y-axis', theme=None)

Creates a stacked bar chart to visualize the total amount that is subdivided into sub-groups.
Parameters

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.

## area_chart(data, x_col, y_col, title='Area Chart', xlabel='X-axis', ylabel='Y-axis', theme=None)

Generates an area chart to represent quantities through area filled under lines.
Parameters

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.

## hexbin_plot(data, x_col, y_col, gridsize=50, title='Hexbin Plot', xlabel='X-axis', ylabel='Y-axis', theme=None)

Creates a hexbin plot to represent the relationship between two numerical variables when you have a lot of data points.
Parameters

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.

## violin_plot(data, col, title='Violin Plot', ylabel='Y-axis', theme=None)

Generates a violin plot which combines a boxplot with a kernel density plot to visualize the distribution of numerical data.
Parameters

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.

## correlation_matrix(data, title='Correlation Matrix', theme=None)

Creates a heatmap of the correlation matrix to visualize the relationship between every pair of variables in your dataset.
Parameters

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.

## pair_plot(data, title='Pair Plot', theme=None)

Generates a pair plot to visualize the relationships between all pairs of variables in your dataset.
Parameters

Parameters:

    data: The pandas DataFrame containing your data.
    x_col: The column to use for the x-axis.
    y_col: The column to use for the y-axis.
    title: The title of your graph.
    xlabel: The label for the x-axis.
    ylabel: The label for the y-axis.


## Time Series Analysis 📈

Time series analysis is crucial for analyzing temporal data, and EasyGraph offers a variety of charts to assist in uncovering patterns, anomalies, and trends in your time series data.

### autocorrelation_plot(series, title='Autocorrelation Plot', theme=None)

Visualizes the autocorrelation of a time series, helping to identify seasonality and trend in your data.

Parameters:

    series: The pandas Series containing your time series data.
    title: The title of your graph.
    theme: The theme for the plot. Supports all seaborn and matplotlib themes.

### lag_plot(series, lag=1, title='Lag Plot', theme=None)

Generates a lag plot to visualize the relationship between observations and their lags, aiding in identifying structure and randomness in time series data.

Parameters:

    series: The pandas Series containing your time series data.
    lag: The lag between observations. Defaults to 1.
    title: The title of your graph.
    theme: The theme for the plot. Supports all seaborn and matplotlib themes.

### candlestick_chart(data, open_col, high_col, low_col, close_col, datetime_col, title='Candlestick Chart', theme=None)

Generates a candlestick chart to visualize the open, high, low, and close prices of a security over time, which is essential for financial time series analysis.

Parameters:

    data: The pandas DataFrame containing your time series data.
    open_col: The column containing the opening prices.
    high_col: The column containing the highest prices in the time period.
    low_col: The column containing the lowest prices in the time period.
    close_col: The column containing the closing prices.
    datetime_col: The column containing the datetime information.
    title: The title of your graph.
    theme: The theme for the plot. Supports all seaborn and matplotlib themes.

## Geographical Plotting 🌍

Geographical plotting is essential for visualizing spatial distributions, relationships, and trends. EasyGraph offers a variety of charts to help analyze geographical data, uncover insights, and make data-driven decisions.

### `choropleth_map(data, geojson, locations, color, title='Choropleth Map', theme=None, interactive=True)`

Generates a choropleth map to visualize spatial data, revealing patterns, distributions, and variations across geographical areas.

**Parameters:**
- `data`: The pandas DataFrame containing your geographical data.
- `geojson`: The GeoJSON object that represents the geographical features.
- `locations`: The column in your DataFrame that matches the `featureidkey` in the GeoJSON object.
- `color`: The column in your DataFrame representing the variable you want to visualize.
- `title`: The title of your graph. Defaults to 'Choropleth Map'.
- `theme`: The theme for the plot. Supports all seaborn and matplotlib themes. (Optional)
- `interactive`: Whether to display the plot in interactive mode. Recommended for choropleth maps. Defaults to True.

### `scattergeo_map(data, lat_col, lon_col, text_col, title='Scattergeo Map', theme=None, interactive=True)`

Creates a scattergeo map to display individual data points on a geographical map, enabling the analysis of spatial relationships and trends.

**Parameters:**
- `data`: The pandas DataFrame containing your geographical data.
- `lat_col`: The column in your DataFrame representing the latitude coordinates.
- `lon_col`: The column in your DataFrame representing the longitude coordinates.
- `text_col`: The column in your DataFrame representing the text information to be displayed on hover.
- `title`: The title of your graph. Defaults to 'Scattergeo Map'.
- `theme`: The theme for the plot. Supports all seaborn and matplotlib themes. (Optional)
- `interactive`: Whether to display the plot in interactive mode. Recommended for scattergeo maps. Defaults to True.

### `linegeo_map(data, lat_col, lon_col, line_group, title='Linegeo Map', theme=None, interactive=True)`

Constructs a linegeo map to visualize connections or paths between geographical locations, aiding in the study of spatial patterns and distributions.

**Parameters:**
- `data`: The pandas DataFrame containing your geographical data.
- `lat_col`: The column in your DataFrame representing the latitude coordinates.
- `lon_col`: The column in your DataFrame representing the longitude coordinates.
- `line_group`: The column in your DataFrame used to group rows into line segments.
- `title`: The title of your graph. Defaults to 'Linegeo Map'.
- `theme`: The theme for the plot. Supports all seaborn and matplotlib themes. (Optional)
- `interactive`: Whether to display the plot in interactive mode. Recommended for linegeo maps. Defaults to True.

# More Charts, Maps, Plots Coming very soon.
- (In August 2024)

# Contribution 🤝

Feel free to fork, open a pull request, or submit issues. Let's make EasyGraph the easiest graphing package in the Python ecosystem together!
License 📄

MIT
##Kudos 💖

Big shoutout to all cool devs and data scientists out there! Happy graphing!
