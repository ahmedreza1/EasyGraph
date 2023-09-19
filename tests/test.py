import pandas as pd
from easy_graph import bar_chart, line_chart

# Creating a sample DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April'],
    'Sales': [100, 200, 150, 250]
}
df = pd.DataFrame(data)

# Testing the bar_chart function
bar_chart(df, 'Month', 'Sales', title='Monthly Sales', xlabel='Month', ylabel='Sales')

# Testing the line_chart function
line_chart(df, 'Month', 'Sales', title='Monthly Sales', xlabel='Month', ylabel='Sales')
