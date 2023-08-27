'''For Loops with 2D Lists'''

'''
Covered in this video:
> 2D lists review: creation, indexes, access, change, len() function. 
> Looping Forward, rows and columns
> Looping Backward, rows and columns
> For Each Loop
'''
'2D lists review: creation, indexes, access, change, len() function.'

#a 2D list is a list of lists
list2d = [["a","b","c","d","e","f"],["g","h","i","j","k","l"],["m","n","o","p","q","r"],["s","t","u","v","w","x"]]
#             list 0                        list 1                  list 2                    list 3                 
# list2d is a list of 4 lists

#simplify by formatting the code this way 
list2d = [
  ["a","b","c","d","e","f"], #list 0
  ["g","h","i","j","k","l"], #list 1
  ["m","n","o","p","q","r"], #list 2
  ["s","t","u","v","w","x"]  #list 3
]


#simply in our mind as rows and columns 
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes

#access (use the list name and [row][col] to access an element)
list2d[0][0] # a
list2d[0][1] # b
list2d[3][5] # z

#change (use the list name and [row][col] to access an element then = new value)
list2d[0][0] = "aa"
list2d[3][5] = "xx"

#len() function
len(list2d) # 4 (number of rows/lists)
len(list2d)-1 # 3 (last row index)

row = 0 #represents the row, in this case the row at index 0 
len(list2d[row]) # 6 number of columns/elements in a given row/list
len(list2d[row])-1 # 5 last column index 


'Looping Forward, rows and columns'

#Syntax
'''
for row in range(): #row represents row indexes
  for col in range(): #col represent column indexes
'''
#end = ", " and end = " |" are just for formatting the output

for row in range(0,len(list2d),1): # first row(0) to last row by 1s
  for col in range(0,len(list2d[row]),1): # first col(0) to last col by 1s
    print(row, col, end = ", ")#printing indexes
    print(list2d[row][col], end = " |") #printing elements
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
  


'Looping Backward, rows and columns'
#end = ", " and end = " |" are just for formatting the output

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
  

'For Each Loop'
#special for loop syntax
#end = "|" is just for formatting the output

for row in list2d:
  for col in row:
    print(col, end = "|")
  print() # this line is just for formatting the output

#no formating
for row in list2d:
  for col in row:
    print(col)