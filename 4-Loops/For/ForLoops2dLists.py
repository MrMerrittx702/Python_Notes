#===============================================================================================================================#
'''For Loops with 2D Lists'''
#===============================================================================================================================#

'''
Covered in this file:
> 2D Lists Review
> 2D List Iteration: For Loop Setup
> Forward Iteration: Beginning to End
> For Each Loop
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
'> 2D List Iteration: For Loop Setup'
'''
Use nested for loops to iterate
  2 Loops 1 inside the other
  > Outer Loops through rows/lists
  > Inner Loops through columns/items
'''

#Outer Loop 
#start a the first list, stop at the last list, increment by 1
for row in range(0,len(list2d),1):
    ...

#Inner Loop
#start at the first item, stop at  the last item, increment by 1
for col in range(0,len(list2d[row]),1):
    ...


'The inner loop goes inside of the outer loop'
#Outer Loop-------------------------------------------------#
for row in range(0,len(list2d),1):                          #
    #Inner Loop----------------------------------#          #
    for col in range(0,len(list2d[row]),1):      #          #
        ...                                      #          #
    #exit inner loop-----------------------------#          #
#exit outer loop--------------------------------------------#
     
#===============================================================================================================================#
'> Forward Iteration: Beginning to End'

for row in range(0,len(list2d),1): # first row(0) to last row by 1s 

    for col in range(0,len(list2d[row]),1): # first col(0) to last col by 1s

        print(row, col, end = ", ")#printing indexes
        print(list2d[row][col], end = " ") #printing elements

    print()#this line is just for formatting the output


for row in range(len(list2d)): # 0(default) to last row by 1s(default)

    for col in range(len(list2d[row])): # 0(default) to last col by 1s(default)

        print(row, col, end = ", ") # printing indexes
        print(list2d[row][col], end = " |") # printing elements

    print()#this line is just for formatting the output


#no formatting
for row in range(len(list2d)): 

    for col in range(len(list2d[row])): 

        print(row,col) # printing indexes
        print(list2d[row][col]) # printing elements

#===============================================================================================================================#
'> For Each Loop'
#special for loop syntax
'In a For each loop the variable (row or col) represents the element, not the index'

#Note only works forward, and only works for looping through the entire list
for row in list2d:
    for col in row:
        print(col, end = "|")
    print() # this line is just for formatting the output

#no formating
for row in list2d:
    for col in row:
        print(col)

#end = " " is just for formatting the output
#===============================================================================================================================#
'> Backward Iteration: End to Beginning'


for row in range(len(list2d)-1,-1,-1): # last row to first row(0) by 1s

    for col in range(len(list2d[row])-1,-1,-1): # last col to first col(0) by 1s

        print(row, col, end = ", ")#printing indexes
        print(list2d[row][col], end = " |") #printing elements

    print() # this line is just for formatting the output


#no formatting
for row in range(len(list2d)-1,-1,-1):

    for col in range(len(list2d[row])-1,-1,-1): 

        print(row,col)#printing indexes
        print(list2d[row][col]) #printing elements
    

#end = ", " and end = " |" are just for formatting the output
#===============================================================================================================================#
'> Other Iterations'

#Count the number of 7s
list2d = [[4, 2, 7, 2, 7, 2, 6, 5, 6, 6], [7, 7, 8, 5, 8, 1, 3, 7, 6, 5], [5, 1, 3, 8, 8, 0, 6, 3, 6, 6], [5, 8, 6, 0, 4, 4, 9, 9, 6, 8], [4, 8, 3, 1, 7, 9, 3, 4, 7, 1], [4, 7, 4, 7, 7, 1, 7, 4, 7, 4], [6, 0, 6, 1, 2, 7, 8, 1, 7, 5], [9, 3, 6, 1, 4, 2, 0, 1, 3, 1], [8, 2, 5, 1, 1, 2, 6, 2, 0, 2], [2, 8, 7, 0, 6, 0, 7, 5, 3, 4], [2, 3, 8, 0, 8, 9, 8, 2, 5, 0], [8, 2, 9, 5, 4, 5, 2, 5, 3, 8], [8, 3, 7, 2, 3, 7, 3, 4, 9, 4], [6, 6, 7, 2, 3, 2, 6, 1, 5, 7], [0, 0, 3, 7, 5, 6, 9, 9, 9, 8], [6, 7, 8, 0, 4, 1, 0, 0, 3, 7], [8, 4, 4, 2, 4, 2, 4, 4, 1, 0], [9, 0, 1, 1, 2, 3, 3, 6, 9, 4], [6, 7, 2, 3, 9, 3, 1, 4, 1, 5], [7, 3, 6, 5, 3, 7, 6, 1, 6, 3], [1, 5, 7, 4, 7, 6, 
6, 2, 9, 9], [1, 7, 0, 6, 8, 0, 0, 4, 8, 2], [0, 1, 5, 3, 0, 4, 6, 6, 0, 9], [5, 6, 8, 7, 1, 5, 9, 1, 9, 2], [1, 4, 1, 0, 7, 2, 6, 1, 3, 4], [8, 8, 9, 7, 4, 6, 0, 6, 7, 6], [6, 5, 7, 6, 1, 3, 5, 6, 4, 7], [9, 2, 1, 7, 1, 9, 5, 4, 3, 7], [2, 2, 9, 8, 7, 4, 0, 0, 1, 8], [8, 0, 1, 0, 8, 1, 8, 4, 8, 4], [2, 0, 8, 0, 9, 1, 8, 7, 9, 8], [6, 2, 8, 0, 1, 9, 0, 1, 3, 9], [1, 1, 7, 0, 1, 5, 5, 1, 2, 2], [9, 6, 0, 0, 2, 4, 7, 1, 1, 6], [5, 5, 6, 7, 6, 8, 7, 1, 4, 3], [3, 2, 6, 7, 2, 8, 3, 0, 2, 6], [2, 2, 6, 0, 7, 9, 9, 9, 3, 6], [8, 7, 6, 1, 2, 3, 6, 1, 4, 2], [9, 1, 4, 9, 0, 8, 7, 7, 3, 0], [1, 8, 5, 6, 2, 5, 7, 1, 5, 4], [4, 8, 6, 9, 0, 6, 8, 9, 7, 4], [9, 6, 
3, 9, 1, 3, 2, 5, 6, 0], [9, 8, 7, 6, 6, 9, 5, 1, 8, 1], [4, 7, 5, 8, 1, 1, 4, 8, 9, 1], [9, 6, 7, 2, 7, 1, 9, 9, 1, 0], [1, 0, 5, 3, 3, 4, 5, 0, 2, 1], [4, 5, 6, 8, 5, 3, 9, 6, 5, 3], [9, 2, 1, 3, 6, 6, 7, 0, 5, 5], [8, 8, 0, 2, 2, 1, 7, 8, 7, 3], [8, 0, 2, 3, 3, 6, 5, 3, 3, 3], [5, 1, 8, 6, 5, 7, 8, 9, 8, 6], [7, 3, 8, 9, 9, 3, 2, 6, 4, 9], [7, 6, 6, 8, 6, 9, 1, 3, 8, 9], [1, 4, 6, 3, 7, 3, 4, 0, 5, 0], [7, 4, 0, 5, 5, 8, 1, 8, 4, 8], [5, 9, 6, 0, 3, 3, 1, 9, 7, 6], [6, 1, 5, 4, 2, 1, 0, 7, 1, 8], [0, 8, 1, 2, 8, 6, 1, 9, 8, 2], [5, 6, 8, 4, 7, 3, 0, 6, 5, 0], [2, 7, 7, 3, 0, 4, 0, 9, 0, 2], [7, 3, 2, 8, 2, 0, 0, 5, 1, 8], [4, 3, 8, 0, 1, 6, 8, 2, 5, 3], [4, 8, 2, 9, 0, 9, 6, 1, 8, 4], [2, 2, 7, 8, 6, 5, 2, 9, 5, 6], [5, 0, 5, 4, 9, 8, 6, 3, 3, 7], [0, 6, 6, 6, 2, 1, 7, 8, 4, 6], [1, 8, 7, 2, 1, 8, 0, 9, 1, 2], [0, 2, 3, 2, 4, 4, 7, 0, 1, 2], [2, 0, 1, 0, 6, 3, 3, 8, 6, 3], [4, 6, 1, 4, 8, 1, 3, 8, 0, 3], [1, 6, 5, 9, 5, 1, 5, 6, 2, 5], [9, 7, 3, 7, 3, 7, 8, 4, 4, 6], [2, 8, 2, 7, 9, 8, 4, 5, 7, 8], [9, 8, 7, 9, 8, 3, 3, 1, 7, 8], [8, 8, 3, 2, 5, 3, 4, 1, 0, 8], [9, 6, 1, 6, 2, 2, 
5, 2, 3, 9], [5, 3, 1, 2, 9, 7, 1, 6, 0, 4], [6, 2, 0, 5, 7, 2, 2, 8, 4, 0], [4, 4, 0, 4, 5, 1, 6, 6, 6, 9], [2, 0, 7, 5, 6, 3, 9, 8, 4, 2], [9, 2, 8, 8, 4, 1, 7, 2, 8, 3], [0, 3, 4, 0, 8, 9, 5, 0, 3, 9], [4, 5, 6, 1, 8, 3, 5, 4, 9, 8], [0, 3, 7, 2, 6, 0, 8, 3, 2, 7], [8, 1, 6, 7, 4, 5, 6, 9, 8, 0], [5, 5, 1, 0, 5, 1, 0, 7, 9, 1], [5, 4, 8, 1, 0, 2, 2, 3, 5, 2], [4, 9, 8, 2, 7, 8, 9, 2, 4, 2], [2, 1, 5, 7, 7, 6, 7, 1, 8, 2], [5, 3, 6, 3, 6, 4, 1, 2, 9, 3], [6, 6, 4, 7, 3, 6, 5, 1, 3, 0], [3, 4, 4, 2, 0, 5, 7, 4, 2, 3], [3, 4, 7, 6, 7, 7, 0, 5, 5, 0], [6, 7, 7, 5, 3, 0, 8, 0, 9, 6], [2, 5, 3, 2, 3, 2, 3, 2, 4, 3], [2, 5, 9, 8, 5, 9, 0, 6, 6, 2], [6, 9, 
9, 4, 8, 6, 5, 0, 2, 0], [5, 1, 4, 2, 8, 6, 2, 7, 9, 5], [0, 6, 4, 9, 4, 4, 3, 0, 0, 7], [3, 0, 2, 8, 9, 9, 4, 3, 5, 8]]

count = 0
for row in range(len(list2d)):#range assumes start == 0 and step == 1
    for col in range(len(list2d[row])):#range assumes start == 0 and step == 1
        if(7 == list2d[row][col]):
            count +=1
    print(count) # 101



#Change each consonant to a "C" and each vowel to a "V"

list2d = [                          #For Loops with 2d Lists
  ["a","b","c","d","e","f"],# 0               | '''Keep these things in mind'''
  ["g","h","i","j","k","l"],# 1  row indexes  |#to access an element --> list2d[row][col]
  ["m","n","o","p","q","r"],# 2               | #range(start, stop, step)
  ["s","t","u","v","w","x"] # 3               | 
  # 0   1   2   3   4   5
        #column indexes
]
# len(list2d) == 4 // len(list2d[row] == 6)

vowels = "aeiou"
for row in range(len(list2d)):#range assumes start == 0 and step == 1
    for col in range(len(list2d[row])):#range assumes start == 0 and step == 1
        if list2d[row][col] in vowels:
            list2d[row][col] = "V"
        else:
            list2d[row][col] = "C"

print(list2d)

[['V', 'C', 'C', 'C', 'V', 'C'], 
 ['C', 'C', 'V', 'C', 'C', 'C'], 
 ['C', 'C', 'V', 'C', 'C', 'C'], 
 ['C', 'C', 'V', 'C', 'C', 'C']]


#Loop in a serpentine pattern
list2d = [ 
  [0, 1, 2, 3, 4], #forward
  [0, 1, 2, 3, 4], #backward
  [0, 1, 2, 3, 4], #forward
  [0, 1, 2, 3, 4], #backward
  [0, 1, 2, 3, 4]  #forward
] 

for row in range(len(list2d)):
    if(0 == row % 2):
        for col in range(len(list2d[row])):
            print(list2d[row][col], end = " ")
    else:
        for col in range(len(list2d[row]-1,-1,-1)):
            print(list2d[row][col], end = " ")
