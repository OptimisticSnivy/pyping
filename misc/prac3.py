import pandas as pd
import statistics as st
import numpy as np
import opendatasets as od

od.download("https://www.kaggle.com/datasets/uciml/iris")

df = pd.read_csv("iris/Iris.csv")

df.head()

# Stats-1
mode_summary = df.groupby('Species')['SepalLengthCm'].apply(lambda x: st.mode(x))
print("Mode :")
print(mode_summary)

median_summary = df.groupby('Species')['SepalLengthCm'].median()
print("Median :")
print(median_summary)

mean_summary = df.groupby('Species')['SepalLengthCm'].mean()
print("Mean :")
print(mean_summary)

# Stats-2
Species_numeric_value = df.groupby('Species').size().tolist()
Species_stats = df.groupby('Species').describe()
print(Species_stats)

setsoa_stats = df[df['Species'] == 'Iris-setosa'].describe()
vericolor_stats = df[df['Species'] == 'Iris-veriscolor'].describe()
virginica_stats = df[df['Species'] == 'Iris-virginica'].describe()
print("Setosa Statistics")
print(setsoa_stats)
print("\nVeriscolor Statistics")
print(vericolor_stats)
print("\nVirginica Statistics")
print(virginica_stats)
