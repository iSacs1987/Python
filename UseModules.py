"""
This is the example script for working with modules. It shows examples of three
different ways to import modules into your programs.
"""
# First we can import the whole module with the simple import command. Here we
# import the module calendar. Please make sure that your scripts don't have the
# same name as modules because import looks inside your directory first and thus
# would import your own script instead of the module
import calendar

# After you imported the module you can access it's methods with the point
# notation we already swa when working with lists. The method prcal here prints
# out the calendar for a specific year (2022).
calendar.prcal(2022)
# Another way to import modules is to use alias. So here I import again the
# whole module calendar but since I'm lazy I don't want to type calendar all the
# time when workign with its methods. Thata why I tell python ok instead of
# calendar I use cld (that is done with the as cld statement)
import calendar as cld

# Now I can access the mtohods of calendar again with the point notation but I
# can use the alias (cld) instead of the whole name (calendar)
cld.prcal(2021)
# Last but not least we can also import only the methods or functions we need
# from a module. This is done as shown below. Here I only want the prcal method
# from my module calendar. If you want multiple methods you can write all of
# them after the import statement separated by comma.
from calendar import prcal

# Since I now imported the method prcal to my program (or my current namespace)
# I can use it similiar to how we use print() for example. So simple call the
# method and put the corresponding argument in brackets.
prcal(2020)
