# EasyGraph 📊

**EasyGraph** is your go-to Python package for quick and dirty data visualization. Throw some data at it and watch it spit out beautiful, intuitive graphs faster than you can say "matplotlib"! It's as easy as pie (charts)!

## Features 🚀

- **Zero to Hero**: Go from zero to data visualization hero in seconds!
- **Plug and Play**: No steep learning curve; just install and start graphing!
- **Flexible**: Customize your charts with a wide range of parameters.

## Installation 💻

Get it fresh from PyPI:

```bash
pip install EasyGraph-py
```

# Usage 🛠

Here’s a sneak peek at how easy it is to use EasyGraph:

```bash
from easy_graph import bar_chart, line_chart
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April'],
    'Sales': [100, 200, 150, 250]
}
df = pd.DataFrame(data)

# Boom! A bar chart!
bar_chart(df, 'Month', 'Sales', title='Monthly Sales', xlabel='Month', ylabel='Sales')

# Kaboom! A line chart!
line_chart(df, 'Month', 'Sales', title='Monthly Sales', xlabel='Month', ylabel='Sales')

```

# Documentation 📖

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

# Contribution 🤝

Feel free to fork, open a pull request, or submit issues. Let's make EasyGraph the easiest graphing package in the Python ecosystem together!
License 📄

MIT
##Kudos 💖

Big shoutout to all cool devs and data scientists out there! Happy graphing!