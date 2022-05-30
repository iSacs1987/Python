"""
This is the example script for working with the module Pandas and its DataFrame
objects. In this script we see how you can create a Series and a DataFrame.
Afterwards we use some simple methods on the DataFrame
"""
# First we import the two modules we need for this script
import numpy as np
import pandas as pd
# Now I can create a Series object with pd.Series and handing over a list of
# elements. In contrast to the ndarrays of NumPy we can mix datatypes here.
s = pd.Series([1, 3, 5, np.nan, 6, 8,"Hello"])
# This second object is a DataFrame a form of data table. We can create such an
# object by handing over a matrix, e.g. from NumPy and than we can hand over
# our row names (index) in form of a list and the column names (columns) also
# in form of a list, to be able to access our values later on according to these
# names.
df = pd.DataFrame(np.random.randn(4,6), index=["Test1","Test3","Test2","Test4"], columns=["A","B","C","D","E","F"])
# If we just hand over row and column names we can create an empty DataFrame
df2 = pd.DataFrame(index=["Test1","Test3","Test2","Test4"], columns=["A","B","C","D","E","F"])
# If we don't hand over row or column names, these are generated automatically
# as numbers starting with 0
df3 = pd.DataFrame(np.random.randn(4,6))
# Of course we can choose to hand over only column names or only row names as
# well. Now the name which were NOT handed over are generated automatically
# again.
df4 = pd.DataFrame(np.random.randn(4,6),columns=["A","B","C","D","E","F"])
df5 = pd.DataFrame(np.random.randn(4,6), index=["Test1","Test3","Test2","Test4"])
# If we just hand over column or row names we get an empty DataFrame which does
# NOT have any rows or columns respectively. So this is not so good.
df6 = pd.DataFrame(columns=["A","B","C","D","E","F"])
df7 = pd.DataFrame(index=["Test1","Test3","Test2","Test4"])
# Now we can print out our Objects
print("Our Series:",s)
print("Our complete DataFrame:\n",df)
print("Our empty DataFrame:\n",df2)
print("Our DataFrame without row or column names:\n",df3)
print("Our DataFrame with column names only:\n",df4)
print("Our DataFrame with row names only:\n",df5)
print("Our DataFrame with column names only without data:\n",df6)
print("Our DataFrame with row names only without data:\n",df7)
print("")
 # Now I print out the types of our first two objects, so that you can see the
 # corresponding object names.
print(type(s))
print(type(df))
print("")
# Now I want to show you the usage of some pandas methods. Per default these
# methods work on columns. So df.sum() for example returns a sum for each column
print("Sums of the columns:\n",df.sum())
# By handing over axis=1 as argument we can change this behavior and calculate
# the sums of our rows.
print("Sums of the row:\n",df.sum(axis=1))
print("")
# The describe method returns mean, maximum , minimun values, standard deviation
# and some medians for each column of your DataFrame.
print("Description of our DataFrame:\n",df.describe())
print("")
# We can sort our DataFrame according to the row and column names with the help
# of df.sort_index() per default your DataFrame is sorted according to your row
# names (index).
print("DataFrame sorted according to row names:\n",df.sort_index())
print("")
# By using axis=1 as argument you can now sort your DataFrame according to your
# column names. We can use ascending=False to get a descending order in this
# case to see what happens
print("DataFrame sorted according to column names:\n",df.sort_index(axis=1,ascending=False))
print("")
# We can also sort our DataFrames according to the value they contain. Per
# default this emthod works on columns. So we can hand over the column we want
# to use as basis for our sorting with the by keyword.
print("DataFrame sorted according to column B:\n",df.sort_values(by="B"))
print("")
# If we want to sort according to a row we have to use again axis=1 and than
# the by keyword with the corresponding row name.
print("DataFrame sorted according to row Test2:\n",df.sort_values(by="Test2",axis=1))
print("")
# Last but not least we can get access to all row names by using df.index and
# all column names by df.columns.
print("Row Names of our DataFrame:",df.index)
print("Column Names of our DataFrame:",df.columns)
# We can use these methods to create loops that iterate over our DataFrame and
# run different operations on the elements of our DataFrame. For more details
# about accessing values in DataFrames see AccessPandas.py
for elem in df.index:
    print("The Current Row Name is",elem)
# Keep in mind that df.index and df.column are only generator methods similar
# to range(). So if you want to work with the elements inside of these methods
# in form of a list, you have to cast them to a list as we already saw with
# the range generator
print("Row Names of our DataFrame as List:",list(df.index))
print("Column Names of our DataFrame as List:",list(df.columns))
