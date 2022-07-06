# For data manipulation
import numpy as np
import pandas as pd

# Import RandomForestClassifier and accuracy_score functions from sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings("ignore")

# The data is stored in the directory 'data'
path = '../data/'

# Read stock data from csv file
data = pd.read_csv(path + 'BAC_2010_2021.csv', index_col=0)
data.index = pd.to_datetime(data.index)
data.head()

# Create input features
data['Open-Close'] = (data['Open'] - data['Close'])
data['High-Low'] = (data['High'] - data['Low'])

# Drop NaN values
data.dropna(inplace=True)

# Store the features in a variable X
X = data[['Open-Close', 'High-Low']]
X.head(2)

y = np.where(data['Adj Close'].shift(-1) > data['Adj Close'], 1, -1)
y

# Training dataset length
split = int(len(data) * 0.75)

# Splitting the X and y into train and test datasets
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Create and fit the model on train dataset
clf = RandomForestClassifier(random_state=5)
model = clf.fit(X_train, y_train)

print('Prediction Accuracy (%): ', accuracy_score(y_test, model.predict(X_test), normalize=True)*100.0)