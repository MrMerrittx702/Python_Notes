#===============================================================================================================================#
'''Python Conditionals'''
#===============================================================================================================================#

#iterate: repitition of a process or function
#condition: statement that evaluates True/False to determine if a code block is run.

'''
  Covered in this video:
  > Review: Booleans, Relational Operators,and  Logical Operators
  > Boolean Expressions 
  > Python Indentation and Code Blocks
  > if Statements
  > if-else Statements
  > Chained Conditionals 
  > Nested Conditionals 
  > Ternary Operators: Shorthand Conditionals`
'''
#===============================================================================================================================#
'> Review: Booleans, Relational Operators, and  Logical Operators'

#Conditionals often utilize booleans, relational operators, and logical operators. 

#Booleans (True/False)
True
False

#Relational Operators (Inequalities)
#relational operators are used for comparisons 
#evaluate to a boolean (True/False)
#Order of operations is left to right
'''
>  #greater than
<  #less than 
>= #greater than or equal to
<= #less than or equal to
== #equal to
!= #not equal to

#Special to python
is # identical to
is not # not identical to
in # apart of
not in # not apart of

#Logical Operators (for multiple conditions)
#Order of Operations NAXO
not (~) # opposite: ~T --> F // ~F --> T
and (&) #both : T and T --> T //all others are F
xor (^) # only 1: T ^ F, F ^ T --> T // all others F
or (|)  # at least 1: F or F --> F // all others are T
'''

#Truth tables show how logical operators are evaluated

#===============================================================================================================================#
'> Boolean Expressions (evaluate True or False)'

#String Comparisons
print("text" == "text") #True

#Number Comparisons
print(5 >= 2) #True

#Variable Comparisons
x = "some text"
y = "other text"
print(x == y) #False


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
    #start of for code block----------------------#      #
    while(condition):                             #      #
      #start of while code block -----------#     #      #      
      if(condition):                        #     #      #
        #Start of if code block ------#     #     #      #
        print("So many indents!")     #     #     #      #
      #end of if code block-----------#     #     #      #
    #end of while code block----------------#     #      #
  #end of for code block--------------------------#      #
#end of function code block------------------------------#


'''
Note:
Indentation is typically achieved using spaces or tabs. 
Don't mix spaces and tabs, it can lead to syntax errors or inconsistent behavior. 
Python 3 disallows mixing tabs and spaces for indentation in the same source file.

If you are using an editor like VS code using the tab key, and spaces is not a problem. 
'''

#===============================================================================================================================#
'> if Statements'
#Syntax
condition = True or False

  #the condition in parenthesis is a boolean expression
if(condition):  #end with a colon ":"
  #indent 2 spaces to be inside the if code block
  'Code Block Here'

#unident 2 spaces to be outside the if code block

#----------------------------------------------------#
if(condition): #----------------------------------#  #
  'runs this block when the condition is True'    #  #
  'skips this block when the condition if False'  #  #
  #-----------------------------------------------#  #
#----------------------------------------------------#

#each new if starts its own separate conditional

if(True): #--------#        
  'run this block' # 
#------------------#

if(False): #--------#
  'skip this block' # 
#-------------------#

'''
  Special Notes for Conditionals:
    When writing if statments you will often get output, sometimes even correct output, but you code does not work as intended in every case. 
    Any non-zero number (integer, float) is evaluated as True
    Any non-empty string, list, tuple, set, or dictionary,  is evaluated as True
    Any function, method, lambda or class is evaluated as True
    By default objects are evaluated True, but how an object is evaluated can be changed.
'''



#===============================================================================================================================#
'> if-else Statements'
#------------------------------------------------------------#
if(condition): #---------------------------------#           #
  'runs this block when the condition is True    '           #
  'skips this block when the condition is False  '           #
  #----------------------------------------------#           #
else: #---------------------------------------------------#  #
  'runs this block when all conditions above it are False '  #
  'skips this block when any condition above it is True   '  #
  #-------------------------------------------------------#  #
#------------------------------------------------------------#

#------------------------#
if(True): #--------#     #
  'run this block' #     #
  #----------------#     #
else: #--------------#   #
  'skip this block'  #   #
  #------------------#   #
#------------------------#

#-------------------------#
if(False): #---------#    #
  'skip this block'  #    #
  #------------------#    #
else: #------------#      #
  'run this block' #      #
  #----------------#      #
#-------------------------#

#===============================================================================================================================#
'if-elif-else (Chained Conditional)' 
#-------------------------------------------------------------------------------------#
if(condition): #----------------------------------#                                   #
  'runs this block when the condition is True'    #                                   #
  'skips this block when the condition is False'  #                                   #
  #-----------------------------------------------#                                   #
elif(condition): #----------------------------------------------------------------#   #
  'runs this block when the conditions above are False and its condition is True '#   #
  'skips this block when an above condition is True or its condition is False'    #   #
  #-------------------------------------------------------------------------------#   #
else:#----------------------------------------------------------#                     #
  'runs this block only when the conditions above it are False' #                     #
  'skips this block when any condition above it is True'        #                     #
  #-------------------------------------------------------------#                     # 
#-------------------------------------------------------------------------------------#

#-------------------------------#
if(True): #----------#          #
  'run this block'   #          #
  #------------------#          #
elif(True): #-----------#       #
  'skip this block'     #       #
  #---------------------#       #
else: #--------------#          #
  'skip this block'  #          #
  #------------------#          #
#-------------------------------#

#-------------------------------#
if(False): #----------#         #
  'skip this block'   #         #
  #-------------------#         #
elif(True): #-----------#       #
  'run this block'      #       #
  #---------------------#       #
else: #--------------#          #
  'skip this block'  #          #
  #------------------#          #
#-------------------------------#

#-------------------------------#
if(False): #----------#         #
  'skip this block'   #         #
  #-------------------#         #
elif(False): #----------#       #
  'skip this block'     #       #
  #---------------------#       #
else: #--------------#          #
  'run this block'   #          #
  #------------------#          #
#-------------------------------#
#===============================================================================================================================#
'> Nested Conditionals'
#conditionals inside conditionals
if(True):
  if(True):
    'the block runs only if both are True'

a = True or False
b = True or False
c = True or False

#-------------------------------------------------#
if(a):                                            #
  print("a is True")                              #
  #-------------------------------------#         #
  if(b):                                #         #
    print("a,b are True")               #         #
    #----------------------------#      #         #
    if(c):                       #      #         #
      print("a,b,c are True")    #      #         #
    else:                        #      #         #
      print("c is False")        #      #         #
    #----------------------------#      #         #
  else:                                 #         #
    print("a is True")                  #         #
  #-------------------------------------#         #
else:                                             #
  print("a is False")                             #
#-------------------------------------------------#

#There can many different combinations

#===============================================================================================================================#
'> Ternary Operator: Shorthand Conditionals'

#ternary operators are a shorthand way of writing if statements
#They are best used for short simple conditionals, as longer ternary operators are confusing. 

#syntax --> x if condition else y
x = 2; y = 3; z = 4
print("if") if True else print("else")
print("if") if x > 0 else print("else if") if y > 0 else print("else")

# The term "ternary" refers to the fact that it takes three operands: the condition to be evaluated, 
# the expression to be returned if the condition is true, and the expression to be returned if the 
# condition is false.

