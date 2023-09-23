import pandas as pd
import numpy as np
from easy_graph import (
    bar_chart, line_chart, scatter_plot, histogram, boxplot, 
    pie_chart, stacked_bar_chart, area_chart, hexbin_plot, 
    violin_plot, correlation_matrix, pair_plot,
    candlestick_chart, autocorrelation_plot, lag_plot
)

# Creating a sample DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April'],
    'Sales': [100, 200, 150, 250],
    'Expense': [90, 170, 130, 210],
    'Profit': [10, 30, 20, 40],
}
df = pd.DataFrame(data)

# Adding a categorical variable for scatter plot
df['Is Profitable'] = df['Profit'] > 0

# Testing the bar_chart function
bar_chart(df, 'Month', 'Sales', title='Monthly Sales', xlabel='Month', ylabel='Sales', interactive=True)

# Testing the line_chart function
line_chart(df, 'Month', 'Sales', title='Monthly Sales', xlabel='Month', ylabel='Sales')

# Testing the scatter_plot function
scatter_plot(df, 'Sales', 'Expense', title='Sales vs Expense', xlabel='Sales', ylabel='Expense')

# Testing the histogram function
histogram(df, 'Sales', title='Sales Distribution', xlabel='Sales', ylabel='Frequency')

# Testing the boxplot function
boxplot(df, 'Sales', title='Sales Boxplot', ylabel='Sales')

# Testing the pie_chart function
pie_chart(df, 'Sales', 'Month', title='Sales Distribution', interactive=True)

# Testing the stacked_bar_chart function
stacked_bar_chart(df, 'Month', ['Sales', 'Expense'], title='Monthly Sales and Expense', xlabel='Month', ylabel='Value')

# Testing the area_chart function
area_chart(df, 'Month', 'Sales', title='Sales Area Chart', xlabel='Month', ylabel='Sales')

# Testing the hexbin_plot function
hexbin_plot(df, 'Sales', 'Expense', title='Hexbin Plot of Sales and Expense', xlabel='Sales', ylabel='Expense')

# Testing the violin_plot function
violin_plot(df, 'Sales', title='Sales Violin Plot', ylabel='Sales')

# Testing the correlation_matrix function
correlation_matrix(df, title='Correlation Matrix')

# Testing the pair_plot function
pair_plot(df, title='Pair Plot')

# Creating synthetic data for candlestick_chart
stock_data = {
    'Date': pd.date_range(start='1/1/2023', periods=4, freq='M'),
    'Open': [100, 150, 200, 250],
    'High': [110, 160, 210, 260],
    'Low': [90, 140, 190, 240],
    'Close': [105, 155, 205, 255],
}
stock_df = pd.DataFrame(stock_data)

# Testing the candlestick_chart function
candlestick_chart(stock_df, 'Open', 'High', 'Low', 'Close', 'Date', title='Monthly Stock Prices', interactive=True)

# Creating synthetic time series data for autocorrelation_plot and lag_plot
time_series_data = {
    'Date': pd.date_range(start='1/1/2023', periods=30, freq='D'),
    'Value': np.random.randn(30).cumsum() # Cumulative sum of random numbers to create a time series
}
time_series_df = pd.DataFrame(time_series_data)
time_series_series = time_series_df.set_index('Date')['Value']

# Testing the autocorrelation_plot function
autocorrelation_plot(time_series_series, title='Autocorrelation Plot')

# Testing the lag_plot function
lag_plot(time_series_series, lag=1, title='Lag Plot')