Import SVM Module

# Import the libraries
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Type your code below
from sklearn.svm import SVC

Read Data From CSV File

# Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# Read the data from CSV file
# Type your code below 
Df = pd.read_csv('../data/SPY.csv', index_col=0)
print(Df.head())

Create Classifier Model

# Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import warnings
warnings.filterwarnings('ignore')

# The data is stored in the directory 'data'
path = '../data/'

# Read the csv file using read_csv method of pandas
Df = pd.read_csv(path + 'SPY.csv', index_col=0)

# Create predictor variables
Df['Open-Close'] = Df.Open - Df.Close
Df['High-Low'] = Df.High - Df.Low
X= Df[['Open-Close','High-Low']]

# Target variables
y = np.where(Df['Close'].shift(-1) > Df['Close'], 1, -1)

# Split the data into train and test dataset
split_percentage = 0.8
split = int(split_percentage*len(Df))

# Train data set
X_train = X[:split]
y_train = y[:split]

# Test data set
X_test = X[split:]
y_test = y[split:]

# Instantiate SVC()
svc = SVC()
# Create classifier model
# Type your code below
clf = svc.fit(X_train, y_train)

Predict Trading Signals

# Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import warnings
warnings.filterwarnings('ignore')

# The data is stored in the directory 'data'
path = '../data/'

# Read the csv file using read_csv method of pandas
Df = pd.read_csv(path + 'SPY.csv', index_col=0)

# Create predictor variables
Df['Open-Close'] = Df.Open - Df.Close
Df['High-Low'] = Df.High - Df.Low
X= Df[['Open-Close','High-Low']]

# Target variables
y = np.where(Df['Close'].shift(-1) > Df['Close'], 1, -1)

# Split the data into train and test dataset
split_percentage = 0.8
split = int(split_percentage*len(Df))

# Train data set
X_train = X[:split]
y_train = y[:split]

# Test data set
X_test = X[split:]
y_test = y[split:]

# Create support classifier model
clf = SVC().fit(X_train, y_train)

# Predict signals
# Type your code below
Df['Predicted_Signal'] = clf.predict(X)
print(Df.tail())
