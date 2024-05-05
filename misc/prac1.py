import pandas as pd
import opendatasets as od

od.download("https://www.kaggle.com/datasets/toramky/automobile-dataset")

df = pd.read_csv("automobile-dataset/Automobile_dataset.csv")

print(df)

# Check Null values 
df.isnull()
df.isnull().sum()
df.notnull()
df.notnull().sum()

# if missing or datatype
# df['column_name'].fillna(value, inplace=True)
# df = pd.read_csv('data.csv', dtype={'column1': int, 'column2': str})

# print say all the names of car companies

make = df['make'].unique()
makec = df['make'].value_counts()
print(make)
print(makec)

# turn categorical variables to quantative variables, ie, make into a specific number like 1,2,3 respectively

fuel = df['fuel-type'].unique()
fuelc = df['fuel-type'].value_counts()
print(fuel)
print(fuelc)

mapping = { 'gas': 1 , 'diesel' : 2 }
df['fuel-type-number'] = df['fuel-type'].map(mapping)
df.head()
