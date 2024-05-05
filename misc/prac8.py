from pandas._libs.tslibs import timestamps
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt


# Load the Titanic dataset
titanic_data = sns.load_dataset('titanic')

sns.countplot(data=titanic_data, x='sex', hue='survived')

sns.histplot(data=titanic_data, x='fare', hue='survived')

# Set seaborn theme
sns.set_theme()

# Pairplot to visualize patterns
sns.pairplot(titanic_data, hue='survived', palette='husl', diag_kind='kde')
plt.show()
