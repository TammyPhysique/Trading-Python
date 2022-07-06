# Import numpy
import numpy as np

# Import matplotlib as an alias plt and set the style
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('seaborn-darkgrid')

# Import svm from sklearn
from sklearn import svm

# Create 40 separable points
np.random.seed(0)
X = np.r_[np.random.randn(20, 2)-[2, 2], np.random.randn(20, 2) + [2, 2]]
Y = [0] * 20 + [1] * 20
X[:3],Y[:3]

# Fit the model
clf = svm.SVC(kernel="linear")
clf.fit(X, Y)

# Get the separating hyperplane

# Coefficient of the model
w = clf.coef_[0]  

# Slope of the model
a = -w[0] / w[1]  

# Define the X coordinate
xx = np.linspace(-5, 5) 

# Calculate the Y coordinate
yy = a * xx - (clf.intercept_[0]) / w[1] 

xx,yy

# Construct the upper plane
b = clf.support_vectors_[0]    
yy_down = a * xx + (b[1] - a * b[0]) 
yy_down

plt.figure(figsize=(10,7))

# Separating hyperplane
plt.plot(xx, yy,'k-')        
# Lower boundary
plt.plot(xx, yy_down, 'k--') 
# Upper boundary
plt.plot(xx, yy_up,'k--')   
plt.scatter(clf.support_vectors_[:,0], clf.support_vectors_[:,1], s=80, facecolors="none") 
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
plt.title('Support Vector Classifier', fontsize=14)
plt.xlabel('X-coordinate', fontsize=12)
plt.ylabel('Y-coordinate', fontsize=12)
plt.show()

