"""
This is an example script for working with Numpy and his ndarray objects. We
will just see how you can create these arrays and use some simple methods on
them like sum(), max(), min(), shape, reshape() and transpose(). There are also
a number of different mathematical operations that are available to use in numpy
but we won't cover them here. If you're interested in them use the following
link https://numpy.org/ and look them up under Documentation ==> API reference.
"""
# First we import NumPy with the alias of np. This is an international
# convention to shorten your code and to make sure that your use the right
# methods. Numpy uses methods whose names are identical to methods from SciPy or
# other modules and thus to make sure Python knows which method to use we need
# the point notation.
import numpy as np
# Now we can create our ndarray objects. I used the same examples as in my
# presentation, to make things more understandable.
# First we use the np.array() method to cast a list to an array
array1 = np.array([4,3,2,1])
# Second we use the np.arange() method to create an array that contains numbers
# from 0 until 3. The method is similiar to the range generator we used before
# and can also take up to three arguments. One argument means, we hand over only
# the end of our array and get an array with elements starting at 0 and ending
# right before the handed over argument. Two arguments mean we hand over the
# start and end value. Again the start value is included while the end value is
# excluded. Three arguments mean we hand over the start value, the end value and
# the step size.
array2 = np.arange(4) # Elements: 0 1 2 3
array11 = np.arange(3,9) # Elements: 3 4 5 6 7 8
array12 = np.arange(3,28,3) # Elements: 3 6 9 12 15 18 21 24 27
# Furthermore we can create array which contain only 0s (zeros) or only 1s
# (ones). Each ot these methods takes the dimensions your new array as arguments
# Please keep in mind that these array contain floats and NOT integers.
array3 = np.zeros(4) # An array with 4 0s
array4 = np.ones(4) # An Array with 4 1s
# If you want to create a multi-dimensional array you have to use two brackets
# and than hand over the dimensions of your array to these methods. Here we
# create an array that contains 3 array with 4 subarray and each of these
# subarray contain 2 elements.
array5 = np.zeros((3,4,2))
# We can also change the dimensions of our arrays using reshape. But the new
# dimensions have to fit the number of elements in our array correctly. That
# means in the example below I create an array that contains 15 elements with
# the arange method. So Now my new array has to have exactly 15 elements as well
# Therefore I can only use dimensions like (3,5) or (5,3) which both also have
# 15 elements.
array6 = np.arange(15).reshape(3, 5)
# Last but not least we can create array with the help of random generators. As
# with mathematical operations we have a wide number of methods available to us
# here. I used a generator which returns values from the “standard normal”
# distribution with a mean of 0 and a standard deviation of 1. Again I can hand
# over the dimensions my array should have. Here I create an array with 6
# subarrays which contain 4 numbers each.
array7 = np.random.randn(6,4)
# Now I can print out my array
print("Using np.array([4,3,2,1]) returns:",array1)
print("Using np.arange(4) returns:",array2)
print("Using np.arange(3,9) returns:",array11)
print("Using np.arange(3,28,3) returns:",array12)
print("Using np.zeros(4) returns:",array3)
print("Using np.ones(4) returns:",array4)
print("Using np.zerose((3,4,2)) returns:\n",array5)
print("Using np.arange(15).reshape(3,5) returns:\n",array6)
print("Using np.random.randn(6,4) returns:\n",array7)
print("")
# We can use simple methods on our lists to calculate the sum of all elements
# sum() or to get the minimum value or maximum value of our array min() and
# max() respectively. These methods return the corresponding value in the same
# datatype of your elements. That means if you have an array with integers the
# returned values are also integers and if you have an array with floats the
# retured values are also floats.
print("Sum of elements of array1:",array1.sum())
print("Min of elements of array1:",array1.min())
print("Max of elements of array1:",array1.max())

print("Sum of elements of array7:",array7.sum())
print("Min of elements of array7:",array7.min())
print("Max of elements of array7:",array7.max())
print("")
# We can change the dimensions of our arrays with the help of the transpose
# method to make the columns of our original matrix into rows in our new matrix
# and vice versa. This also works on arrays with mor dimensions. In all cases
# the order of your dimensions are reversed. So an array with dimensions 6,4
# gets transposed to an array with dimensions 4,6 and an array with dimensions
# 3,4,2 gets transposed to an array with dimension 2,4,3 etc. These methods do
# NOT work in place that means you do NOT make any changes to your original
# array. Do show you this I print out the dimensions of array7 using the shape
# method, which returns the dimension of the corresponding array. You will see
# that these dimensions stay the same.
print("Dimensions of array7 before tranpose():",array7.shape)
print("The transposed array7:\n",array7.transpose())
print("Dimensions of array7 after tranpose():",array7.shape)
print("")
# Last but not least I want to give you some examples how calculations are done
# elementwise in Numpy arrays. Here I have some simple mathematical operations
# and you will see that the results show that each element of the corresponding
# array was changed.
array8 = array1 * 4
print("Adding 4 to array1 returns:",array8)
array9 = array8 - 2
print("Subtracting 2 from the previous array returns:",array9)
array10 = array7 * 5
print("Multiplying array7 by 5 returns:\n",array10)
