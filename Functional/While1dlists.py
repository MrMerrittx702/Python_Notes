'''While Loops with Lists'''

#lists
              #elements
list1d = [1,2,3,4,5,6,7,8,9] #declare and initialize
#index    0 1 2 3 4 5 6 7 8
#length = 9

#access
list1d[0]
print(list1d[0])

#change
list1d[0] = 42

#get length
length = len(list1d)
print(length)



'''Setting up a while loop to iterate through a list'''

#using index instead of count 
index = 0 #start (starting index in python is 0)

while index < :#stop (stop at the end of the list)
  #indent 2 spaces for code in the block



  index +=  #step (usually by 1)
#unindent to leave the block


'''Loop through a list beginning to end'''

index = 0

while index < len(list1d): # or <= len(list1d)-1

  print(list1d[index], end = " ")
  
  index += 1

'''Loop through a list end to beginning'''
index = len(list1d)-1

while index >= 0: # or > -1
  
  print(list1d[index], end = " ")

  index -= 1

'''Loop through a list middle to end'''
#get the middle index
index = int(len(list1d)/2) #int() float 4.5 --> integer 4

while index < len(list1d):# or <= len(list1d)-1
  print(list1d[index], end = " ")

  index += 1

'''Loop through a list middle to beginning'''
index = int(len(list1d)/2) #int() float 4.5 --> integer 4

while index >= 0: #or > -1
  print(list1d[index], end = " ")

  index -= 1

