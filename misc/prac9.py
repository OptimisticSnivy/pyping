from pandas._libs.tslibs import timestamps
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt


# Load the Titanic dataset
titanic_data = sns.load_dataset('titanic')

# Null values
titanic_data.isnull().sum()

titanic_data['age'] = titanic_data['age'].fillna(titanic_data['age'].mean())

# Plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=titanic_data, x='sex', y='age', hue='survived', palette='Set2')
plt.title('Distribution of Age by Gender and Survival Status')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

# Plot with fixed legend
plt.figure(figsize=(10, 6))
box = sns.boxplot(data=titanic_data, x='sex', y='age', hue='survived', palette='Set2')

# Customize legend handles to use colored patches instead of lines
handles, labels = box.get_legend_handles_labels()
colors = sns.color_palette('Set2')[:2]
plt.legend(handles=handles[:2], labels=['No', 'Yes'], loc='upper right', title='Survived', facecolor='white')

plt.title('Distribution of Age by Gender and Survival Status')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()
