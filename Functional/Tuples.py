'''Tuples'''

'''
tuples are immutable, and ordered
'''

#index 0 1 2
tup = (1,2,3) #called packing a tuple

#Worked with like lists
#Convert from tuple to list to change
list1d = list(tup)

#Convert back 
tup = tuple(list1d)

#add tuple to a tuple

'''
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

#unpacking a tuple
numbers = (1,2,3)
(one,two,three) = numbers

#Using Asterisk * adds remaining values as a list
numbers = (1,2,3,4,5,6,7,8)
(a,b,*c) = numbers
print(c)#[3, 4, 5, 6, 7, 8]

#Use * to multiply the contents of a tuple
numbers = (1,2)
num_tup = numbers * 5
print(num_tup)#(1, 2, 1, 2, 1, 2, 1, 2, 1, 2)

#two built in tuple methods

count_tup = (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
tally = count_tup.count(1) #returns the number of times a value occurs in a tuple
print(tally)# 5

index_tup = (1,2,3,4,5,6,7,8)
index = index_tup.index(4) #searches the tuple for a specified value and returns the index it was found at. 
print(index)# 3