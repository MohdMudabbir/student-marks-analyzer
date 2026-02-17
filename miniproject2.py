import pandas as pd
df=pd.read_csv("students2.csv")
print(df)
print("Average is:",df["Marks"].mean())
print("Maximum is:",df["Marks"].max())
df.loc[df["Name"]=="Sammy","Marks"]=100
print(df)
print("\n")
df.loc[df["Name"]=="Bob","Age"]=75
print("Bobby age after deletion is:",df)
print("\n")
print("After removing bobby sorry:")
df=df.loc[df["Name"]!="Bob"]
print(df)
print("\n")

df=df.loc[df["Marks"]!=100]
print(df)
print("\n")

df.loc[len(df)]=["casstiel",55,92,"Pass"]
print(df)
print("\n")
df.loc[2]=["Sammy",27,100,"Fail"]
print(df)
print("\n")
df.loc[3]=["Dean",25,75,"fail"]
print(df)
print("\n")

df=pd.read_csv("students2.csv")
print(df)
df=df[df["Marks"]>80]
print(df)
print("\n")
df=df.loc[df["Age"]<50]
print(df)
df.to_csv("students.csv",index=False)
print("our home work is:\n")
print("\n")
print("\n")
print("\n")
df.loc[2]=["Sara",22,75,"Pass"]
print(df)
print("updating sara:\n")
df.loc[df["Name"]=="Sara","Marks"]=88
print(df)
print("Marks greater than 80 is:\n")
greater_80=df.loc[df["Marks"]>=87]
print(greater_80)
print("Deleting Sara:\n")
df.loc[df["Name"]!="sara"]
print("Deleting sara ",df)
df.to_csv("students2.csv",index=False)
