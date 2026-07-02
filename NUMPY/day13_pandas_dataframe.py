import pandas as pd 
data={
    "Name":["Arsh","Aman","Priya","Rahul","Simran"],
    "Roll No":[101,102,103,104,105],
    "Marks":[75,82,91,68,88],
    "Age":[19,20,21,22,21]
}
df=pd.DataFrame(data)
print(df)
print("Name: ",data["Name"])
print("Marks: ",data["Marks"])
print("Name and Age: ",df[["Name","Age"]])
print("First row:",df.iloc[0])
print("Third Row: ",df.iloc[2])
print("Last row:",df.iloc[-1])
print("2 to 4 rows:",df.iloc[1:4])
print("\nshape: ",df.shape)
print("\coloumns:",df.columns)
print("\ninfo:",df.info())
print("\ndescribe: ",df.describe())
print("head:\n",df.head())
print("\nhead till 3",df.head(3))
print("\ntail: ",df.tail())
print("\ntail till 2:",df.tail(2))
df["Result"]=["Pass","Pass","Pass","Fail","Pass"]
print("\nresult:",df["Result"])
df["Grade"] = ["C", "B", "A", "D", "B"]
print("\ngrade:",df["Grade"])
print("\nUpdated DataFrame:")
print(df)