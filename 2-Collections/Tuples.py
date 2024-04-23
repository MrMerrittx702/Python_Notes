#===============================================================================================================================#
'''Python Tuples'''
#===============================================================================================================================#
'''
Covered in this file:
  > Tuple Defined
  > Creating a Tuple
  > Tuple Operations 
  > Accessing Data
  > Common built-in tuple function calls 
  > Common built-in tuple methods calls
  > Tuple Slicing and Concatenation
  > Tuples of Tuples: Nested Tuples
  > Unpacking Collections
  > Looping through Tuples
'''


#===============================================================================================================================#
'> Tuple Defined'

''' 
A tuple is basically an immutable list

A tuple is an ordered collection of elements enclosed within parentheses (). 
> are immutable 
> can contain elements of different data types
'''
# ordered meaning it has a specific order 0,1,2,...
# immutable meaning it cannot be changed

("a","b","c","d","e") #tuples(contains multiple items called elements)
# 0   1   2   3   4   #indexes (are used to access each element)
# length = 5          #The length is the total number of elements

# tuple indexes always start at 0 
#In this example:
#   a,b,c,d,e are elements
#   0,1,2,3,4 are indexes
#   length = 5

'''
There are four collection data types in the Python programming language:

> List: collection which is ordered and mutable. Allows duplicate members.

> Tuple: collection which is ordered and immutable. Allows duplicate members.

> Set: collection which is unordered, unchangeable*, and unindexed. No duplicate members.

> Dictionary: collection which is ordered** and changeable. No duplicate members.
'''

#===============================================================================================================================#
'> Creating a Tuple'
#once initialized a tuple cannot be changed

#use () to denote and empty tuple
tuple1d = ()

#use a trailing , for a tuple with a single value
tuple1d = ("a",)
#OR
tuple1d = "a", 


#use commas to seperate items
#declare      initialize
tuple1d = (1,2,3,4,5,6,7,8,9) 
#index     0 1 2 3 4 5 6 7 8
#length = 9

#OR
tuple1d = "a", "b", "c"
#index     0    1    2
#length = 3

#use the tuple(iterable) constructor call
tuple() #()
tuple('abcdef') #('a', 'b', 'c', 'd', 'e', 'f')


#===============================================================================================================================#
'> Converting from Lists and Sets'
list1d = ["a","b","c"]
set1d = {"a","b","c"}

#From list or set to tuple use tuple()
tuple1d = tuple(list1d)
tuple1d = tuple(set1d)


#From tuple to a list with list()
list1d = list(tuple1d)

#From a tuple to a set with set()
set1d = set(tuple1d)

#===============================================================================================================================#
'> Tuple Operations '

#multi variable assignment with lists
a, b, c = (1,2,3)
#a = 1 b = 2 c = 3

numerals = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

alpha = (
  'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l', 
  'm', 'n', 'o', 'p', 'q', 'r', 
  's', 't', 'u', 'v', 'w', 'x', 
  'y', 'z'
)

#checking membership 
"a" in alpha #True
"1" in numerals #True

"a" not in alpha #False
"1" not in numerals #False

#concatenation
numerals + alpha
('0', '1', '2', '3', '4', '5', 
 '6', '7', '8', '9', 'a', 'b', 
 'c', 'd', 'e', 'f', 'g', 'h', 
 'i', 'j', 'k', 'l', 'm', 'n', 
 'o', 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 'z')

#duplication
numerals * 3
('0', '1', '2', '3', '4', 
 '5', '6', '7', '8', '9', 
 '0', '1', '2', '3', '4', 
 '5', '6', '7', '8', '9', 
 '0', '1', '2', '3', '4', 
 '5', '6', '7', '8', '9')

#===============================================================================================================================#
'> Accessing Data'
#         (------------------elements---------------------)
tuple1d = ("a","b","c","d","e","f","g","h","i","j","k","l")
#index    ( 0   1   2   3   4   5   6   7   8   9   10  11)
#reverse  (-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1)

# elements in a tuple are accessed by their index

#Starting from the front end
tuple1d[0] #a
tuple1d[5] #f
tuple1d[10] #k

#Starting from the back end
tuple1d[-1] #l
tuple1d[-5] #h
tuple1d[-10] #c


#===============================================================================================================================#
'> Built-in tuple function calls'
'''
Functions are blocks of reusable code
  Functions are typically called using their name followed by parentheses 
    and any required arguments inside
  
      function_name(arguments)
'''

#len()
len(tuple1d)   #returns number of elements in a tuple
len(tuple1d)-1 #returns the last index of the 

#max()
max(tuple1d) #Returns the largest element in the tuple.

#min()
min(tuple1d)#Returns the smallest element in the tuple.

#sum(tuple1d)
nums = (1,2,3,4,5)
sum(nums) #Returns the sum of all elements in a number tuple.

#sorted(iterable)
sorted(tuple1d) #returns a sorted list of the specified iterable


#===============================================================================================================================#
'> Built-in methods used tuples'
'''
  Methods are functions defined by a class
    Methods are typically called using an object or class and dot (.) syntax
      object.method(parameters) --> for methods which require objects
        or
      class.method(paramters) --> for methods which do not require objects
'''

#To see what methods you can call on an object use dir(object)
#To see more information on a specific method use help(object.method)

#.index(x, start, end)
tuple1d.index("elem")# Returns the index of the first occurrence of element x 
tuple1d.index("elem",2,5)#(optional start and end indices can be specified).

#.count(x)
tuple1d.count("elem")# Returns the number of occurrences of element x in the tuple.


#===============================================================================================================================#
'> Tuple Slicing and Concatenation'

#slicing returns a part of the original tuple
#tuple[start_index:stop_index:step] 
tuple1d = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
print(tuple1d[0:]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(tuple1d[:3]) #['a', 'b', 'c']
print(tuple1d[0:5]) #[0,1,2,3,4]
print(tuple1d[:6:3])#['a', 'd']
print(tuple1d[1:6:2]) #[1, 3, 5]
#note the stop_index is not included in the slice

#tuples can be concatenated
tuple1d_1= (0,1,2,3,4,5,6,7,8,9)
tuple1d_2 = (11,12,13,14,15,16,17,18,19)
print(tuple1d_1 + tuple1d_2) 
#(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19)


#===============================================================================================================================#
'> Tuples of Tuples: Nested Tuples'

#a 2D tuple is a tuple of tuples
#index    ((---------tuple 0-------),(--------tuple 1--------),(--------tuple 2--------),(--------tuple 3--------))
#reverse  ((---------tuple -4------),(--------tuple-3--------),(--------tuple -2-------),(--------tuple -1-------))
tuple2d = (("a","b","c","d","e","f"),("g","h","i","j","k","l"),("m","n","o","p","q","r"),("s","t","u","v","w","x"))
#index    (( 0   1   2   3   4   5 ),( 0   1   2   3   4   5 ),( 0   1   2   3   4   5 ),( 0   1   2   3   4   5 ))
#reverse  ((-6  -5  -4  -3  -2  -1 ),(-6  -5  -4  -3  -2  -1 ),(-6  -5  -4  -3  -2  -1 ),(-6  -5  -4  -3  -2  -1 ))               
# tuple2d is a tuple of 4 tuples


#simplify by formatting the code this way 
tuple2d = (
  ("a","b","c","d","e","f"), #tuple 0 
  ("g","h","i","j","k","l"), #tuple 1 
  ("m","n","o","p","q","r"), #tuple 2 
  ("s","t","u","v","w","x")  #tuple 3 
)


#simplify in our mind as rows and columns 
tuple2d = (
  ("a","b","c","d","e","f"), # 0
  ("g","h","i","j","k","l"), # 1 row 
  ("m","n","o","p","q","r"), # 2   indexes
  ("s","t","u","v","w","x")  # 3
  # 0   1   2   3   4   5
) #    column indexes


#access elements (use the tuple name and [row][col] to access an element)
#tuple[row][col]
tuple2d[0][0] # a
tuple2d[0][1] # b
tuple2d[3][5] # z


#len()function call returns the number of elements in the tuple
len(tuple2d)   # 4 (number of rows/tuples)
len(tuple2d)-1 # 3 (last row index)


row = 0 #represents the row, in this case the row at index 0 
len(tuple2d[row])   # 6 number of columns/elements in a given row/tuple
len(tuple2d[row])-1 # 5 last column index 

#===============================================================================================================================#
'> Unpacking Tuples'
'''
 refers to the process of extracting individual elements 
 from a container (such as a list, tuple, dictionary)
'''
#Unpack iterable types using *
l1 = (1,2,3)
l2 = (4,5,6)
print( (*l1,*l2) ) # (1,2,3,4,5,6)

#===============================================================================================================================#
'> Looping through Tuples'

alphanumeric = (
 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
 'y', 'z')

#for index in range(len(tuple)):
for i in range(len(alphanumeric)):
  print(i) #prints each index of alphanumeric


# for element in tuple:
for char in alphanumeric:
  print(char) #prints each element of alphanumberic


#for index, element in enumerate(tuple):
for index,element in enumerate(alphanumeric):
  print(index, element)


num = (x for x in range(1,27))
upper_alpha = (chr(x) for x in range(65,91)) 
lower_alpha = (chr(x) for x in range(97,123))

alphabet = ()

#for item1, item2,... in zip(iter1,iter2,...)
for number, upper, lower in zip(num, upper_alpha, lower_alpha):
  print(number,upper,lower)
#===============================================================================================================================#




































