import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_data = pd.read_csv(url, names=column_names)

# 1. List down the features and their types
feature_types = iris_data.dtypes
print("Features and their types:")
print(feature_types)

# 2. Create a histogram for each feature
iris_data.hist(figsize=(10, 8))
plt.suptitle('Histograms of Iris Dataset Features', y=0.95)
plt.show()

# 3. Create a boxplot for each feature
plt.figure(figsize=(10, 8))
sns.boxplot(data=iris_data)
plt.title('Boxplots of Iris Dataset Features')
plt.show()

# 4. Compare distributions and identify outliers
# Here, you can visually inspect the histograms and boxplots to compare distributions and identify outliers.

# Visual inspection of histograms
plt.figure(figsize=(12, 8))
for i, feature in enumerate(iris_data.columns[:-1]):
    plt.subplot(2, 2, i + 1)
    sns.histplot(iris_data[feature])
    plt.title(f'Histogram of {feature}')
plt.tight_layout()
plt.show()

# Visual inspection of boxplots
plt.figure(figsize=(12, 8))
for i, feature in enumerate(iris_data.columns[:-1]):
    plt.subplot(2, 2, i + 1)
    sns.boxplot(data=iris_data, x='species', y=feature)
    plt.title(f'Boxplot of {feature} by Species')
plt.tight_layout()
plt.show()
