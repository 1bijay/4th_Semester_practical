from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# New input features: [age, salary]
x = np.array([
    [25, 50000],
    [30, 70000],
    [28, 48000],
    [35, 85000],
    [40, 120000],
    [45, 150000],
    [23, 45000],
    [32, 90000],
    [38, 110000],
    [50, 200000]
])

# New target labels (0 or 1)
y = np.array([0, 1, 0, 1, 1, 1, 0, 1, 1, 1])

# Split the dataset into training and testing sets (80% train, 20% test)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(xtrain, ytrain)

# New data point for prediction
xnew = np.array([[37, 130000]])  # Predict for age=37 and salary=130,000
new_prediction = model.predict(xnew)

# Print the prediction for the new data point with cleaner formatting
print(f"Prediction for input [age: {xnew[0][0]}, salary: {xnew[0][1]}]: {new_prediction[0]}")

# Predict on the test set
y_pred = model.predict(xtest)

# Calculate accuracy of the model
accuracy = accuracy_score(ytest, y_pred)
print(f"Accuracy of the model: {accuracy:.2f}")
