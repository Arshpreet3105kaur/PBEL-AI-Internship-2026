import pandas as pd
data={
    "Name":["Arsh","Aman","Riya"], 
    "Age":[20, 22, 21],
    "Marks":[75,82,91]
}
df=pd.DataFrame(data)
print("head:\n",df.head())
print("tail:\n",df.tail(2))
print("\nInfo:",df.info())
print("\ndescribe:",df.describe())