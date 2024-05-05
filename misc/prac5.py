import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import opendatasets as od
from pandas.core.common import random_state
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score

od.download("https://www.kaggle.com/datasets/rakeshrau/social-network-ads")

data = pd.read_csv("social-network-ads/Social_Network_Ads.csv")

X = data[['Age', 'EstimatedSalary']]
y = data['Purchased']

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
print(y_pred)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Recall Score
recall = recall_score(y_test, y_pred)
print("Recall Score:", recall)

# Precision Score
precision = precision_score(y_test, y_pred)
print("Precision Score:", precision)

# Accuracy Score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Score:", accuracy)
