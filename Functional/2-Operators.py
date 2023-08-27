'''Python Operators'''

'''
Covered in this video:
> Concatenation (combining strings)
> Casting (changing data type)
> Arithmetic operators (math)
> Relational operators (inequalities, )
> Logical operators (not, and, xor, or)
'''

##################################################################################################
'Concatenation (combining strings)'
  + #combine strings
  * #duplicate string

#Literals are actual values 
"Hello" + "World"

print("Hello" + "World")

#Variable
a = "Hello"
b = "World"
print(a + b)

#Duplicating Strings
"a" * 3
duplicated = "a" * 3
print(duplicated) #aaa

##################################################################################################

'Casting'
type() #returns the data type
str()  #convert to string
int()  #convert to integer
float()# convert to float

#example
a = 5
b = "10"
c = 7
print(type(a))
print(type(b))
print(type(c))
print()

a = str(5)
b = int("10")
c = float(7)
print(type(a))
print(type(b))
print(type(c))


'General Order of Operations'

#1. Arithmetic Operators (PEMDAS)
#2. Relational Operators (LEFT TO RIGHT)
#3. Logical Operators (NAXO)

##################################################################################################
'Arithmetic Operators (Math)'
#Order of operations follows PEMDAS from Algebra
#Parenthesis, Exponents, Multiply/Divide, Add/Substract

+   #add
-   #subtract
*   #multiply
/   #divide
%   #modulo (remainder)
**  #exponentiation (power)

print(5 + 2)  # 7
print(5 - 2)  # 3
print(5 * 2)  # 10
print(5 / 2)  # 2.5
print(5 % 2)  # 1
print(5 ** 2) #25
##################################################################################################
'Relational Operators (Inequalities)'
      #relational operators are used for comparisons 
      #evaluate to a boolean (True/False)
      #Order of operations is from left to right. 

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


      #relational operators are used for comparisons that evaluate to a boolean (True/False)

x = 50; y = 45; z = 45

print(x > y)  #True
print(x < y)  #False
print(x >= z) #True
print(x <= z) #False
print(y == z) #True
print(y != x) #True
##################################################################################################
'Logical Operators' 
#Order of operations for logical Operators is Not, And, Xor, Or (NAXO)

not (~) #opposite
and (&) #both
xor (^) #only one
or (|)  #at least one

#Truth tables show how logical operators are evaluated
a = 5;b = 2; c = 8

#not (~) Truth Table
not True    #False
not False   #True
print(not c > 0) #example --> not True --> False
print(~ c > 0) #example --> not True --> False

#and (&) Truth Table
True and True      #True
True and False     #False
False and True     #False  
False and False    #False

print(a > 4 and c > 10) #example -->  True and False --> True
print(a > 4 & c > 10)   #example -->  True and False --> True

#xor (^) Truth Table exclusive or
True ^ True      #False
True ^ False     #True
False ^ True     #True
False ^ False    #False
print(b > a ^ b >= 2) #example --> False ^ True --> True

#or (|) Truth Table
True or True     #True
True or False    #True
False or True    #True  
False or False   #False
print(a < 4 or b > c) #example --> True or False --> True
print(a < 4 | b > c)  #example --> True or False --> True

'Combining Logical Operators'

#Things can get confusing when combining logical operators, so use parenthesis () to help
a = 1; b = 2; c = 3

print(c < b and b < a or c > a and a > b) #what is going on?!?

print( (c < b and b < a) or (c > a and a > b) )
##################################################################################################

