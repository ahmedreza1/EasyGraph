# EasyGraph 📊

**EasyGraph** is your go-to Python package for creating beautiful and intuitive graphs with just a few lines of code. Dive into data visualization with various chart types including line charts, bar charts, scatter plots, and more!

## Features 🚀

- **Variety of Chart Types**: Supports a wide range of chart types for versatile data visualization.
- **Zero to Hero**: Start creating insightful graphs with no prior experience.
- **Plug and Play**: Easy to install and get started with.
- **Flexible**: Customize your charts with a wide range of parameters.
- **Theming Support**: Adapt the visuals of your charts with seaborn and matplotlib themes.

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

# Boom! A bar chart!
bar_chart(df, 'Month', 'Sales', title='Monthly Sales', xlabel='Month', ylabel='Sales')

# Kaboom! A line chart!
line_chart(df, 'Month', 'Sales', title='Monthly Sales', xlabel='Month', ylabel='Sales')

```

# Documentation 📖

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

# Contribution 🤝

Feel free to fork, open a pull request, or submit issues. Let's make EasyGraph the easiest graphing package in the Python ecosystem together!
License 📄

MIT
##Kudos 💖

Big shoutout to all cool devs and data scientists out there! Happy graphing!