'''For Loops without lists'''


'''
Covered in this video:
> For Loop Syntax
> range() function
> Counting Up by 1 and by multiples
> Counting Down by 1 and by multiples
> Nested For loops
> Throw away variable _
'''
#Syntax: rules for writing a language

'For Loop Syntax'

for variable in range(): 
  #indent 2 spaces to be inside the loop block
  'repeat this code block'
#unindent 2 spaces to exit the loop block

#------------------------------------#
for variable in range(): #-----#     #         
  'repeat this code block'     #     #
  #----------------------------#     #
#------------------------------------# 

'the range function'

#returns a range of numbers from start to < stop. 
range(start, stop, step)
#start is included (default is 0)
#stop is not included (+1 if going up or -1 if going down)
#step (default is 1)

#examples
range(0,10,1) #0 to 9
range(10) #0 to 9
range(10,0,-1)#10 to 1
range(-5,6,1)#-5 to 5
range(5,-6,-1)#5 to -5

'Counting Up by 1 and by multiples'

for number in range(start,stop,step):
  print(number, end = " ")#prints the value of number, and  adds a single space

#examples
for number in range(1,11,1): #1 to 10 by 1s
  print(number, end = " ")
  #output: 1 2 3 4 5 6 7 8 9 10

for number in range(1,11): #1 to 10 by 1s (default)
  print(number, end = " ") 
  #output: 1 2 3 4 5 6 7 8 9 10

for number in range(10): #0 (default) to 9 by 1s (default)
  print(number + 1, end = " ")
  #prints number + 1 to output 1 to 10 
  #ie 0+1=1, 1+1=2, ...
  #output: 1 2 3 4 5 6 7 8 9 10

for number in range(0,11,2): #0 to 10 by 2s
  print(number, end = " ")
  #output: 0 2 4 6 8 10

'Counting Down by 1 and by multiples'

for number in range(10,0,-1): # 10 to 0 by -1
  print(number, end = " ") 
  #output: 10 9 8 7 6 5 4 3 2 1

for number in range(10,0,-2): # 10 to 0 by -1
  print(number, end = " ") 
  #output: 10 8 6 4 2

'Nested For Loops'

#Syntax
for variable_1 in range():
  #indent 2 spaces to be inside the outer loop block
  for variable_2 in range():
    #indent 2 spaces to be inside the inner loop block
    'repeat the code block'
  #unindent to exit the inner loop block
#unindent to exit the outer loop block

#-------------------------------------------#
for variable_1 in range(): #-----------#    #
  for variable_2 in range(): #----#    #    # 
    'repeat the code block'       #    #    #
    #-----------------------------#    #    #
  #------------------------------------#    #
#-------------------------------------------#

#examples

for repeat in range(3):# repeat 3 times
  for number in range(0,5,1):# 0 to 4 by 1s
    print(number, end = " ")
  print() #added to format output
#output:
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 

for repeat in range(2):# repeat 2 times
  for number in range(0,101,20):# 0 to 100 by 20s
    print(number, end = " ")
  print() #added to format output
#output:
# 0 20 40 60 80 100 
# 0 20 40 60 80 100 

for repeat in range(4):# repeat 4 times
  for number in range(5,-6,-1):# 5 to -5 by 1s
    print(number, end = " ")
  print() #added to format output
#output:
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5

for repeat in range(4):# repeat 4 times
  for number in range(20,9,-2):# 20 to 10 by 2s
    print(number, end = " ")
  print() #added to format output
#output:
# 20 18 16 14 12 10 
# 20 18 16 14 12 10
# 20 18 16 14 12 10
# 20 18 16 14 12 10


'Throw away variable _ '
#sometimes we don't use a variable but need a place holder
#use underscores as throw away variables

for _ in range(5): #here we don't use the variable for this loop so we use an _
  for number in range(10): # 0 (default) to 9 by 1s (default)
    print(number, end = " ")
  print() # added to format output



