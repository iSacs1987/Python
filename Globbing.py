"""
This is an example script for the module glob, which allows us to search for
files of a specific type in our directory
"""
# The import is pretty simple again
import glob

# Now we can use the glob method of our glob module.
files = glob.glob("*")  # Returns a list of all files
images = glob.glob("*.png")  # Returns a list of files with the extension .png
# Please keep in mind that the list is in arbitrary order.
print(files)
print(images)
