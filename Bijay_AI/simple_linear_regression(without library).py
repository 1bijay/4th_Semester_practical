import numpy as np

# New data points
x = np.array([2, 4, 6, 8, 10])
y = np.array([4, 8, 12, 16, 20])

# Function to calculate linear regression prediction
def regression(x_val, b0, b1):
    return b0 + b1 * x_val

# Number of data points
n = len(x)

# Calculating the sums
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_xsq = np.sum(x ** 2)

# Calculating coefficients b1 and b0
b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_xsq - sum_x ** 2)
b0 = np.mean(y) - b1 * np.mean(x)
print(f'Calculated coefficients: b0 = {b0}, b1 = {b1}')
print(f'Equation of the line: Y = {b0} + {b1}X')
