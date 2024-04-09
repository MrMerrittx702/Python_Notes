#===============================================================================================================================#
'''Python Sets'''
#===============================================================================================================================#

'''
  Covered in this video:
  > Sets Defined
  > Creating a Set 
  > Converting from Lists and Tuples
  > Set Operations
  > Built-in set methods calls
  > Looping through sets

'''

#===============================================================================================================================#
'> Sets Defined'

'''
Sets are collections that are a unordered, unchangeable, unindexed, and do not allow duplicate values
  
  unordered meaning elements are in no particular order
  unchangeable (not immutable) meaning values cannot be changed
    items can be added and removed only
  unindexed meaning elements do not have an order
  no duplicate values
  values must be hashable (cannot store mutable types)

  Hashable means that the value must remain constant such that 
    when passing the value to a hash function it returns an identical hash value
'''

#a set uses curly braces {}
{1,2,3,4,5}

'''
There are four collection data types in the Python programming language:

List is a collection which is ordered and mutable. Allows duplicate members.
Tuple is a collection which is ordered and immutable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

#===============================================================================================================================#
'> Creating a Set'

#declare      initialize
set1d = {1,2,3,4,5,6,7,8,9}

#To create and empty set you must use set() using {} creates a dictionary
empty = set()

#===============================================================================================================================#
'> Converting from Lists and Tuples'

list1d = ["a","b","c"]
tuple1d = (1,2,3)

#From list or tuple to set use set()
set1d = set(list1d)
set1d = set(tuple1d)

#From set to list use list()
list1d = list(set1d)

#From set to tuple use tuple()
tuple1d = tuple(set1d)

#===============================================================================================================================#
'> Set Operations'
#multi variable assignment with Sets
a, b, c = {1,2,3}
#a = 1 b = 2 c = 3
# Note that sets are unordered collections, 
# so the order of assignment is not guaranteed 
# to be the same as the order in the set literal.


set_1 = {1,2,3,4,5,6}
set_2 = {7,8,9,0}
set_3 = {4,5,6,7,8}

#Checking Membership (checking if an element exists in the set)
#Use the in keyword
3 in set_1 # True
3 in set_2 # False

# Union (joining a set with another iterable)
set_1 | set_2 #{1,2,3,4,5,6,7,8,9,0}
set_2 | set_3 #{9,0,4,5,6}
#creates a new set of all unique elements from both sets


#Intersection (&)(keep only duplicates)
set_1 & set_3 #{4,5,6}
set_2 & set_3 #{7,8}

#Difference (-) (keep all items from the first set not present in the second)
set_1 - set_3 #{1,2,3}
set_2 - set_3 #{9,0}


#Symmetric Difference (^) (keep all but the duplicates)
set_1 - set_3 #{1,2,3,7,8}
set_2 - set_3 #{4,5,6,9,0}

#===============================================================================================================================#
'> Built-in set methods calls'
'''
  Methods are functions defined by a class
    Methods are typically called using an object or class and dot (.) syntax
      object.method(parameters) --> for methods which require objects
        or
      class.method(paramters) --> for methods which do not require objects
'''

#To see what methods you can call on an object use dir(object)
#To see more information on a specific method use help(object.method)

set1d = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

# set1d.add(element) adds an element to the set.
set1d.add(10)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# set1d.clear() removes all elements from the set.
set1d.clear()  # {}

# set1d.copy() returns a shallow copy of the set.
set1d = {1, 2, 3}
set1d.copy()  # {1, 2, 3}

# set1d.difference(*others) returns the difference between the set and another set or sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diff = set1.difference(set2)  # {1, 2}

# set1d.difference_update(*others) removes all elements of another set from this set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.difference_update(set2)  # {1, 2}

# set1d.discard(element) removes an element from the set if it is a member.
set1d = {1, 2, 3}
set1d.discard(2)  # {1, 3}

# set1d.intersection(*others) returns the intersection of the set with another set or sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection(set2)  # {2, 3}

# set1d.intersection_update(*others) updates the set with the intersection of itself and another set or sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)  # set1 is now {2, 3}

# set1d.isdisjoint(other) returns True if the set has no elements in common with another set.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set1.isdisjoint(set2)  # True

# set1d.issubset(other) returns True if every element of the set is in another set.
set1 = {1, 2}
set2 = {1, 2, 3, 4}
set1.issubset(set2)  # True

# set1d.issuperset(other) returns True if every element of another set is in the set.
set1 = {1, 2, 3, 4}
set2 = {1, 2}
set1.issuperset(set2)  # True

# set1d.pop() removes and returns an arbitrary element from the set.
set1 = {1, 2, 3}
set1.pop()  # e.g., 1

# set1d.remove(element) removes an element from the set. If the element is not a member, it raises a KeyError.
set1 = {1, 2, 3}
set1.remove(2)  # {1, 3}

# set1d.symmetric_difference(other) returns the symmetric difference of the set with another set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference(set2)  # {1, 2, 5, 6}

# set1d.symmetric_difference_update(other) updates the set with the symmetric difference of itself and another set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)  # set1 is now {1, 2, 5, 6}

# set1d.union(*others) returns the union of the set with another set or sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.union(set2)  # {1, 2, 3, 4, 5}

# set1d.update(*others) updates the set with the union of itself and another set or sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)  # set1 is now {1, 2, 3, 4, 5}

#del keyword removes the set completely
del set1d

#===============================================================================================================================#
'> Set Comprehension'
# A set comprehension is a shorthand way to algorithmically create a set

#syntax: {element_value for _ in range()}
set1d = {0 for _ in range(5)} #{0,0,0,0,0}

#syntax: {operation for _ in range()}
x = 2
set1d = { x**2 for _ in range(5)} #{4,4,4,4,4}

#syntax: {function_call for _ in range()}
import random
set1d = { random.randint(0,100) for _ in range(5)}

#===============================================================================================================================#
'> Looping through sets'

'''
Sets are unordered and unindexed
  unordered meaning elements are in no particular order
  unindexed meaning elements do not have an order
  no duplicate values 
'''

#This means that looping through the values will occur in a random order
#running the code below 5 times results in a different list each time.

set1d = {"a","b","c","d","e"}
list1d = []
for elem in set1d:
  list1d.append(elem)
print(list1d)

# 1 ['a', 'c', 'e', 'd', 'b']
# 2 ['a', 'd', 'c', 'b', 'e']
# 3 ['a', 'c', 'e', 'b', 'd']
# 4 ['a', 'c', 'd', 'b', 'e']
# 5 ['b', 'c', 'd', 'e', 'a']











