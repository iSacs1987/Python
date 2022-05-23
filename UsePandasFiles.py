import pandas as pd

data1 = pd.read_excel("Cation.xlsx")
data2 = pd.read_excel("Cation.xlsx", sheet_name="Separations")
data3 = pd.read_excel("Cation.xlsx", sheet_name=None)

print(data1)
print(data2)
print(data3)

data1.to_excel("NewFile.xlsx")
data1.to_csv("NewFile.csv")

data4 = pd.read_csv("NewFile.csv")
print(data4)
