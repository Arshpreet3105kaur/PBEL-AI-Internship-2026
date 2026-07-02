import pandas as pd 
data={
    "Name":["Arsh","Aman","Riya"],
    "Age":[20, 22, 21],
    "Marks":[75,82,91]
}
df=pd.DataFrame(data)
print (df)
print("\nShape:", df.shape)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Column Names:", df.columns)
print("Only Marks:")
print(df["Marks"])

print("\nOnly Name:")
print(df["Name"])

print("\nName and Age:")
print(df[["Name", "Age"]])