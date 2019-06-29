'''
Simple Linear Regression example - Demonstrating Scikit-Learn Usecase
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Defining the range and parameter
rng = np.random.RandomState(42)
x = 8*rng.rand(50)
y = 2*x - 1 + rng.rand(50)

# Plotting the data
plt.figure('Scatter Plot')
plt.scatter(x, y, cmap='viridis')
plt.title('Scatter Plot')
plt.savefig('Scatter Plot.png')
plt.show()

# Define the linear_model
model = LinearRegression(fit_intercept=True)
print(f"Model is: {model}")

# Define the feature matrix
X = x[:, np.newaxis]
print(f"Shape of Feature matrix: {X.shape}")

# Fit the model
model.fit(X, y)

'''
In the fit() process we have the learned model parameters to 
go with underscores. Here we can get the slope term using coef_
and the intercept using intercept_
'''
print(f"The slope : {model.coef_} and the intercept: {model.intercept_}")

# Predict the labels for unknown data
xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)

# Plotting the result
plt.figure('Results')
plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.title('Fit results')
plt.savefig('Linear Regression.png')
plt.show()