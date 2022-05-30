"""
This is the example script for accessing value in your DataFrames. Here I will
show you some examples for accessing value in your DataFrames, accessing whole
columns and rows as well as how to add columns and rows to your DataFrames.
"""
# First we have to import the needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Now I create again a Series and a DataFrame. This time I included the index
# keyword in my Series creation as well, to have names for each element in my
# Series later on.
s = pd.Series([1, 3, 5, np.nan, 6, 8],index=["A","B","C","D","E","F"])
df = pd.DataFrame(np.random.randn(4,6), index=["Test1","Test3","Test2","Test4"], columns=["A","B","C","D","E","F"])
# Now we can print out our Objects
print("Our Series:",s)
print("Our complete DataFrame:\n",df)
print("")
# To access specific values in our Series or DataFrames we have the methods .loc
# or .iloc available. loc takes row and/or column names while iloc takes indices
# (whole numbers as we saw for lists). To access the fifth element in our Series
# we can use one of the two examples shown below.
print("Entry at index 4 of Series:",s.iloc[4])
print("Entry in row 'E' of Series:",s.loc["E"])
# For DataFrames we have to use an index for the row and an index for the column
# with iloc each in its own pair of brackets. The first index always specifies
# the row and the second one the column.
print("Entry in fourth row and third column:",df.iloc[3][2])
# For loc we can use the row and column names in one bracket separated by a
# comma. Again we have to specify the row first and than the column
print("Entry in Row 'Test4' and column 'C':",df.loc["Test4","C"])
print("")
# If we want to use a whole row of a DataFrame we can use iloc and replace the
# index of the column with a :
print("Fourth row of our DataFrame:\n",df.iloc[3][:])
print("")
# If we want to use a whole column we can do something similar, but now we have
# to use one bracket and have the indices inside it together separated by a
# comma
print("Third column of our DataFrame:\n",df.iloc[:,2])
print("")
# When using loc we can simply replace the corresponding column or row name with
# a : and get access to the whole row or column
print("Row 'Test4' of our DataFrame:\n",df.loc["Test4",:])
print("")
print("Column 'A' of our DataFrame:\n",df.loc[:,"A"])
print("")
# I included a small loop here that plots the values of the rows of our
# DataFrame as a Scatterplot. I use a Dictionary to change the marker and color
# for each row.
colors = {"Test1":"k*","Test2":"r.","Test3":"gd","Test4":"bs"}
plt.figure()
# As I mentioned in UsePandas.py we can use df.index for the creation of loops
# so here I loop over the rows of our DataFrame and plot them against a range
# from 0 to 5
for elem in df.index:
    print(df.loc[elem,:])
    plt.plot(np.arange(6),df.loc[elem,:],colors[elem])
plt.show()
plt.close()
# Last but not least I want to show you how you can add new columns and rows to
# your DataFrames in a simple manner. By using row or column names that do NOT
# exist in your current DataFrame in combination with the .loc method we can
# add these rows and/or columns to our DataFrame.
df.loc["Test5","E"] = np.random.randn(1) # The row "Test5" is added
df.loc["Test2","K"] = np.random.randn(1) # The column "K" is added
print("Our complete DataFrame:\n",df)
# Please keep in mind that these columns/rows are just added to the end of your
# DataFrame, that means in the example below our new column "H" comes after the
# column "K".
df.loc["Test3","H"] = np.random.randn(1)
print("Our complete DataFrame:\n",df)
