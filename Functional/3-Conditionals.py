'''Python Conditionals'''

'''
Covered in this video:
> Review: Booleans, Relational Operators,and  Logical Operators
> Boolean Expressions 
> if Statements
> Python Indentation and Code Blocks
> if-else Statements
> Chained Conditionals 
> Nested Conditionals 
'''

#Conditionals often utilize booleans, relational operators, and logical operators. 

#Booleans (True/False)
True
False

#Relational Operators (Inequalities)
#relational operators are used for comparisions 
#evaluate to a boolean (True/False)
#Order of operations is left to right

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

#Truth tables show how logical operators are evaluated


'Boolean Expressions (evaluate True or False)'

#String Comparisions
print("text" == "text") #True

#Number Comparisions
print(5 >= 2) #True

#Variable Comparisions
x = "some text"
y = "other text"
print(x == y) #False

#============================================================================================================================================
'if Statements'
#Syntax

  #the condition in parenthesis is a boolean expression
if(condition):  #end with a colon ":"
  #indent 2 spaces to be inside the if code block
  'Code Block Here'

#unident 2 spaces to be outside the if code block

#----------------------------------------------------#
if(condition): #----------------------------------#  #
  #runs this block when the condition is True     #  #
  #skips this block when the condition if False   #  #
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
#When writing if statments you will often get output, sometimes even correct output, but you code does not work as intended in every case. 
#Any non-zero number (integer, float) is evaluated as True
#Any non-empty string, list, tuple, set, or dictionary,  is evaluated as True
#Any function, method, lambda or class is evaluated as True
#By default objects are evaluated True, but how an object is evaluated can be changed.
'''



#============================================================================================================================================
'if-else Statements'
#------------------------------------------------------------#
if(condition): #---------------------------------#           #
  #runs this block when the condition is True    #           #
  #skips this block when the condition is False  #           #
  #----------------------------------------------#           #
else: #---------------------------------------------------#  #
  #runs this block when all conditions above it are False #  #
  #skips this block when any condition above it is True   #  #
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

#============================================================================================================================================
'if-elif-else (Chained Conditional)' 
#-------------------------------------------------------------------------------------#
if(condition): #----------------------------------#                                   #
  #runs this block when the condition is True     #                                   #
  #skips this block when the condition is False   #                                   #
  #-----------------------------------------------#                                   #
elif(condition): #---------------------------------------------------------------#    #
  #runs this block when the conditions above are False and its condition is True #    #
  #skips this block when an above condition is True or its condition is False    #    #
  #------------------------------------------------------------------------------#    #
else:#----------------------------------------------------------#                     #
  #runs this block only when the conditions above it are False  #                     #
  #skips this block when any condition above it is True         #                     #
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

'Nested Conditionals'
#conditionals inside conditionals
if(True):
  if(True):
    'the block runs only if both are True'

  
#There can many different combinations



