import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Load the dataset
data = pd.read_csv("iris.csv")

# Split features and target variable
X = data.drop('Species', axis=1)
y = data['Species']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Naive Bayes classifier
model = GaussianNB()

# Train the classifier
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Compute confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Calculate TP, FP, TN, FN
TP = conf_matrix[1][1]
FP = conf_matrix[0][1]
TN = conf_matrix[0][0]
FN = conf_matrix[1][0]

# Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

# Calculate Error Rate
error_rate = 1 - accuracy

# Calculate Precision
precision = precision_score(y_test, y_pred, average='macro')

# Calculate Recall
recall = recall_score(y_test, y_pred, average='macro')

print("Accuracy:", accuracy)
print("Error Rate:", error_rate)
print("Precision:", precision)
print("Recall:", recall)
