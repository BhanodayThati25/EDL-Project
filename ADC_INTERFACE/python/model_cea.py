import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Define the nonlinear function to fit
def func(x, a, b, c):
    #return a * np.exp(-b * x) + c
    return a*(x**2) + b*x + c

# Data to fit
xdata = np.log10(np.array([1, 1000, 5000, 10000, 20000, 100000, 400000, 800000]))
ydata = np.array([7.25, 10.8, 14.01, 22.56, 35.64, 41.5, 48.82, 59.1])

# Perform the curve fitting
popt, pcov = curve_fit(func, xdata, ydata)

# Print the optimized parameters
print(popt)

# Plot the data and the best-fitting curve
plt.plot(xdata, ydata, 'ko', label='Data')
plt.plot(xdata, func(xdata, *popt), 'r-', label='Best fit')
plt.legend()
plt.show()

#accuracy of the fitting
ypred = func(xdata, popt[0], popt[1], popt[2])
print(ypred)

# y_test and y_pred are the test and predicted values respectively
r2 = r2_score(ydata, ypred)
print('R-squared:', r2)