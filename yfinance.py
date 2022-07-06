!pip install yfinance

import yfinance as yf
data = yf.download('AAPL', start="2017-01-01", end="2017-04-30")
data.head()

# Yahoo recently has become an unstable data source.

# If it gives an error, you may run the cell again, or try again sometime later

import pandas as pd
from pandas_datareader import data
data = data.get_data_yahoo('AAPL', '2017-01-01', '2018-01-01')
data.head()

# Import necessary packages
import yfinance as yf
from datetime import datetime

# Set start and end date
start = datetime(2018, 1, 1)
end = datetime(2019, 1, 1)

# Type your code below
data = yf.download('MSFT',start,end)
print(data.tail())

# Import libraries
import numpy as np
import pandas as pd

# The data is stored in the directory 'data_modules'
# Read the csv file using read_csv method of pandas
infy = pd.read_csv('../data_modules/infy_data.csv')

# Display the data frame
infy

# Display the first 5 rows
infy.head()

import pandas as pd
#Type your code here
infy = pd.read_csv ('infy_data.csv')
print (infy.head ()) # You will see the top 5 rows
print ('\n')
print (infy.tail ()) # You will see the bottom 5 rows

