import pandas as pd
import opendatasets as od
import numpy as np

od.download("https://www.kaggle.com/datasets/sankha1998/student-semester-result")

df = pd.read_csv("student-semester-result/data.csv")

# missing values
df.isnull().sum()

# to check datatpyes
df.info()

# handle missing values
# marks
avg1 = df["1st"].astype("float64").mean(axis=0)
avg2 = df["2nd"].astype("float64").mean(axis=0)
avg3 = df["3rd"].astype("float64").mean(axis=0)
avg4 = df["4th"].astype("float64").mean(axis=0)
avg5 = df["5th"].astype("float64").mean(axis=0)

df["1st"]=df["1st"].replace(np.nan, avg1)
df["2nd"]=df["2nd"].replace(np.nan, avg2)
df["3rd"]=df["3rd"].replace(np.nan, avg3)
df["4th"]=df["4th"].replace(np.nan, avg4)
df["5th"]=df["5th"].replace(np.nan, avg5)

# handle missing values
# roll
roll = df["Roll"].astype("float64").mean(axis=0)
df["Roll"]=df["Roll"].replace(np.nan, roll)

# handle missing values
# roll
df['Gender']=df['Gender'].replace(np.nan,"Female")

# Converting it to normal dist. by conv cgpa to percentage
max1 = df['1st'].max()
max2 = df['2nd'].max()
max3 = df['3rd'].max()
max4 = df['4th'].max()
max5 = df['5th'].max()

cgcol = [ '1st' ,'2nd', '3rd', '4th', '5th' ]
maxcol = [max1 , max2, max3, max4, max5]

arr =  zip(cgcol, maxcol)
for col, max in arr:
    df[col+"_%"] = (df[col] / max) * 100
