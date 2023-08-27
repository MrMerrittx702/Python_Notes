''' For Loops with 1D lists'''

'''
Covered in this video:
> 1D list review: creation, indexes, access, changing, len() function. 
> Looping Forward (Beginning to End)
> Looping Backward (End to Beginning)
> Calculating the middle index
> Looping Beginning to Middle
> Looping Middle to End
> Looping End to Middle
> Looping Middle to Beginning
> The For Each Loop
'''

'1D list review: creation, indexes, access, changing, len() function.'
# index  : 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
list1d = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#          Each item in the list is called an "element"


#access (use the list name and [index] to access an element)
list1d[0] # a
list1d[1] # b
list1d[25] # z

#change (use the list name and [index] to access an element then = new value)
list1d[0] = "aa"
list1d[2] = "cc"

#len() function
len(list1d) # 26 (number of elements)
len(list1d)-1 # 25 (last index)

'Looping Forward (Beginning to End)'
#end ="|" is just for formatting the output

for index in range(0,len(list1d),1): # 0 to last index by 1s
  print(index, end ="|") #printing indexes
  print(list1d[index]) #printing elements

for index in range(len(list1d)): # 0 (default) to last index by 1s (default)
  print(index, end ="|") #printing indexes
  print(list1d[index]) #printing elements 


'Looping Backward (End to Beginning)'
#end ="|" is just for formatting the output

for index in range(len(list1d)-1,-1,-1):#last index to 0 by 1s 
  print(index, end ="|") #printing indexes
  print(list1d[index]) #printing elements


'Calculating the middle index'

# index  : 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
list1d = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#          Each item in the list is called an "element"
len(list1d) # 26 (number of elements)
len(list1d)-1 # 25 (last index)

len(list1d)/2 # 13.0 (cannot use a float as an index)
int(len(list1d)/2) # 13 (13 is the 14th index) 13-25 is the back half
int(len(list1d)/2-1) # 12 (12 is the 13th index) 0-12 is the front half
middle_index = int(len(list1d)/2-1)


'Looping Beginning to Middle'
#end ="|" is just for formatting the output

for index in range(0, int(len(list1d)/2), 1): #0 to middle index by 1s
  print(index, end ="|") #printing indexes
  print(list1d[index]) #printing elements

for index in range(int(len(list1d)/2)): #0 (default) to middle index by 1s (default)
  print(index, end ="|") #printing indexes
  print(list1d[index]) #printing elements

'Looping Middle to End'
#end ="|" is just for formatting the output

for index in range(int(len(list1d)/2), len(list1d), 1): #middle index to last index by 1s
  print(index, end ="|") #printing indexes
  print(list1d[index]) #printing elements

#                   middle index to last index by 1s (default)
for index in range(int(len(list1d)/2), len(list1d)): 
  print(index, end ="|") #printing indexes
  print(list1d[index]) #printing elements


'Looping End to Middle'
#end ="|" is just for formatting the output

#                     last index to middle index by 1s
for index in range(len(list1d)-1, int(len(list1d)/2)-1, -1): 
  print(index, end ="|") #printing indexes
  print(list1d[index]) #printing elements

'Looping Middle to Beginning'
#end ="|" is just for formatting the output

#                   middle index to 0 by 1s
for index in range(int(len(list1d)/2-1),-1,-1):
  print(index, end ="|") #printing indexes
  print(list1d[index]) #printing elements


'The For Each Loop'

#special way to write a for loop

#Syntax
for variable in iterable:
#iterables are something that can be repeated through 
# a list is iterable

#element does not represent and index, but the actual element. 
for element in list1d:
  print(element, end = "|")

