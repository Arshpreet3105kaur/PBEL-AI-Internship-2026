import pandas as pd

marks = pd.Series([75, 82, 91, 68, 88])

print("Original:")
print(marks)

print("\nGrace Marks (+5):")
print(marks + 5)

print("\nDouble Marks:")
print(marks * 2)

print("\nSquare:")
print(marks ** 2)
print(marks.iloc[-1])
print(marks.iloc[-2])
print(marks.iloc[1:4])