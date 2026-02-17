import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\HP\my python\students3.csv")
print(df)
print("\n")
df["Marks"]=pd.to_numeric(df["Marks"])
print("\n")
print(df.head())
print("\n")
print(df.isnull())
print("\n")
print(df.isnull().sum())
print("\n")
df["Result"]=df["Marks"].apply(lambda x: "pass" if x>=40 else "Fail")
print(df)
print("\n")
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
print(df)
print("\n")
top=df["Marks"].max()
print(top)
print("\n")
top1=df.loc[df["Marks"].idxmax()]
print(top1)
df.plot(x="Name",y="Marks",kind="bar")
plt.show()
print("\n")
df["Result"].value_counts().plot(kind="pie",autopct="%1.1f%%")
plt.show()
print("\n")



















