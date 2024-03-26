#===============================================================================================================================#
'''While loop 2d lists'''
#===============================================================================================================================#
'''
Covered in this file:
> 2D Lists Review
> 2D List Iteration: While Loop Setup
> Forward Iteration: Beginning to End
> Backward Iteration: End to Beginning
> Other Iterations

'''
#===============================================================================================================================#
'> 2D Lists Review'

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
'> 2D List Iteration: While Loop Setup'

'''
Use nested while loops to iterate
  2 Loops 1 inside the other
  > Outer Loops through rows/lists
  > Inner Loops through columns/items

'''

#Outer loop
row = 0 #start at the first list 
while( row < len(list2d) ): #OR row <= len(list2d)-1 ; stop at last list
  ...
  row += 1 #increment by 1
#exit outer while

#Inner Loop
col = 0 #start at first item
while( col < len(list2d[row]) ): #OR col <= len(list2d[row])-1 ; stop at last item
  ...
  col += 1 #increment by 1
#exit inner loop

'The inner loop goes inside of the outer loop'
#Outer loop---------------------------------------#
row = 0                                           #
while( row < len(list2d) ):                       #
                                                  #
  #Inner Loop-------------------------#           #
  col = 0 #start at first item        #           #
  while( col < len(list2d[row]) ):    #           #
    ...                               #           #
    col += 1                          #           #
  #exit inner loop--------------------#           #
                                                  #
  row += 1                                        # 
#exit outer while---------------------------------#



#===============================================================================================================================#
'> Forward Iteration: Beginning to End'

row = 0 #start at the first list index
while row < len(list2d): # or <= len(list2d)-1

  col = 0 #start at the first element index
  while col < len(list2d[row]): # or <= len(list2d[row])-1
    
    print(row, col, end = "|") #printing indexes
    print(list2d[row][col], end = ", ") #printing elements

    col += 1 #increment by 1

  row += 1 #increment by 1

#end =" " is just for formatting the output
#===============================================================================================================================#
'> Backward Iteration: End to Beginning'

row = len(list2d) - 1 #start at the last list index
while row >= 0: # or > -1 #stop at the first list index

  col = len(list2d[row]) - 1 #start at the last element index
  while col >= 0: # or > -1 #stop at the first element index
    
    print(row, col, end = "|") #printing indexes
    print(list2d[row][col], end = ", ") #printing elements

    col -= 1 #decrement by 1

  row -= 1 #decrement by 1



#end =" " is just for formatting the output
#===============================================================================================================================#
'> Other Iterations'


'''
  >Using a conditional to check the elements.
  >Using a conditional and changing values.
  >Serpentine Loop pattern
'''


#Count the number of times the number 5 appears (90 times)
#list2d[100][10] --> 1000 total elements
list2d = [[4, 2, 7, 2, 7, 2, 6, 5, 6, 6], [7, 7, 8, 5, 8, 1, 3, 7, 6, 5], [5, 1, 3, 8, 8, 0, 6, 3, 6, 6], [5, 8, 6, 0, 4, 4, 9, 9, 6, 8], [4, 8, 3, 1, 7, 9, 3, 4, 7, 1], [4, 7, 4, 7, 7, 1, 7, 4, 7, 4], [6, 0, 6, 1, 2, 7, 8, 1, 7, 5], [9, 3, 6, 1, 4, 2, 0, 1, 3, 1], [8, 2, 5, 1, 1, 2, 6, 2, 0, 2], [2, 8, 7, 0, 6, 0, 7, 5, 3, 4], [2, 3, 8, 0, 8, 9, 8, 2, 5, 0], [8, 2, 9, 5, 4, 5, 2, 5, 3, 8], [8, 3, 7, 2, 3, 7, 3, 4, 9, 4], [6, 6, 7, 2, 3, 2, 6, 1, 5, 7], [0, 0, 3, 7, 5, 6, 9, 9, 9, 8], [6, 7, 8, 0, 4, 1, 0, 0, 3, 7], [8, 4, 4, 2, 4, 2, 4, 4, 1, 0], [9, 0, 1, 1, 2, 3, 3, 6, 9, 4], [6, 7, 2, 3, 9, 3, 1, 4, 1, 5], [7, 3, 6, 5, 3, 7, 6, 1, 6, 3], [1, 5, 7, 4, 7, 6, 
6, 2, 9, 9], [1, 7, 0, 6, 8, 0, 0, 4, 8, 2], [0, 1, 5, 3, 0, 4, 6, 6, 0, 9], [5, 6, 8, 7, 1, 5, 9, 1, 9, 2], [1, 4, 1, 0, 7, 2, 6, 1, 3, 4], [8, 8, 9, 7, 4, 6, 0, 6, 7, 6], [6, 5, 7, 6, 1, 3, 5, 6, 4, 7], [9, 2, 1, 7, 1, 9, 5, 4, 3, 7], [2, 2, 9, 8, 7, 4, 0, 0, 1, 8], [8, 0, 1, 0, 8, 1, 8, 4, 8, 4], [2, 0, 8, 0, 9, 1, 8, 7, 9, 8], [6, 2, 8, 0, 1, 9, 0, 1, 3, 9], [1, 1, 7, 0, 1, 5, 5, 1, 2, 2], [9, 6, 0, 0, 2, 4, 7, 1, 1, 6], [5, 5, 6, 7, 6, 8, 7, 1, 4, 3], [3, 2, 6, 7, 2, 8, 3, 0, 2, 6], [2, 2, 6, 0, 7, 9, 9, 9, 3, 6], [8, 7, 6, 1, 2, 3, 6, 1, 4, 2], [9, 1, 4, 9, 0, 8, 7, 7, 3, 0], [1, 8, 5, 6, 2, 5, 7, 1, 5, 4], [4, 8, 6, 9, 0, 6, 8, 9, 7, 4], [9, 6, 
3, 9, 1, 3, 2, 5, 6, 0], [9, 8, 7, 6, 6, 9, 5, 1, 8, 1], [4, 7, 5, 8, 1, 1, 4, 8, 9, 1], [9, 6, 7, 2, 7, 1, 9, 9, 1, 0], [1, 0, 5, 3, 3, 4, 5, 0, 2, 1], [4, 5, 6, 8, 5, 3, 9, 6, 5, 3], [9, 2, 1, 3, 6, 6, 7, 0, 5, 5], [8, 8, 0, 2, 2, 1, 7, 8, 7, 3], [8, 0, 2, 3, 3, 6, 5, 3, 3, 3], [5, 1, 8, 6, 5, 7, 8, 9, 8, 6], [7, 3, 8, 9, 9, 3, 2, 6, 4, 9], [7, 6, 6, 8, 6, 9, 1, 3, 8, 9], [1, 4, 6, 3, 7, 3, 4, 0, 5, 0], [7, 4, 0, 5, 5, 8, 1, 8, 4, 8], [5, 9, 6, 0, 3, 3, 1, 9, 7, 6], [6, 1, 5, 4, 2, 1, 0, 7, 1, 8], [0, 8, 1, 2, 8, 6, 1, 9, 8, 2], [5, 6, 8, 4, 7, 3, 0, 6, 5, 0], [2, 7, 7, 3, 0, 4, 0, 9, 0, 2], [7, 3, 2, 8, 2, 0, 0, 5, 1, 8], [4, 3, 8, 0, 1, 6, 8, 2, 5, 3], [4, 8, 2, 9, 0, 9, 6, 1, 8, 4], [2, 2, 7, 8, 6, 5, 2, 9, 5, 6], [5, 0, 5, 4, 9, 8, 6, 3, 3, 7], [0, 6, 6, 6, 2, 1, 7, 8, 4, 6], [1, 8, 7, 2, 1, 8, 0, 9, 1, 2], [0, 2, 3, 2, 4, 4, 7, 0, 1, 2], [2, 0, 1, 0, 6, 3, 3, 8, 6, 3], [4, 6, 1, 4, 8, 1, 3, 8, 0, 3], [1, 6, 5, 9, 5, 1, 5, 6, 2, 5], [9, 7, 3, 7, 3, 7, 8, 4, 4, 6], [2, 8, 2, 7, 9, 8, 4, 5, 7, 8], [9, 8, 7, 9, 8, 3, 3, 1, 7, 8], [8, 8, 3, 2, 5, 3, 4, 1, 0, 8], [9, 6, 1, 6, 2, 2, 
5, 2, 3, 9], [5, 3, 1, 2, 9, 7, 1, 6, 0, 4], [6, 2, 0, 5, 7, 2, 2, 8, 4, 0], [4, 4, 0, 4, 5, 1, 6, 6, 6, 9], [2, 0, 7, 5, 6, 3, 9, 8, 4, 2], [9, 2, 8, 8, 4, 1, 7, 2, 8, 3], [0, 3, 4, 0, 8, 9, 5, 0, 3, 9], [4, 5, 6, 1, 8, 3, 5, 4, 9, 8], [0, 3, 7, 2, 6, 0, 8, 3, 2, 7], [8, 1, 6, 7, 4, 5, 6, 9, 8, 0], [5, 5, 1, 0, 5, 1, 0, 7, 9, 1], [5, 4, 8, 1, 0, 2, 2, 3, 5, 2], [4, 9, 8, 2, 7, 8, 9, 2, 4, 2], [2, 1, 5, 7, 7, 6, 7, 1, 8, 2], [5, 3, 6, 3, 6, 4, 1, 2, 9, 3], [6, 6, 4, 7, 3, 6, 5, 1, 3, 0], [3, 4, 4, 2, 0, 5, 7, 4, 2, 3], [3, 4, 7, 6, 7, 7, 0, 5, 5, 0], [6, 7, 7, 5, 3, 0, 8, 0, 9, 6], [2, 5, 3, 2, 3, 2, 3, 2, 4, 3], [2, 5, 9, 8, 5, 9, 0, 6, 6, 2], [6, 9, 
9, 4, 8, 6, 5, 0, 2, 0], [5, 1, 4, 2, 8, 6, 2, 7, 9, 5], [0, 6, 4, 9, 4, 4, 3, 0, 0, 7], [3, 0, 2, 8, 9, 9, 4, 3, 5, 8]]

count = 0
row = 0
while row < len(list2d): # or <= len(list2d)-1

  col = 0
  while col < len(list2d[row]): # or <= len(list2d[row])-1
    
    if(5 == list2d[row][col]):
      count += 1
    
    col += 1
  
  row += 1

print(count)

#Convert each 1 to an X and each 0 to a Y
list2d = [[1, 0, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 0, 1, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 1, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 
0, 1, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1, 0, 0, 
1, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 1, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 
0, 1, 1, 0, 0, 1, 0, 1], [1, 1, 0, 0, 0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 1, 0], [1, 1, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 
0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0]]

x_count = 0
y_count = 0
row = 0
while row < len(list2d): # or <= len(list2d)-1

  col = 0
  while col < len(list2d[row]): # or <= len(list2d[row])-1
    
    if(1 == list2d[row][col]):
      x_count += 1
      list2d[row][col] = "X"
    else:
      y_count += 1
      list2d[row][col] = "Y"
    
    col += 1
  
  row += 1

print(list2d)
print(f"X count = {x_count}")    #X count = 295
print(f"Y count = {y_count}")    #Y count = 705
print(x_count + y_count == 1000) #True

[['X', 'Y', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'X', 'Y'], ['X', 'X', 'X', 'X', 'Y', 'X', 'X', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'X', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'Y', 'Y', 'X', 'Y', 'X', 'Y', 'Y', 'X', 'Y'], ['Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y'], ['Y', 'X', 
'Y', 'Y', 'Y', 'X', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'Y', 'Y', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 'Y'], ['Y', 'X', 'X', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'X', 'Y', 'X', 'X', 'Y', 'Y', 'X', 'Y', 'X'], ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'X'], ['Y', 'X', 'Y', 'Y', 'X', 'Y', 'X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'Y', 'X', 'Y', 'Y', 'Y', 'X', 'Y'], ['Y', 'X', 'X', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'X'], ['Y', 'Y', 'Y', 'X', 'X', 'Y', 'X', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y'], ['X', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X', 'Y', 'Y'], ['Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 'X', 'X'], ['Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 
'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X'], ['X', 'Y', 'Y', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X'], ['Y', 'Y', 'Y', 'X', 'Y', 'X', 'Y', 'Y', 'Y', 'X'], ['X', 'Y', 'X', 'X', 'Y', 'Y', 'Y', 'X', 'Y', 'Y'], ['Y', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'X'], ['X', 'X', 'X', 'X', 'X', 'Y', 'Y', 'X', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 'X', 'X'], ['Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'Y'], ['Y', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X', 'Y'], ['Y', 'Y', 'Y', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'Y', 'Y', 'X', 'X', 'Y', 'Y'], ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y'], ['Y', 'X', 'X', 'X', 'Y', 'Y', 'X', 'X', 'X', 'Y'], ['Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'X', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'X', 'Y', 'X'], ['Y', 'Y', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y'], ['X', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y'], ['X', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'X'], ['Y', 'Y', 'X', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y'], ['Y', 'Y', 'X', 'Y', 'X', 'X', 'Y', 'X', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 
'X', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'X', 'X', 'Y'], ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'X'], ['Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X'], ['Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X', 'X', 'X', 'Y'], ['Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'X', 'X', 'X', 'Y', 'Y', 'Y'], ['X', 'X', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X'], ['Y', 'X', 'X', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'X', 'X', 'Y', 'Y', 'X', 'Y', 'X'], ['Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'Y'], ['Y', 'X', 'Y', 'Y', 'X', 'X', 'X', 'Y', 'X', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y'], ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'X'], ['Y', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X'], ['X', 'Y', 'X', 'Y', 'X', 'X', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y'], ['X', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X', 'X', 'X', 'X'], ['X', 'X', 'Y', 'Y', 'X', 'Y', 'X', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'X', 'X', 'Y', 'Y', 'X', 'Y', 'X'], ['X', 'X', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'X'], ['X', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'X', 'Y'], ['X', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 
'Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'X', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'Y', 'X', 'Y'], ['X', 'X', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y'], ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y'], ['X', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X'], ['X', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'X'], ['Y', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y'], ['Y', 'Y', 'X', 'Y', 'Y', 'X', 'Y', 'X', 'X', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'Y', 'Y'], ['X', 'Y', 'Y', 'Y', 'X', 'Y', 'Y', 'Y', 'X', 'Y']]


#Loop in a serpentine pattern
list2d = [ 
  [0, 1, 2, 3, 4], #forward
  [0, 1, 2, 3, 4], #backward
  [0, 1, 2, 3, 4], #forward
  [0, 1, 2, 3, 4], #backward
  [0, 1, 2, 3, 4]  #forward
] 

row = 0
while row < len(list2d): 

  if(0 == row % 2):
    col = 0
    while col < len(list2d[row]): 
      
      print(list2d[row][col],end = ",") 
      
      col += 1
  else:
    col = len(list2d[row])-1
    while col > -1: 
    
      print(list2d[row][col],end = ",") 
     
    
      col -= 1
  print()
  
  row += 1

# 0,1,2,3,4,
# 4,3,2,1,0,
# 0,1,2,3,4,
# 4,3,2,1,0,
# 0,1,2,3,4,















