

'''While loop problems'''

#count up to 10

#count down from 10

#count up to 1000

#count down from 1000

#count up to 20 starting from 10

#count down to 50 starting from 70

#count to 500 by 5s starting at 0

'''Nested While loops'''
#count up to 5. Repeat this 5 times.

#count up to 10. Repeat this 100 times. 

#count down from 100. Repeat this 5 times. 

#



'''While loop with 1d list'''
#create the following list 
list1d = [0,1,2,3,4,5,6,7,9]

#loop from beginning to end and print out each item in the list

#loop from the end to the beginning and print out each item in the list.

#loop from the middle index to the end and print out each element(item).

#Loop from the middle index to the beginning and print out each element (item). 

'''While loop with 2d list'''
#create the following list 
list2d = [
  ["r 0, c 0","r 0, c 1","r 0, c 2","r 0, c 3"],
  ["r 1, c 0","r 1, c 1","r 1, c 2","r 1, c 3"],
  ["r 2, c 0","r 2, c 1","r 2, c 2","r 2, c 3"]
]
#create a nested while loop that loops forward through each row and each column then prints out what row and what column you are at. 

#create a nested while loop that loops forward through each row and each column then prints out each element(item)

#create a nested while loop that loops backward through each row and each column then prints out each element(item)

#create a nested while loop that loops forward through each row, but backward through each column and prints out each element(item).

#copy the following 2d list into your code

'''Looping through a 2d list with the len function'''
list2d = [
  [0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
  [0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0],
  [0,0,0,0,0,0,0,8,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,8],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0],
  [8,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0],
  [0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
  [0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,8],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,8,0,0,0,0,0,0,0,0,8,0,0,0,0,0,8,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0],
  [8,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0]
]

#use a nested while loop to count the number of 0s in the 2d list

#use a nested while loop to count the number of 8s in this 2d list

#use a nested while loop to count the number of 0s in the first half rows of the list

#use a nested while loop to count the number of 8s in the second half of the list. 
count_8s = 0
row = 0
while row < len(list2d):

  col = 0 
  while col < len(list2d[row]):

    if(list2d[row][col] == 8):
      list2d[row][col] = "X"
    else:
      list2d[row][col] = "-"
    
    print(list2d[row][col], end = " ")
    col += 1

  print()
  row += 1





array[-1]