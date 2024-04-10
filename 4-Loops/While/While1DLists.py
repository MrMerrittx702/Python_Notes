#===============================================================================================================================#
'''1D List Iteration: While Loops'''
#===============================================================================================================================#
'''
Covered in this file:
> Lists Review
> List Iteration: While Loop Setup
> Forward Iteration: Beginning to End
> Backward Iteration: End to Beginning
> Calculating the Middle Index
> Halves Iteration: Beginning to Middle
> Halves Iteration: Middle to Beginning
> Halves Iteration: Middle to End
> Halves Iteration: End to Middle
'''

#===============================================================================================================================#
'Lists Review'

#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] #declare and initialize
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#length aka number of elements = 9 

#access an element 
list1d[0] # a
list1d[4] # e
list1d[8] # i
list1d[9] # IndexError: list index out of range


#change and element
list1d[0] = "x"
list1d[4] = "y"
list1d[8] = "z"
#['x', 'b', 'c', 'd', 'y', 'f', 'g', 'h', 'z']
#  ^                   ^                   ^

#slicing
#list[start_index:stop_index:step] 
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(list1d[0:]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(list1d[:3]) #['a', 'b', 'c']
print(list1d[0:5]) #['a', 'b', 'c', 'd', 'e']
print(list1d[:6:3])
print(list1d[1:6:2]) #['b', 'd', 'f']
#note the stop_index is not included in the slice

#get length
number_of_elements = len(list1d) # 9
last_index = len(list1d)-1 # 8

#methods
list1d.append()  # Adds a single element x to the end of the list.
list1d.extend()  # Extends the list by appending elements from the iterable.
list1d.insert()  # Inserts an element x at a given index i.
list1d.remove()  # Removes the first occurrence of element x from the list.
list1d.pop()     # Removes the element at the given index i and returns it. default is the last element
list1d.clear()   # Removes all elements from the list.
list1d.index()   # Returns the index of the first occurrence of element x 
list1d.count()   # Returns the number of occurrences of element x in the list.
list1d.sort()    # Sorts the list in ascending order. 
list1d.reverse() # Reverses the elements of the list in place.
list1d.copy()    # Returns a shallow copy (reference location) of the list.

#===============================================================================================================================#
'List Iteration: While Loop Setup'

start_index = 0; list_length=0; step=1

#use index or i instead of count 
index = start_index #start (starting index in python is 0)

while index < list_length :#stop (stop at the end of the list)
    #indent 4 spaces for code in the block
    #--------------------------#
    #code block to execute here#
    #--------------------------#
    index += step  #step (usually by 1)
#unindent to leave the block

#===============================================================================================================================#
'Forward Iteration: Beginning to End'
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] #declare and initialize
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#length aka number of elements = 9 

index = 0 #start at first index

while index < len(list1d): # or <= len(list1d)-1  stop at last index 
    
    print(index, end = " ") # prints index
    print(list1d[index], end = " ") #prints element
    
    index += 1 # increment by 1

#end =" " is just for formatting the output
#===============================================================================================================================#
'Backward Iteration: End to Beginning'
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] #declare and initialize
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#length aka number of elements = 9 

index = len(list1d)-1 #start at last index

while index >= 0: # or > -1 # stop at first index

  print(index, end = " ") # prints index
  print(list1d[index], end = " ") #prints element

  index -= 1 # decrement by 1

#end =" " is just for formatting the output
#===============================================================================================================================#
'Calculating the Middle Index'

'Even Length Lists'
#        [-----------------elements-------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] #declare and initialize
#index   [ 0    1    2    3    4    5    6    7 ]
#reverse [-8   -7   -6   -5   -4   -3   -2   -1 ]
#length aka number of elements = 8

#              Is the middle index 3 or 4?
#Calculating the middle index
# list length divided by 2 equals the mid_index
middle_index = len(list1d)/2 # 4

#Note: this does not work for odd numbered lists.

'Odd Length Lists'
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] #declare and initialize
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#length aka number of elements = 9 

#                    Middle index is clearly 4

#Calculating the middle index
# list length divided by 2 equals the mid_index
len(list1d)/2 # 4.5 <-- Floats cannot be indexes

#Floor division //
middle_index = len(list1d//2)# // Truncates 4.5 to 4
#OR
#Casting int()
middle_index = int(len(list1d)/2) #Truncates 4.5 to 4

'''
In odd length lists this calculation results in 
  the second half being 1 element more than the first half

The two methods above work for both even and odd length lists
'''



#===============================================================================================================================#
'Front Half Iteration: Beginning to Middle'
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] #declare and initialize
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#length aka number of elements = 9 

index =  0 #start at first index

while index < len(list1d)//2: #or <= (len(list1d)//2)-1 #stop at middle index

    print(index, end = " ") # prints index
    print(list1d[index], end = " ") #prints element

    index += 1 # increment by 1

#end =" " is just for formatting the output
#===============================================================================================================================#
'Front Half Iteration: Middle to Beginning'
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] #declare and initialize
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#length aka number of elements = 9 

index = (len(list1d)//2)-1 # start at middle index

while index >= 0: #or > -1 #stop at first index

    print(index, end = " ") # prints index
    print(list1d[index], end = " ") #prints element

    index -= 1 # decrement by 1

#end =" " is just for formatting the output
#===============================================================================================================================#
'Back Half Iteration: Middle to End'
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] #declare and initialize
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#length aka number of elements = 9 


index = len(list1d)//2 #start at middle index

while index < len(list1d):# or <= len(list1d)-1 #stop at last index

    print(index, end = " ") # prints index
    print(list1d[index], end = " ") #prints element

    index += 1 # increment by 1

#end =" " is just for formatting the output
#===============================================================================================================================#
'Front Half Iteration: End to Middle'
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] #declare and initialize
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#length aka number of elements = 9 

index = len(list1d)-1 #start at last index

while index >= len(list1d)//2: #or > (len(list1d)//2)-1 stop at middle index

    print(index, end = " ") # prints index
    print(list1d[index], end = " ") #prints element

    index -= 1 # decrement by 1

#end =" " is just for formatting the output
#===============================================================================================================================#









