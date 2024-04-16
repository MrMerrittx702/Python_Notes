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

#===============================================================================================================================#
'> Defining a list'
'   > A list is an ordered mutable collection of data, with multiple comma seperated values.'
'   > ordered meaning it has a specific order 0,1,2,... (ie indexed)'
'   > mutable meaning its value can change'


["a","b","c","d","e"] #list (contains multiple items called elements or members)
# 0   1   2   3   4   #indexes (are used to access each element)
# length = 5          #The length is the total number of elements

# List indexes always start at 0 
#In this example:
#   a,b,c,d,e are elements
#   0,1,2,3,4 are indexes
#   length = 5

'''
There are four collection data types in the Python programming language:

> List: 
collection which is ordered and mutable. Allows duplicate members.

> Tuple: 
collection which is ordered and immutable. Allows duplicate members.

> Set: 
collection which is unordered, unchangeable*, and unindexed. No duplicate members.

> Dictionary: 
collection which is ordered** and changeable. No duplicate members.
'''

#===============================================================================================================================#
'> Creating a List'
'   > use [] to denote a list'
'   > seperate elements of a list with commas'
'   > The list() constructor builds a list'

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
'> Converting from Tuples and Sets'
'   > The list() constructor builds a list'
'   > The tuple() constructor builds a tuple'
'   > The set() constructor builds a set'

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
'   > in : checks membership'
'   > not in: checks membership'
'   > + : concatenates two lists'
'   > += : concatenates and assigns'
'   > * : duplicates a list'
'   > *= : duplicates and assigns'

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

#Check Membership (in/not in)
"a" in alpha    #True
"1" in numerals #True

"a" not in alpha    #False
"1" not in numerals #False

#Concatenation (+)
numerals + alpha
#result
['0', '1', '2', '3', '4', '5', 
 '6', '7', '8', '9', 'a', 'b', 
 'c', 'd', 'e', 'f', 'g', 'h', 
 'i', 'j', 'k', 'l', 'm', 'n', 
 'o', 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 'z']

#Concatenation and assign (+=)
a = [1,2,3,4]
a += [5,6,7,8]
a += [9,10,11,12]
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#Duplication (*)
numerals * 3
#result
['0', '1', '2', '3', '4', 
 '5', '6', '7', '8', '9', 
 '0', '1', '2', '3', '4', 
 '5', '6', '7', '8', '9', 
 '0', '1', '2', '3', '4', 
 '5', '6', '7', '8', '9']

#Duplicate and assign (*=)
b =[1,0]
b *= 5
print(b) #[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

#===============================================================================================================================#
'> Accessing Data'
'   > Access elements of a list with their index and subscripting []'
'   > syntax --> list[index]'

list1d = ["a","b","c","d","e","f","g","h","i","j","k","l"]
#index     0   1   2   3   4   5   6   7   8   9   10  11
#reverse  -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1
# elements in a list are accessed by their index

# Access elements using their index and subscripting 
# syntax --> list[index]
# Starting from the front end
list1d[0] #a
list1d[5] #f
list1d[10] #k

# Starting from the back end (Reverse indexing)
list1d[-1] #l
list1d[-5] #h
list1d[-10] #c

#===============================================================================================================================#
'> Changing Data'
'   > change data by reassigning an element using its index and subscripting []'
'   > syntax --> list[index] = new_value'

#        [------------------elements---------------------]
list1d = ["a","b","c","d","e","f","g","h","i","j","k","l"]
#index   [ 0   1   2   3   4   5   6   7   8   9   10  11]
#reverse [-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1]
# elements in a list are changed by assigning a new value to its index

# Change data by assigning a new value to an index using subscripting [].
# Starting from the front end
list1d[0] = "z" 
list1d[5] = "y" 
list1d[10] = "x" 

# Starting from the back end (Reverse indexing)
list1d[-1] = "m"
list1d[-5] = "n"
list1d[-10] = "o"

# Here is the new list:
list1d = ["z","b","o","d","e","y","g","n","i","j","x","m"]
#index   [ 0   1   2   3   4   5   6   7   8   9   10  11]
#reverse [-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1]

#===============================================================================================================================#
'> Built-in list function calls'
'''
Functions are blocks of reusable code, that perform a specific task
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
'   > slicing returns a part of the original list'
'   > use slicing notation to return a sublist'
'   > syntax --> list[start_index:stop_index:step]'
'   > Default start_index is 0'
'   > Default stop_index is len(list) (end of the list)'
'   > Default step is 1'
'   > The slice includes the start_index, but excludes the stop_index'
'   > Assign to a slice of a list using slice notation'
'   > syntax --> list[start_index:stop_index:step] = [new list values]'

#slicing returns a part of the original list
#list[start_index:stop_index:step] 
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#If a stop_index is not provided the default is len(list)
print(list1d[0:]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#If a start_index is not provided the default is 0
print(list1d[:3]) #['a', 'b', 'c']
print(list1d[0:5]) #[0,1,2,3,4]
print(list1d[:6:3])#['a', 'd']
print(list1d[1:6:2]) #[1, 3, 5]

print(list1d[::2]) # ['a', 'c', 'e', 'g', 'i']
#note the stop_index is not included in the slice


list1d_1= [0,1,2,3,4,5,6,7,8,9]

#Assign to a list slice with slice notation
list1d_1[2:5] = ['a','b','c'] #[0, 1, 'a', 'b', 'c', 5, 6, 7, 8, 9]
print(list1d_1)



#===============================================================================================================================#
'> Lists of Lists: Nested Lists'
'   > a 2D list is a list that contains other lists.'
'   > called a nested list or multidimensional list'
'   > Access values with 2 indexes and subscripting [][]'

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
'   > A list comprehension is a shorthand way to algorithmically create a list'

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

#result
[(1, 'A', 'a'), (2, 'B', 'b'), (3, 'C', 'c'), (4, 'D', 'd'), (5, 'E', 'e'), (6, 'F', 'f'), 
 (7, 'G', 'g'), (8, 'H', 'h'), (9, 'I', 'i'), (10, 'J', 'j'), (11, 'K', 'k'), (12, 'L', 'l'), 
 (13, 'M', 'm'), (14, 'N', 'n'), (15, 'O', 'o'), (16, 'P', 'p'), (17, 'Q', 'q'), (18, 'R', 'r'), 
 (19, 'S', 's'), (20, 'T', 't'), (21, 'U', 'u'), (22, 'V', 'v'), (23, 'W', 'w'), (24, 'X', 'x'), 
 (25, 'Y', 'y'), (26, 'Z', 'z')]

#===============================================================================================================================#
'''
Vocabulary:

Argument
Ascending
Collection
Comprehension
Concatenation
Constructor
Descending
Duplication
Element
Function
Function Call
Function Definition
Index
Iterable
Iteration
Iterator
List
Member
Membership
Mutable
Parameter
Return
Reverse Index
Slicing
Unpacking


Argument:
An argument is a value passed to a function or method when it is called. 
It provides input or data for the function's operation, allowing the function to perform its task with specific values or parameters.

Ascending:
Ascending refers to an arrangement of elements in increasing order. 
It is commonly used when sorting data or arranging items based on their values or properties from lowest to highest.

Collection:
A collection is a group of related elements or items stored and manipulated together as a single unit. 
It can include various data structures such as lists, sets, dictionaries, arrays, and tuples.

Comprehension:
Comprehension refers to the concise and expressive way of creating new collections (such as lists, sets, or dictionaries) by iterating over existing ones and applying conditions or transformations to the elements.

Concatenation:
Concatenation is the process of combining two or more strings, sequences, or data structures into a single entity. 
In the context of strings, concatenation involves joining the characters of one string to the end of another string.

Constructor:
A constructor is a special type of method used for initializing objects of a class. 
It is automatically called when a new instance of the class is created, allowing for the setup of initial values or configurations.

Descending:
Descending refers to an arrangement of elements in decreasing order. 
It is the opposite of ascending and is used when sorting data or arranging items based on their values or properties from highest to lowest.

Duplication:
Duplication is the process of creating a copy or duplicate of an existing object, data structure, or value. 
It allows for the replication of data, enabling multiple references or independent modifications.

Element:
An element is a single item or component within a collection or sequence. 
It can refer to individual values in a list, set, tuple, or other data structure.

Function:
A function is a self-contained block of code that performs a specific task or operation. 
It can accept input arguments, perform computations, and return results, providing modularity and reusability in the code.

Function Call:
A function call is an instruction that invokes a specific function with provided arguments. 
It triggers the execution of the function's code, and upon completion, the function may return a result or perform other actions as defined.

Function Definition:
A function definition is the implementation of a function, including its name, parameters, and code block. 
It specifies the behavior of the function and defines how it operates when called with specific arguments.

Index:
An index is a numeric value used to identify the position of an element within a collection or sequence. 
It typically starts from zero for the first element and increments by one for each subsequent element.

Iterable:
An iterable is an object that can be iterated over, allowing its elements to be accessed sequentially. 
It includes data structures like lists, tuples, sets, dictionaries, and strings, as well as custom iterable objects.

Iteration:
Iteration is the process of repeatedly executing a set of instructions or operations, typically over a sequence of elements. 
It involves iterating or traversing through the elements of a collection one by one.

Iterator:
An iterator is an object used to traverse or iterate over the elements of a collection. 
It maintains state information about the current position within the collection and provides methods for accessing the next element.

List:
A list is a mutable, ordered collection of elements or items. It allows for the storage and manipulation of data in a sequential manner, with elements accessed by their index.

Member:
A member is an element or part belonging to a group, class, or collection. 
In programming, it commonly signifies variables, functions, or other entities associated with a class, module, or data structure.

Membership:
Membership refers to the inclusion of an element within a collection or sequence. 
It involves testing whether a value is contained in a data structure, such as a list, set, tuple, or dictionary.

Mutable:
Mutable refers to an object or value that can be modified or changed after its creation. 
Mutable objects allow for in-place modifications, such as adding or removing elements from a list.

Parameter:
A parameter is a variable or placeholder in a function or method definition that is used to receive input when the function or method is called. 
Parameters define the interface of the function and specify the types and order of arguments it expects.

Return:
Return is a keyword used in functions to specify the value that the function should produce or output when called. 
It allows functions to send back results or data to the caller for further use or processing.

Reverse Index:
A reverse index is a numeric value used to identify the position of an element within a collection, counting backward from the end of the collection. 
It provides a convenient way to access elements from the end of the collection.

Slicing:
Slicing is a technique used to extract a portion or subsequence of elements from a collection or sequence. 
It allows for the creation of new collections containing specific ranges of elements from the original sequence.

Unpacking:
Unpacking is the process of extracting individual elements from a collection or sequence and assigning them to separate variables. 
It enables the decomposition of data structures like tuples or lists into their constituent parts.
'''