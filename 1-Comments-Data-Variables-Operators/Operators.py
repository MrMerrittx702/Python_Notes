#===============================================================================================================================#
'''Python Operators'''
#===============================================================================================================================#
'''
Covered in this file:
> Concatenation (combining strings)
> Casting (changing data type)
> Arithmetic operators (math)
> Relational operators (inequalities)
  > Membership operators
  > Identity operators
> Assignment vs Equality Operator
> Compound Assignment Operators
> Logical operators (not, and, or)
> Compound Logical Expressions and De Morgan's Laws
> Built-in Operation Function Calls
> Bitwise Operators
> Complete Operator Precedence
'''

#===============================================================================================================================#
'> Concatenation (combining strings)'
' > concatenation means to join'

'''
+ combine strings
* duplicate string
'''

#use the + to concatenate strings
"Hello" + "World"

print("Hello" + "World")

#using a variable
a = "Hello"
b = "World"
print(a + b)

#Duplicating Strings
"a" * 3
duplicated = "a" * 3
print(duplicated) #aaa

#===============================================================================================================================#
'> Casting'
' > converting the type of data.'

'Function calls for casting.'
type() #returns the data type
str()  #convert to string
int()  #Converts a number or string to an integer.
float()#Converts a number or string to a floating-point number.

#example
a = 5
b = "10"
c = 7
print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'> 
print(type(c)) # <class 'int'> 


a = str(5)
b = int("10")
c = float(7)
print(type(a)) # <class 'str'> 
print(type(b)) # <class 'int'>  
print(type(c)) # <class 'float'>

#===============================================================================================================================#
'> General Order of Operations'

#1. Arithmetic Operators (PEMDAS)
#2. Relational Operators (LEFT TO RIGHT)
#3. Logical Operators (NAO)

#===============================================================================================================================#
'> Arithmetic Operators (Math)'
#Order of operations follows PEMDAS from Algebra
#Parenthesis, Exponents, Multiply/Divide, Add/Substract
'''
  **  #exponentiation (power) 

  *   #multiply
  /   #divide
  //  #floor division(Integer division)
  %   #modulo (remainder division)

  +   #add
  -   #subtract
  
'''
print( 5 ** 2 ) #25

print( 5 * 2 )  # 10
print( 5 / 2 )  # 2.5
print( 5 // 2 )  # 2 Truncates 2.5 to 2 (does not round)
print( 5 % 2 )  # 1

print( 5 + 2 )  # 7
print( 5 - 2 )  # 3
#===============================================================================================================================#
'> Relational Operators (Inequalities)'
  #relational operators are used for comparisons 
  #evaluate to a boolean (True/False)
  #Order of operations is from left to right. 
'''
  >  #greater than
  <  #less than 
  >= #greater than or equal to
  <= #less than or equal to
  == #equal to
  != #not equal to

  #Special to python

    Membership Operators
      in      # apart of
      not in  # not apart of

    Identity Operators
      is      # identical to
      is not  # not identical to
    

  '''

  #relational operators are used for comparisons that evaluate to a boolean (True/False)

x = 50; y = 45; z = 45
list1d = ["a","b","c"]
 
print( x > y )  #True
print( x < y )  #False
print( x >= z ) #True
print( x <= z ) #False
print( y == z ) #True
print( y != x ) #True

#Membership Operators
print( "a" in list1d ) #True
print( "d" not in list1d ) #True

#Identity Operators
print( y is z ) #True
print( x is not z ) #True


#===============================================================================================================================#
'> Assignment vs. Equality Operators'

'''
= #assignment 
== #equality (comparision)
'''
# the equal sign must always be on the left side of the operation

#example
a = 1 #a stores the value 1
a == 1 # checks if a is equal to the value 1
#===============================================================================================================================#
'> Compound Assignment Operators'
#shorthand operators to perform an operation and assignment

'''
+=   #add and assign
-=   #subtract and assign
*=   #multiply and assign
/=   #divide and assign
//=  #floor divide and assign
%=   #modulo (remainder) and assign
**=  #exponentiation (power) and assign
'''

x = 1

#THIS        is the same as    THIS
x = x + 1;  'is the same as';  x+=1
x = x - 1;  'is the same as';  x-=1
x = x * 1;  'is the same as';  x*=1
x = x / 1;  'is the same as';  x/=1
x = x // 1; 'is the same as';  x//=1
x = x % 1;  'is the same as';  x%=1
x = x ** 1; 'is the same as';  x**=1
 
#===============================================================================================================================#
'> Logical Operators' 
#Order of operations for logical Operators is Not, And, Or (NAO)
#
'''
not  #opposite
and  #both
or   #at least one
'''
a = True; b = False; c = True

#NOT Truth Table------#
not True    #False    #
not False   #True     #
#---------------------#

#AND Truth Table-------------#
True  and True     #True     #
True  and False    #False    #
False and True     #False    #
False and False    #False    #
#----------print( a and b ) # False

#OR Truth Table--------------#
True  or True    #True       #
True  or False   #True       #
False or True    #True       #
False or False   #False      #
#----------------------------#

#===============================================================================================================================#
"> Combining Operators and De Morgan's Laws "

#Things can get confusing when combining  operators, so use parenthesis () to help
#PAY ATTENTION TO OPERATOR PRECEDENCE 
a = 1; b = 2; c = 3

print(c < b and b < a or c > a and a > b) #what is going on?!?

print( (c < b and b < a) or (c > a and a > b) )


"De Morgan's Laws"
''' a set of fundamental principles in logic that describe the relationship between 
negation (logical NOT) and conjunction (logical AND), as well as negation 
and disjunction (logical OR). '''

a = True or False
b = True or False

#Think Distributive Property from Math Class
#De Morgan's Laws----------------------------#
not(a and b) == (not a or not b)  # True     #
not(a or b)  == (not a and not b) # True     #
#--------------------------------------------#

#DON'T MAKE THIS ERROR-----------------------#
not(a and b) == (not a and not b) # False    #
not(a or b)  == (not a or not b)  # False    #
#--------------------------------------------#

#===============================================================================================================================#
'> Built-in Operation Function Calls'

# abs(x)
abs(-10) #10
# Returns the absolute value of x. 


# max(iterable, *, key, default) *: separates the positional arguments from the keyword-only arguments that follow.
max(3, 7, 2, 10) #10
# Returns the largest item in an iterable or the largest of two or more arguments.


# min(iterable, *, key, default) *: separates the positional arguments from the keyword-only arguments that follow.
min(3, 7, 2, 10) # 2
# Returns the smallest item in an iterable or the smallest of two or more arguments.


# sum(iterable, /, start=0)
sum([1, 2, 3, 4, 5]) # 15
# Sums the items of an iterable from left to right and returns the total.


# pow(x, y, z=None, /)
pow(2, 3) # 8
# Raises x to the power of y, optionally modulo z.


# round(number, ndigits)
round(3.14159, 2) # 3.14
# Rounds a floating-point number to a specified number of decimal digits.


# divmod(a, b)
divmod(10, 3) # (3,1)
# Returns a tuple containing the quotient and remainder of the division of a by b.

# complex([real,imag)
complex(1, 2) # 1 + 2j
# Creates a complex number.
#complex numbers are a built-in data type used to represent numbers in the form of a + bj, 
#where a and b are real numbers, and j represents the imaginary unit (√(-1)).


# round(x, n)
round(3.7) # 4
# Rounds a number to the nearest integer.


# all(iterable)
all([True, True, False]) #False
# Returns True if all elements of the iterable are true (or if the iterable is empty).


# any(iterable)
any([True, True, False]) #True
# Returns True if any element of the iterable is true. If the iterable is empty, returns False.

#===============================================================================================================================#
'''Bitwise Operations'''
#Bitwise operations work on individual bits within data.
#Order of operations for Bitwise Operators is Not, Shifts, And, Xor, Or (NSAXO)

'''
  Bitwise NOT (~) #opposite
  Bitwise Shift (<<) Left | Right (>>)
  Bitwise AND (&) #both
  Bitwise XOR (^) #only one
  Bitwise OR (|)  #at least one
'''

'''
  Binary Data Representation: Two's complement notation.
    Integers use as many bits as they need in memory

    In two's complement representation:
      Positive integers have a leading 0 bit.
      Negative integers have a leading 1 bit.

      
    Positive Integers: conceptually infinite leading 0s
      ...01 --> 1
      ...000000000000000000000001
    Negative Integers: conceptually infinite leading 1s
      ....1 --> -1
      ....11111111111111111111111
'''

#in bits
true = 1
false = 0

'Bitwise NOT (~) #opposite'
'flips all the bits in a binary number, changing each 0 to 1 and each 1 to 0.'
x = 3
print( bin(x)  ) # 0b11  --> ...011
print( bin(~x) ) #-0b100 --> ...100

'Bitwise Shift (<<) Left | Right (>>)'
'moves all the bits in a number by a specified number of positions.'
#Left Shift (x * 2**shift amount)
x = 1 #0b1
print( x << 3) #8 --> 0b1000
#               0b 0 0 0 1 --> 0b 1 0 0 0
#shift left 3      3 2 1 0

#Right Shift (x / 2** shift amount)
x = 255 #0b10000000
print( x >> 7) # 1 --> 0b1
#                0b 1 0 0 0 0 0 0 0 --> 0b 1
# shift right 7     0 1 2 3 4 5 6 7

'Bitwise AND (&) #both'
'takes two numbers and performs a logical AND operation on each pair of corresponding bits.'
#The resultant bit is 1 if both bits are 1
x = 12         # 0b1100 
y = 10         # 0b1010 
print( x & y ) # 0b1000 --> 8

'Bitwise XOR (^) #only one'
'takes two numbers and performs a logical XOR operation on each pair of corresponding bits.'
#The resultant bit is 1 if only one bit is 1
x = 12         # 0b1100 
y = 10         # 0b1010 
print( x ^ y ) # 0b0110 --> 6

'Bitwise OR (|)  #at least one'
' takes two numbers and performs a logical OR operation on each pair of corresponding bits'
#The resultant bit is 1 if at least on bit is 1
x = 12         # 0b1100 
y = 10         # 0b1010 
print( x | y ) # 0b1110 --> 14


'Truth tables show how logical operators are evaluated'
#NOT Truth Table Bits-#
not 1   #0            #
not 0   #1            #
#---------------------#

#AND Truth Table Bits-#
1 and 1  #1           #
1 and 0  #0           #
0 and 1  #0           #
0 and 0  #0           #
#---------------------#


#XOR (^) Truth Table Bits-#
1 ^ 1   #0                #
1 ^ 0   #1                #
0 ^ 1   #1                #
0 ^ 0   #0                #
#-------------------------#

#OR Truth Table Bits-#
1 or 1  #1           #
1 or 0  #1           #
0 or 1  #1           #
0 or 0  #0           #
#--------------------#

#===============================================================================================================================#
'> Complete Operator Precedence'
'''
  +-------------+---------------------------------+
  | Operators   | Description                     |
  +-------------+---------------------------------+
  | ()          | Parentheses                     |
  | **          | Exponentiation                  |
  | +x -x ~x    | Unary plus, unary minus,        |
  |             | and bitwise NOT                 |
  | * / // %    | Multiplication, division,       |
  |             | floor division, and modulus     |
  | + -         | Addition and subtraction        |
  | << >>       | Bitwise left and right shifts   |
  | &           | Bitwise AND                     |
  | ^           | Bitwise XOR                     |
  | |           | Bitwise OR                      |
  | == != > >=  | Comparisons                     |
  | < <= is     |                                 |
  | is not      | Identity                        |
  | in not in   | Membership operators            |
  | not         | Logical NOT                     |
  | and         | Logical AND                     |
  | or          | Logical OR                      |
  +-------------+---------------------------------+
  Operations at the same level proceed from left to right
'''




#===============================================================================================================================#
'Appendix'

'Bitwise NOT'
bitwise_NOT = []

for x in range(128):
  x_bin = bin(x)
  bin_not = bin(~x)
  int_not = int(bin_not,2)
  bitwise_NOT.append((x, x_bin, bin_not, int_not ))

print(str(bitwise_NOT).replace("),","),\n"))

[(0,  '0b0', '-0b1', -1),
 (1,  '0b1', '-0b10', -2),
 (2,  '0b10', '-0b11', -3),
 (3,  '0b11', '-0b100', -4),
 (4,  '0b100', '-0b101', -5),
 (5,  '0b101', '-0b110', -6),
 (6,  '0b110', '-0b111', -7),
 (7,  '0b111', '-0b1000', -8),
 (8,  '0b1000', '-0b1001', -9),
 (9,  '0b1001', '-0b1010', -10),
 (10, '0b1010', '-0b1011', -11),

 (11, '0b1011', '-0b1100', -12),
 (12, '0b1100', '-0b1101', -13),
 (13, '0b1101', '-0b1110', -14),
 (14, '0b1110', '-0b1111', -15),
 (15, '0b1111', '-0b10000', -16),
 (16, '0b10000', '-0b10001', -17),
 (17, '0b10001', '-0b10010', -18),
 (18, '0b10010', '-0b10011', -19),
 (19, '0b10011', '-0b10100', -20),
 (20, '0b10100', '-0b10101', -21),

 (21, '0b10101', '-0b10110', -22),
 (22, '0b10110', '-0b10111', -23),
 (23, '0b10111', '-0b11000', -24),
 (24, '0b11000', '-0b11001', -25),
 (25, '0b11001', '-0b11010', -26),
 (26, '0b11010', '-0b11011', -27),
 (27, '0b11011', '-0b11100', -28),
 (28, '0b11100', '-0b11101', -29),
 (29, '0b11101', '-0b11110', -30),
 (30, '0b11110', '-0b11111', -31),

 (31, '0b11111', '-0b100000', -32),
 (32, '0b100000', '-0b100001', -33),
 (33, '0b100001', '-0b100010', -34),
 (34, '0b100010', '-0b100011', -35),
 (35, '0b100011', '-0b100100', -36),
 (36, '0b100100', '-0b100101', -37),
 (37, '0b100101', '-0b100110', -38),
 (38, '0b100110', '-0b100111', -39),
 (39, '0b100111', '-0b101000', -40),
 (40, '0b101000', '-0b101001', -41),

 (41, '0b101001', '-0b101010', -42),
 (42, '0b101010', '-0b101011', -43),
 (43, '0b101011', '-0b101100', -44),
 (44, '0b101100', '-0b101101', -45),
 (45, '0b101101', '-0b101110', -46),
 (46, '0b101110', '-0b101111', -47),
 (47, '0b101111', '-0b110000', -48),
 (48, '0b110000', '-0b110001', -49),
 (49, '0b110001', '-0b110010', -50),
 (50, '0b110010', '-0b110011', -51),

 (51, '0b110011', '-0b110100', -52),
 (52, '0b110100', '-0b110101', -53),
 (53, '0b110101', '-0b110110', -54),
 (54, '0b110110', '-0b110111', -55),
 (55, '0b110111', '-0b111000', -56),
 (56, '0b111000', '-0b111001', -57),
 (57, '0b111001', '-0b111010', -58),
 (58, '0b111010', '-0b111011', -59),
 (59, '0b111011', '-0b111100', -60),
 (60, '0b111100', '-0b111101', -61),

 (61, '0b111101', '-0b111110', -62),
 (62, '0b111110', '-0b111111', -63),
 (63, '0b111111', '-0b1000000', -64),
 (64, '0b1000000', '-0b1000001', -65),
 (65, '0b1000001', '-0b1000010', -66),
 (66, '0b1000010', '-0b1000011', -67),
 (67, '0b1000011', '-0b1000100', -68),
 (68, '0b1000100', '-0b1000101', -69),
 (69, '0b1000101', '-0b1000110', -70),
 (70, '0b1000110', '-0b1000111', -71),

 (71, '0b1000111', '-0b1001000', -72),
 (72, '0b1001000', '-0b1001001', -73),
 (73, '0b1001001', '-0b1001010', -74),
 (74, '0b1001010', '-0b1001011', -75),
 (75, '0b1001011', '-0b1001100', -76),
 (76, '0b1001100', '-0b1001101', -77),
 (77, '0b1001101', '-0b1001110', -78),
 (78, '0b1001110', '-0b1001111', -79),
 (79, '0b1001111', '-0b1010000', -80),
 (80, '0b1010000', '-0b1010001', -81),

 (81, '0b1010001', '-0b1010010', -82),
 (82, '0b1010010', '-0b1010011', -83),
 (83, '0b1010011', '-0b1010100', -84),
 (84, '0b1010100', '-0b1010101', -85),
 (85, '0b1010101', '-0b1010110', -86),
 (86, '0b1010110', '-0b1010111', -87),
 (87, '0b1010111', '-0b1011000', -88),
 (88, '0b1011000', '-0b1011001', -89),
 (89, '0b1011001', '-0b1011010', -90),
 (90, '0b1011010', '-0b1011011', -91),

 (91, '0b1011011', '-0b1011100', -92),
 (92, '0b1011100', '-0b1011101', -93),
 (93, '0b1011101', '-0b1011110', -94),
 (94, '0b1011110', '-0b1011111', -95),
 (95, '0b1011111', '-0b1100000', -96),
 (96, '0b1100000', '-0b1100001', -97),
 (97, '0b1100001', '-0b1100010', -98),
 (98, '0b1100010', '-0b1100011', -99),
 (99, '0b1100011', '-0b1100100', -100),
 (100, '0b1100100', '-0b1100101', -101),

 (101, '0b1100101', '-0b1100110', -102),
 (102, '0b1100110', '-0b1100111', -103),
 (103, '0b1100111', '-0b1101000', -104),
 (104, '0b1101000', '-0b1101001', -105),
 (105, '0b1101001', '-0b1101010', -106),
 (106, '0b1101010', '-0b1101011', -107),
 (107, '0b1101011', '-0b1101100', -108),
 (108, '0b1101100', '-0b1101101', -109),
 (109, '0b1101101', '-0b1101110', -110),
 (110, '0b1101110', '-0b1101111', -111),

 (111, '0b1101111', '-0b1110000', -112),
 (112, '0b1110000', '-0b1110001', -113),
 (113, '0b1110001', '-0b1110010', -114),
 (114, '0b1110010', '-0b1110011', -115),
 (115, '0b1110011', '-0b1110100', -116),
 (116, '0b1110100', '-0b1110101', -117),
 (117, '0b1110101', '-0b1110110', -118),
 (118, '0b1110110', '-0b1110111', -119),
 (119, '0b1110111', '-0b1111000', -120),
 (120, '0b1111000', '-0b1111001', -121),

 (121, '0b1111001', '-0b1111010', -122),
 (122, '0b1111010', '-0b1111011', -123),
 (123, '0b1111011', '-0b1111100', -124),
 (124, '0b1111100', '-0b1111101', -125),
 (125, '0b1111101', '-0b1111110', -126),
 (126, '0b1111110', '-0b1111111', -127),
 (127, '0b1111111', '-0b10000000', -128)]

'Bitwise Shift (<<) Left | Right (>>)'
def create_shift_table(number, shift):
    """
    Creates a table that shows the results of left and right bit shifts for integers.

    Args:
        number (int): The maximum number to include in the table.
        shift (int): The number of positions to shift left or right.

    Returns:
        list: A list of tuples representing the shift table, each tuple containing:
            - The original number
            - Its binary representation
            - The result of left shifting the number by the given shift
            - The binary representation of the left shifted result
            - The result of right shifting the number by the given shift
            - The binary representation of the right shifted result

    Example:
        create_shift_table(5, 2) returns:
        [
            ('number', 'binary', 'left_int', 'left_bin', 'right_int', 'right_bin'),
            (0, '0b0', 0, '0b0', 0, '0b0'),
            (1, '0b1', 4, '0b100', 0, '0b0'),
            (2, '0b10', 8, '0b1000', 0, '0b0'),
            (3, '0b11', 12, '0b1100', 0, '0b0'),
            (4, '0b100', 16, '0b10000', 1, '0b1'),
            (5, '0b101', 20, '0b10100', 1, '0b1')
        ]
    """
    shifts = [("number", "binary", 'left_int', 'left_bin', 'right_int', 'right_bin')]
    for x in range(number):
        binary = bin(x)
        left_int = x << shift
        left_bin = bin(left_int)
        right_int = x >> shift
        right_bin = bin(right_int)
        shifts.append((x, binary, left_int, left_bin, right_int, right_bin))

    return shifts