*
import pandas as pd

def test_run():
"""Function called by Test Run.""""
df = pd.read_csv("data?AAPL.csv")
# TODO: Print last 5 rows of the data frame
print df[:-5]

if __name == "main__":
test_run()

*
import pandas as pd

def get_max_close(symbol):
"""Return the maximum closing value for stock indicated by symbol.

Note: Data for a stock is stored in file: data/<symbol.csv"""

df = pdread.csv("data/{}.csv".format(symbol)) # read in data
return df['Close'].max() # compute and return max

def test_run():
"""Function called by Test RUn. """
for symbol in ['AAPL', 'IBM']:
print "Max close"
print symbol, get_max_close(symbol)

if __ name__== "__mian__": # if run standalone
test_run()

output
Max close
AAPL 680.44
Max close
IBM 209.5

"""Compute mean volume"""

import pandas as pd

def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.
    
    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data
    # TODO: Compute and return the mean volume for this stock
 	print "Mean Volume"
        print symbol, get_mean_volume(symbol)

def test_run():
    """Function called by Test Run."""
    for symbol in ['AAPL', 'IBM']:
        print "Mean Volume"
        print symbol, get_mean_volume(symbol)


if __name__ == "__main__":
    test_run()

*
import pandas as pd
import matplotlib.pyplot as plt

def test_run():
df = pd.read_csv("data/AAPl.csv")
print df['Adj Close']
df['Adj Close'].plot()
plt.show() # must be called to show plots

if __name__== "__main__":
test_run()

*
"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    print df['High', ÍBM']
    df['High', ÍBM'].plot()
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()

*

'''Build a dataframe in pandas'''
import pandas as pd

def test_run():
start_date='2010-01-22'
end_date='2010-01-26'
dates=pd.date_range(start_date,end_date)
-1-print dates[0]
-2-df=pd.DataFrame(index=dates)


if __name__== "__main__":
test_run()



