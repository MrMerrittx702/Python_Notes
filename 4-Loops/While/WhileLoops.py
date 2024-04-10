#===============================================================================================================================#
'''Python While Loops without lists'''
#===============================================================================================================================#
'''
Covered in this file:
> Iteration Defined
> Python indentation and Code Blocks
> While Loops Syntax
> The control variable
> Counting with while loops
> Counting Up by 1 and by multiples
> Counting Down by 1 and by multiples
> Infinite Loops and Off by 1 Errors
> Special to Python: While-Else
> Nested While Loops
> Break, Continue, and Pass
'''
#iterate: repitition of a process or function
#condition: statement that evaluates True/False to determine if a code block is run.
#Syntax: rules for writing a language
#===============================================================================================================================#
'> Iteration Defined'
'''
  Iteration is the repitition of a process or function.
  Iterables are data types that can return their values one at a time

  Iteration can be thought of as looping or repeating
'''

#===============================================================================================================================#
'> Python Indentation and Code Blocks'
'''
  Indentation creates blocks of code, which are groups of statements that are executed together as a unit. 
  Each indentation level represents a higher level of code structure(conditionals, loops, functions, classes)
  All statements within the same block must have the same level of indentation. 
  The end of a block is indicated by the decrease in indentation level. 
'''
#examples
condition = True or False

if(condition):
    #start of the if code block
    print("Inside the if statement")

#end of the if code block
while(condition):
    #start of the while code block
    print("Inside the while loop")

#end of the while code block
for _ in range(10):
    #start of the for code block
    print("Inside the for loop")

#end of the for code block
def function_():
    #start of the function code block
    print("Inside of the function definition")

#end of the function code block
  
#Nested Indentation# Blocks inside of blocks
def example_():
    #start of function code block--------------------------#
    for _ in range(5):                                     #
        #start of for code block----------------------#    #
        while(condition):                             #    #
            #start of while code block -----------#   #    #      
            if(condition):                        #   #    #
                #Start of if code block ------#   #   #    #
                print("So many indents!")     #   #   #    #
            #end of if code block-------------#   #   #    #
        #end of while code block------------------#   #    #
    #end of for code block----------------------------#    #
#end of function code block--------------------------------#

'''
Note:
  Indentation is typically achieved using spaces or tabs. 
  Don't mix spaces and tabs, it can lead to syntax errors or inconsistent behavior. 
  Python 3 disallows mixing tabs and spaces for indentation in the same source file.

  If you are using an editor like VS code using the tab key, and spaces is not a problem. 
'''
#===============================================================================================================================#
'> While Loop Syntax'
condition = True or False


while(condition):
    #indent 4 spaces to be inside of the loop block
    'repeat this code block'
#unindent 4 spaces to exit the loop block

#------------------------------------#
while(condition): #-------------#    #
    'repeat this code block'    #    #
    #---------------------------#    #
#------------------------------------#


#===============================================================================================================================#
'> The control variable'
#while loops will often end up in an infinite loop
#to fix this error while loops usually have a control variable

count = 0 #this is the control variable

while count < 5: #stops the loop when count is >= 5
    'repeat this code'
    count = count + 1 #increases count each time the loop occurs
    #count += 1 is shorthand for the line above

#pay attention to the indentation


#===============================================================================================================================#
'> Counting with while loops'

start = 0 #start: where to start counting
stop = 5 #stop: where to stop counting
step =1 #step: how much to increase or decrease by each time

count = start
while(count < stop):  #can be > < >= or <= stop

    count = count + step # can be + - * / % ...

    #or use the compound assignment operators
    count += step   #can be += -= *= /= ... 


#===============================================================================================================================#
'> Counting Up by 1 and by multiples'

#programmers with often use the letter i as a control variable
#++++++++++++++++++++++++++++++++++++++#
'0 to Positive By 1s'
i = 0 #start at 0
while(i < 5): #stop when i is 5  (i <= 4)
    print(i, end = " ") #print out i with a space at the end
    i += 1 #step  increment i by 1
# 0 1 2 3 4 

'0 to Positive By Multiples'
i = 0 #start at 0
while(i < 5): #stop when i is 5  (i <= 4)
    print(i, end = " ") #print out i with a space at the end
    i += 2 #step  increment i by 2
# 0 2 4 
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From 1 to Positive by 1s'
#From 1 to positive
i = 1 #start 
while (i < 6): #stop (i <= 5)
    print(i, end = " ")
    i += 1 #step  increment i by 1
# 1 2 3 4 5 

'From 1 to Positive by Multiples'
i = 1 #start 
while (i < 6): #stop (i <= 5)
    print(i, end = " ")
    i += 3 #step  increment i by 3
# 1 4 
#++++++++++++++++++++++++++++++++++++++# 
#++++++++++++++++++++++++++++++++++++++#
'From Positive to Positive by 1s'
i = 10 #start
while( i < 21): #stop (i <= 20)
    print(i, end = " ")
    i+=1 #step  increment i by 1
# 10 11 12 13 14 15 16 17 18 19 20 
  
'From Positive to Positive by Mutliples'
i = 10 #start
while( i < 21): #stop (i <= 20)
    print(i, end = " ")
    i+=5 #step  increment i by 5
# 10 15 20 
#++++++++++++++++++++++++++++++++++++++#  
#++++++++++++++++++++++++++++++++++++++#
'From Negative to 0 by 1s'
i = -5 #start
while(i < 1): #stop (i <= 0)
    print(i, end = " ")
    i+=1  #step increment i by 1
# -5 -4 -3 -2 -1 0 

'From Negative to 0 by Multiples'
i = -5 #start
while(i < 1): #stop (i <= 0)
    print(i, end = " ")
    i+=3  #step increment i by 3
# -5 -2 
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From Negative to Negative by 1s'
i = -10 #start
while(i < -4): #stop (i <= -5)
    print(i, end = " ")
    i+=1 #step  increment i by 1
# -10 -9 -8 -7 -6 -5 

'From Negative to Negative by Multiples'
i = -10 #start
while(i < -4): #stop (i <= -5)
    print(i, end = " ")
    i+= 3 #step  increment i by 3
# -10 -7 
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From Negative to Positive by 1s'
i = -3 #start
while(i < 4): #stop (i <= 3)
    print(i, end = " ")
    i+=1 #step increment i by 1
# -3 -2 -1 0 1 2 3 


'From Negative to Positive by Multiples'
i = -3 #start
while(i < 4): #stop (i <= 3)
    print(i, end = " ")
    i+= 2 #step increment i by 2
# -3 -1 1 3
#++++++++++++++++++++++++++++++++++++++#  

#===============================================================================================================================#
'> Counting Down by 1 and by multiples'


'From Positive to 0 by 1s'
i = 10 #start
while(i > -1): #stop (i >= 0)
    print(i, end = " ")
    i -= 1 #step
# 10 9 8 7 6 5 4 3 2 1 0 

'From Positive to 0 by Multiples'
i = 10 #start
while(i > -1): #stop (i >= 0)
    print(i, end = " ")
    i -= 3 #step
# 10 7 4 1 
  


'From Positive to Positive by 1s'
i = 50 #start
while(i > 39): #stop (i >= 40)
    print(i, end = " ")
    i -= 1 #step
# 50 49 48 47 46 45 44 43 42 41 40 

'From Positive to Positive by Multiples'
i = 50 #start
while(i > 39): #stop (i >= 40)
    print(i, end = " ")
    i -= 3 #step
# 50 47 44 41 



'From Positive to Negative by 1s'
i = 5 #start
while(i > -2): #stop (i >= -1)
    print(i, end = " ")
    i -= 1#step
# 5 4 3 2 1 0 -1 

'From Positive to Negative by Multiples'
i = 5 #start
while(i > -2): #stop (i >= -1)
    print(i, end = " ")
    i -= 4 #step
# 5 1 



'From 0 to Negative by 1s'
i = 0 #start
while(i > -7): #stop (i >= -6)
    print(i, end = " ")
    i -= 1#step
# 0 -1 -2 -3 -4 -5 -6 

'From 0 to Negative by Multiples'
i = 0 #start
while(i > -7): #stop (i >= -6)
    print(i, end = " ")
    i -= 3 #step
# 0 -3 -6 



'From Negative to Negative by 1s'
i = -6 #start
while(i > -15): #stop (i >= -14)
    print(i, end = " ")
    i -= 1#step
# -6 -7 -8 -9 -10 -11 -12 -13 -14 

'From Negative to Negative by Multiples'
i = -6 #start
while(i > -15): #stop (i >= -14)
    print(i, end = " ")
    i -= 4#step
# -6 -10 -14 

#===============================================================================================================================#
'> Infinite Loops and Off by 1 Errors'

'''
  Infinite Loops
  An infinite loop is a loop that continues executing 
    indefinitely because its exit condition is never met. 

'''
# examples
condition = True
while (condition):
    print("This is an infinite loop!")

i = 0
while (i < 10):
    print("This is an infinite loop")

i = 5
while( i > 0):
    print("This is an infinite loop")
    i+=1

'''
  Off-by-One Errors
  Off-by-one errors occur when a loop iterates one too 
    many or one too few times, typically due to incorrect 
      indexing or boundary conditions. 
'''

#example
#count from 0 to 5
i = 0
while (i < 5):
    print(i, end = " ")
    i+=1
#Off by 1, only counts from 0 to 4

#===============================================================================================================================#
'> Special to Python: While-Else'

#when the condition is no longer true run the else
i = 1
while(i <= 5):
    print("Counting...", i)
    i+=1
else: #when i becomes 6 this block runs
    print("Finished Counting")

#===============================================================================================================================#
'> Nested While Loops'

#Placing one While Loop into another While Loop

outer_start = 0; outer_stop = 0; outer_step = 0
inner_start = 0; inner_stop = 0; inner_step = 0


repeat = outer_start
while(repeat < outer_stop):#Outer Loop------------#
                                                  #
    count = inner_start                           #
    while(count < inner_stop):#Inner loop--#      #
        print(count, end = " ")            #      #
        count += inner_step                #      #
    #--------------------------------------#      #
    repeat += outer_step                          #
#-------------------------------------------------#

#Example count to 5, 3 times
repeat = 0
while(repeat < 3):

    count = 0
    while(count < 6):
        print(repeat, count)
        count += 1
    
    repeat += 1




#===============================================================================================================================#
'> Break and Continue'

'''
  Break
  The break statement in Python is used to exit (or "break out of") the loop prematurely. 
  It is commonly used within loops like for and while to interrupt the loop's execution based on a certain condition.
'''
while(True):
    break
#the loop will exit on the first loop

'''
  Continue
  The continue statement in Python is used to skip the rest of the code 
  inside a loop for the current iteration, and continue with the next iteration 
  of the loop.
'''
i = 0
while(i < 5):
    if(i == 2):
        i+=1
        continue
    print(i)
    i+=1
#skips the number 2
  
