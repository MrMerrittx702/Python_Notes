#===============================================================================================================================#
'''Python Lists'''
#===============================================================================================================================#

'''
  Covered in this video:
  > Defining a list
  > Creating a List 
  > Converting from Tuples and Sets
  > List Operations
  > Accessing Data
  > Changing Data
  > Built-in list function calls 
  > Built-in list methods calls
  > List Slicing and Concatenation
  > Lists of Lists: Nested Lists
  > Unpacking Collections
  > List Comprehension
  > Looping through lists
'''

'''
Vocabulary:
    > List
    > Mutable
    > Index
    > Element
    > Iterable
    > Iterator
    > Constructor
    > Membership
    > Concatenation
    > Duplication
    > Return
    > Slicing
    > Ascending
    > Descending
    > Comprehension
    > Unpacking
'''

#===============================================================================================================================#
'> Defining a list'

'A list is an ordered mutable collection of data, with multiple comma seperated values.'
# ordered meaning it has a specific order 0,1,2,...
# mutable meaning it can be changed

["a","b","c","d","e"] #list (contains multiple items called elements)
# 0   1   2   3   4   #indexes (are used to access each element)
# length = 5          #The length is the total number of elements

# List indexes always start at 0 
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
'> Creating a List'

# use [] to denote and empty list
list1d = []

#use [] seperating items with commas
#declare      initialize
list1d = [1,2,3,4,5,6,7,8,9] 
#index    0 1 2 3 4 5 6 7 8
#length = 9

#use the list(iterable) constructor call
list() #[]
list('abcdef') #['a', 'b', 'c', 'd', 'e', 'f']

#===============================================================================================================================#
'> Defining a list'
tuple1d = (1,2,3,4,5)
set1d = {1,2,3,4,5}


#From tuple or set to list use list()
list1d = list(tuple1d) #[1,2,3,4,5]
list1d = list(set1d) #[1,2,3,4,5]

#From list to tuple use tuple()
tuple1d = tuple(list1d) #(1,2,3,4,5)

#From list to set use set()
set1d = set(list1d) #{1,2,3,4,5}

#===============================================================================================================================#
'> List Operations'

#multi variable assignment with lists
a, b, c = [1,2,3]
#a = 1 b = 2 c = 3

numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alpha = [
  'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l', 
  'm', 'n', 'o', 'p', 'q', 'r', 
  's', 't', 'u', 'v', 'w', 'x', 
  'y', 'z'
]

#checking membership 
"a" in alpha #True
"1" in numerals #True

"a" not in alpha #False
"1" not in numerals#False

#concatenation
numerals + alpha
['0', '1', '2', '3', '4', '5', 
 '6', '7', '8', '9', 'a', 'b', 
 'c', 'd', 'e', 'f', 'g', 'h', 
 'i', 'j', 'k', 'l', 'm', 'n', 
 'o', 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 'z']

a = [1,2,3,4]
a += [5,6,7,8]
a += [9,10,11,12]
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#duplication
numerals * 3
['0', '1', '2', '3', '4', 
 '5', '6', '7', '8', '9', 
 '0', '1', '2', '3', '4', 
 '5', '6', '7', '8', '9', 
 '0', '1', '2', '3', '4', 
 '5', '6', '7', '8', '9']

b =[1,0]
b *= 5
print(b) #[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

#===============================================================================================================================#
'> Accessing Data'
list1d = ["a","b","c","d","e","f","g","h","i","j","k","l"]
#index     0   1   2   3   4   5   6   7   8   9   10  11
#reverse  -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1

# elements in a list are accessed by their index

#Starting from the front end
list1d[0] #a
list1d[5] #f
list1d[10] #k

#Starting from the back end
list1d[-1] #l
list1d[-5] #h
list1d[-10] #c

#===============================================================================================================================#
'> Changing Data'
#        [------------------elements---------------------]
list1d = ["a","b","c","d","e","f","g","h","i","j","k","l"]
#index   [ 0   1   2   3   4   5   6   7   8   9   10  11]
#reverse [-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1]

# elements in a list are changed by assigning a new value to its index

#Starting from the front end
list1d[0] = "z" 
list1d[5] = "y" 
list1d[10] = "x" 

#Starting from the back end
list1d[-1] = "m"
list1d[-5] = "n"
list1d[-10] = "o"

#Here is the new list:
list1d = ["z","b","o","d","e","y","g","n","i","j","x","m"]
#index   [ 0   1   2   3   4   5   6   7   8   9   10  11]
#reverse [-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1]

#===============================================================================================================================#
'> Built-in list function calls'
'''
Functions are blocks of reusable code, the perform a task
  Functions are typically called using their name followed by parentheses 
    and any required arguments inside
  
      function_name(arguments)
'''

#len()
len(list1d)   #returns number of elements in a list
len(list1d)-1 #returns the last index of the list

#max()
max(list1d) #Returns the largest element in the list.

#min()
min(list1d)#Returns the smallest element in the list.

#sum(list1d)
nums = [1,2,3,4,5]
sum(nums) #Returns the sum of all elements in a number list.

# Returns the list reversed
reversed(list1d)

# Returns an iterator of tuples containing the index, and elem of the list.
enumerate(list1d)

#Returns a sorted list in ascending order
sorted(list1d)

#Combines two lists into an iterator of tuples 
list1 = ["a","b","c"]
list2 = [1,2,3]
zip(list1, list2)
# ("a",1),("b",2),("c",3)



#===============================================================================================================================#
'> Built-in methods used lists'
'''
  Methods are functions defined by a class
    Methods are typically called using an object or class and dot (.) syntax
      object.method(parameters) --> for methods which require objects
        or
      class.method(parameters) --> for methods which do not require objects
'''

#To see what methods you can call on an object use dir(object)
#To see more information on a specific method use help(object.method)

#.append() 
list1d.append("new elem")# Adds a single element x to the end of the list.

#.extend(iterable)
list1d.extend("iterable")# Extends the list by appending elements from the iterable.

#.insert(i, x)
list1d.insert(5, "new elem")# Inserts an element x at a given index i.

#.remove(x)
list1d.remove("elem to remove")# Removes the first occurrence of element x from the list.

#.pop(i)
list1d.pop(1)# Removes the element at the given index i and returns it.
list1d.pop() #If no index is specified, pop() removes and returns the last element in the list.

#.clear()
list1d.clear()# Removes all elements from the list.

#.index(x, start, end)
list1d.index("elem")# Returns the index of the first occurrence of element x 
list1d.index("elem",2,5)#(optional start and end indices can be specified).

#.count(x)
list1d.count("elem")# Returns the number of occurrences of element x in the list.

#.sort(key=None, reverse=False)
list1d.sort()# Sorts the list in ascending order. 
list1d.sort(key=len)#Optionally, you can provide a key function call for custom sorting
list1d.sort(reverse=True)#set reverse to True for descending order.

#.reverse()
list1d.reverse()# Reverses the elements of the list in place.

#.copy()
list1d.copy()# Returns a shallow copy (reference location) of the list.
#===============================================================================================================================#
'> List Slicing and Concatenation'

#slicing returns a part of the original list
#list[start_index:stop_index:step] 
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(list1d[0:]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(list1d[:3]) #['a', 'b', 'c']
print(list1d[0:5]) #[0,1,2,3,4]
print(list1d[:6:3])#['a', 'd']
print(list1d[1:6:2]) #[1, 3, 5]
print(list1d[::2]) # ['a', 'c', 'e', 'g', 'i']
#note the stop_index is not included in the slice

list1d_1= [0,1,2,3,4,5,6,7,8,9]
#assignment to slices
list1d_1[2:5] = ['a','b','c'] #[0, 1, 'a', 'b', 'c', 5, 6, 7, 8, 9]
print(list1d_1)

#lists can be concatenated
list1d_2 = [11,12,13,14,15,16,17,18,19]
print(list1d_1 + list1d_2) 
#[0, 1, 'a', 'b', 'c', 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]


#===============================================================================================================================#
'> Lists of Lists: Nested Lists'

#a 2D list is a list of lists
#index   [[---------list 0--------],[--------list 1---------],[--------list 2---------],[--------list 3---------]]
#reverse [[---------list -4-------],[--------list-3---------],[--------list -2--------],[--------list -1--------]]
list2d = [["a","b","c","d","e","f"],["g","h","i","j","k","l"],["m","n","o","p","q","r"],["s","t","u","v","w","x"]]
#index   [[ 0   1   2   3   4   5 ],[ 0   1   2   3   4   5 ],[ 0   1   2   3   4   5 ],[ 0   1   2   3   4   5 ]]
#reverse [[-6  -5  -4  -3  -2  -1 ],[-6  -5  -4  -3  -2  -1 ],[-6  -5  -4  -3  -2  -1 ],[-6  -5  -4  -3  -2  -1 ]]               
# list2d is a list of 4 lists


#simplify by formatting the code this way 
list2d = [
  ["a","b","c","d","e","f"], #list 0
  ["g","h","i","j","k","l"], #list 1
  ["m","n","o","p","q","r"], #list 2
  ["s","t","u","v","w","x"]  #list 3
]


#simplify in our mind as rows and columns 
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes


#access elements (use the list name and [row][col] to access an element)
#list[row][col]
list2d[0][0] # a
list2d[0][1] # b
list2d[3][5] # z

#changing element (use the list name and [row][col] to access an element then = new value)
list2d[0][0] = "aa"
#[["aa","b","c","d","e","f"],["g","h","i","j","k","l"],["m","n","o","p","q","r"],["s","t","u","v","w","x"]]
#   ^
list2d[3][5] = "xx"
#[["aa","b","c","d","e","f"],["g","h","i","j","k","l"],["m","n","o","p","q","r"],["s","t","u","v","w","xx"]]
#-->                                                                                                   ^

#len()function call returns the number of elements in the list
len(list2d)   # 4 (number of rows/lists)
len(list2d)-1 # 3 (last row index)


row = 0 #represents the row, in this case the row at index 0 
len(list2d[row])   # 6 number of columns/elements in a given row/list
len(list2d[row])-1 # 5 last column index 


#===============================================================================================================================#
'> Unpacking Lists'
'''
 refers to the process of extracting individual elements 
 from a container (such as a list, tuple, dictionary)
'''
# Unpacking with Asterisk (*)
# Unpacking into variables
list1d = [1,2,3]
a, b, c = list1d
#a = 1
#b = 2
#c = 3

list1d = [1,2,3]
a, b = list1d
#ValueError: too many values to unpack (expected 2)

# collects multiple values into a single variable
list1d = ["a","b","c","d"]
first, *rest = list1d
#first = a
#rest = [b,c,d]

*start, last = list1d
#start = [a,b,c]
#last = d

#Ignoring values with (_)
list1d = [1,2,3]
_, b, _ = list1d
#b = 2

#Unpack iterable types using *
l1 = [1,2,3]
l2 = [4,5,6]
print( [*l1,*l2] )# [1,2,3,4,5,6]

#===============================================================================================================================#
'> List comprehensions'
# A list comprehension is a shorthand way to algorithmically create a list

'1D list comprehension'
#syntax: [element_value for _ in range()]
list1d = [0 for _ in range(5)] #[0,0,0,0,0]

#syntax: [operation for _ in range()]
x = 2
list1d = [ x**2 for _ in range(5)] #[4,4,4,4,4]

#syntax: [function_call for _ in range()]
import random
list1d = [ random.randint(0,100) for _ in range(5)]


'2D list comprehension'

#[[element_value for _ in range()] for _ in range()]
list2d = [[0 for _ in range(5)] for _ in range(5)] #[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

#[[operation for _ in range()] for _ in range()]
list2d = [[x**2 for _ in range(5)] for _ in range(5)] #[[4,4,4,4,4],[4,4,4,4,4],[4,4,4,4,4],[4,4,4,4,4],[4,4,4,4,4]]

#[[function_call for _ in range()] for _ in range()]
list2d = [[random.randint(0,100) for _ in range(5)] for _ in range(5)]
#===============================================================================================================================#
'> Looping through Lists'

alphanumeric = [chr(x) for x in range(48,58)] + [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)]
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
 'y', 'z']

#for index in range(len(list)):
for i in range(len(alphanumeric)):
  print(i) #prints each index of alphanumeric


# for element in list:
for char in alphanumeric:
  print(char) #prints each element of alphanumberic


#for element in reversed(list):
for elem in reversed(alphanumeric):
  print(elem)
#prints each element of the reversed list



#for index, element in enumerate(list):
for index,element in enumerate(alphanumeric):
  alphanumeric[index] = (index, element)

#the ouput list is below storing a tuple of (index, element) of the original list
[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), 
 (10, 'A'), (11, 'B'), (12, 'C'), (13, 'D'), (14, 'E'), (15, 'F'), (16, 'G'), (17, 'H'), (18, 'I'), (19, 'J'), 
 (20, 'K'), (21, 'L'), (22, 'M'), (23, 'N'), (24, 'O'), (25, 'P'), (26, 'Q'), (27, 'R'), (28, 'S'), (29, 'T'), 
 (30, 'U'), (31, 'V'), (32, 'W'), (33, 'X'), (34, 'Y'), (35, 'Z'), (36, 'a'), (37, 'b'), (38, 'c'), (39, 'd'), 
 (40, 'e'), (41, 'f'), (42, 'g'), (43, 'h'), (44, 'i'), (45, 'j'), (46, 'k'), (47, 'l'), (48, 'm'), (49, 'n'), 
 (50, 'o'), (51, 'p'), (52, 'q'), (53, 'r'), (54, 's'), (55, 't'), (56, 'u'), (57, 'v'), (58, 'w'), (59, 'x'), 
 (60, 'y'), (61, 'z')]


num = [x for x in range(1,27)]
upper_alpha = [chr(x) for x in range(65,91)] 
lower_alpha = [chr(x) for x in range(97,123)]

alphabet = []

#for item1, item2,... in zip(iter1,iter2,...)
for number, upper, lower in zip(num, upper_alpha, lower_alpha):
  alphabet.append((number,upper,lower))

[(1, 'A', 'a'), (2, 'B', 'b'), (3, 'C', 'c'), (4, 'D', 'd'), (5, 'E', 'e'), (6, 'F', 'f'), 
 (7, 'G', 'g'), (8, 'H', 'h'), (9, 'I', 'i'), (10, 'J', 'j'), (11, 'K', 'k'), (12, 'L', 'l'), 
 (13, 'M', 'm'), (14, 'N', 'n'), (15, 'O', 'o'), (16, 'P', 'p'), (17, 'Q', 'q'), (18, 'R', 'r'), 
 (19, 'S', 's'), (20, 'T', 't'), (21, 'U', 'u'), (22, 'V', 'v'), (23, 'W', 'w'), (24, 'X', 'x'), 
 (25, 'Y', 'y'), (26, 'Z', 'z')]

#===============================================================================================================================#