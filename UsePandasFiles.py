"""
This is our last example script for working with pandas. Here I will show you
how to read in / save Excel and csv files.
"""
# First we have to import pandas
import pandas as pd
# Now we can read in an Excel-file. i have a buig Excel file with many different
# sheets available here. When we run pd.read_excel() just with the name of our
# file as argument, only the first sheet is read in as a DataFrame
data1 = pd.read_excel("Cation.xlsx")
# If we use the keyword sheet_name we can specifiy which Sheet we want to read
# in as a DataFrame
data2 = pd.read_excel("Cation.xlsx", sheet_name="Separations")
# If we use the keyword sheet_name in combination with the None operator, all
# Sheets are read in. That means data3 is a dictionary and the keys of this
# dictionary are the names of our sheets in the excel file. The values are than
# the corresponding DataFrames.
data3 = pd.read_excel("Cation.xlsx", sheet_name=None)
# Per default pandas does NOT use the first column in your file as row names but
# as part of the data. To change this behavior we have to use the index_col
# keyword and hand over the index of the column we want to use as row names. So
# here we use the first column in our Excel file as row names.
data4 = pd.read_excel("Cation.xlsx",index_col=0)
# Now we can print out our variables
print("Just the Excel-file name:\n",data1)
print("")
print("Specifiying the sheet 'Separations';\n",data2)
print("")
print("The whole file as a dictionary:\n",data3)
print("")
print("The value for the key 'Separations' in the dicitonary:\n",data3["Separations"])
print("")
print("Using the keyword index_col:\n",data4)
print("")
print("The corresponding indices:",data4.index)
print("")
# We can save our data to Excel-files with the help of the to_excel method. This
# method takes only the name of the Excel-file you want to create and saves your
# DataFrame as this file.
data1.to_excel("NewFile.xlsx")
# Similiar to to_excel we can use to_csv to create a comma separated csv file
# which contains our DataFrame
data1.to_csv("NewFile.csv")
# We can read in csv files similiar to excel files. The read_csv method allows
# us to read in the data from the file as a DataFrame.
data5 = pd.read_csv("NewFile.csv")
print("Newly read in DataFrame:\n",data5)
print("")
# Again we do NOT get row names from our file. To use row names that were
# specified beforhand we have to use the keyword index_col again.
data6 = pd.read_csv("NewFile.csv",index_col=0)
print("Newly read in DataFrame:\n",data6)
