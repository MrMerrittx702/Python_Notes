#===============================================================================================================================#
'''Python Characters and Strings'''
#===============================================================================================================================#

'''
Covered in this file:
> Characters Defined
> Special Characters
> Converting Characters
> Strings Defined
> String Concatenation and Duplication
> String Comparision
> String Indexing
> Substrings: Slicing
> Built-in String Function Calls
> Built-in String Method Calls
'''
#===============================================================================================================================#
'> Characters Defined'
#basic unit of information that represents a letter, number, symbol, or control code

character = 'a'
character = '2'
character = ' ' # even a space is a character
character = '@'

'See ASCII table below'

'''
| Character | Decimal | Hexadecimal |  Binary  | Octal |
|           |   32    |    0x20     | 0b100000 | 0o40  | This is the space character
|     !     |   33    |    0x21     | 0b100001 | 0o41  |
|     "     |   34    |    0x22     | 0b100010 | 0o42  |
|     #     |   35    |    0x23     | 0b100011 | 0o43  |
|     $     |   36    |    0x24     | 0b100100 | 0o44  |
|     %     |   37    |    0x25     | 0b100101 | 0o45  |
|     &     |   38    |    0x26     | 0b100110 | 0o46  |
|     '     |   39    |    0x27     | 0b100111 | 0o47  |
|     (     |   40    |    0x28     | 0b101000 | 0o50  |
|     )     |   41    |    0x29     | 0b101001 | 0o51  |
|     *     |   42    |    0x2a     | 0b101010 | 0o52  |
|     +     |   43    |    0x2b     | 0b101011 | 0o53  |
|     ,     |   44    |    0x2c     | 0b101100 | 0o54  |
|     -     |   45    |    0x2d     | 0b101101 | 0o55  |
|     .     |   46    |    0x2e     | 0b101110 | 0o56  |
|     /     |   47    |    0x2f     | 0b101111 | 0o57  |

| Character | Decimal | Hexadecimal |  Binary  | Octal |
|     0     |   48    |    0x30     | 0b110000 | 0o60  |
|     1     |   49    |    0x31     | 0b110001 | 0o61  |
|     2     |   50    |    0x32     | 0b110010 | 0o62  |
|     3     |   51    |    0x33     | 0b110011 | 0o63  |
|     4     |   52    |    0x34     | 0b110100 | 0o64  |
|     5     |   53    |    0x35     | 0b110101 | 0o65  |
|     6     |   54    |    0x36     | 0b110110 | 0o66  |
|     7     |   55    |    0x37     | 0b110111 | 0o67  |
|     8     |   56    |    0x38     | 0b111000 | 0o70  |
|     9     |   57    |    0x39     | 0b111001 | 0o71  |

| Character | Decimal | Hexadecimal |  Binary  | Octal |
|     :     |   58    |    0x3a     | 0b111010 | 0o72  |
|     ;     |   59    |    0x3b     | 0b111011 | 0o73  |
|     <     |   60    |    0x3c     | 0b111100 | 0o74  |
|     =     |   61    |    0x3d     | 0b111101 | 0o75  |
|     >     |   62    |    0x3e     | 0b111110 | 0o76  |
|     ?     |   63    |    0x3f     | 0b111111 | 0o77  |
|     @     |   64    |    0x40     |0b1000000 | 0o100 |

| Character | Decimal | Hexadecimal |  Binary  | Octal |
|     a     |   97    |    0x61     |0b1100001 | 0o141 |
|     b     |   98    |    0x62     |0b1100010 | 0o142 |
|     c     |   99    |    0x63     |0b1100011 | 0o143 |
|     d     |   100   |    0x64     |0b1100100 | 0o144 |
|     e     |   101   |    0x65     |0b1100101 | 0o145 |
|     f     |   102   |    0x66     |0b1100110 | 0o146 |
|     g     |   103   |    0x67     |0b1100111 | 0o147 |
|     h     |   104   |    0x68     |0b1101000 | 0o150 |
|     i     |   105   |    0x69     |0b1101001 | 0o151 |
|     j     |   106   |    0x6a     |0b1101010 | 0o152 |
|     k     |   107   |    0x6b     |0b1101011 | 0o153 |
|     l     |   108   |    0x6c     |0b1101100 | 0o154 |
|     m     |   109   |    0x6d     |0b1101101 | 0o155 |
|     n     |   110   |    0x6e     |0b1101110 | 0o156 |
|     o     |   111   |    0x6f     |0b1101111 | 0o157 |
|     p     |   112   |    0x70     |0b1110000 | 0o160 |
|     q     |   113   |    0x71     |0b1110001 | 0o161 |
|     r     |   114   |    0x72     |0b1110010 | 0o162 |
|     s     |   115   |    0x73     |0b1110011 | 0o163 |
|     t     |   116   |    0x74     |0b1110100 | 0o164 |
|     u     |   117   |    0x75     |0b1110101 | 0o165 |
|     v     |   118   |    0x76     |0b1110110 | 0o166 |
|     w     |   119   |    0x77     |0b1110111 | 0o167 |
|     x     |   120   |    0x78     |0b1111000 | 0o170 |
|     y     |   121   |    0x79     |0b1111001 | 0o171 |
|     z     |   122   |    0x7a     |0b1111010 | 0o172 |

| Character | Decimal | Hexadecimal |  Binary  | Octal |
|     [     |   91    |    0x5b     |0b1011011 | 0o133 |
|     \     |   92    |    0x5c     |0b1011100 | 0o134 |
|     ]     |   93    |    0x5d     |0b1011101 | 0o135 |
|     ^     |   94    |    0x5e     |0b1011110 | 0o136 |
|     _     |   95    |    0x5f     |0b1011111 | 0o137 |
|     `     |   96    |    0x60     |0b1100000 | 0o140 |

| Character | Decimal | Hexadecimal |  Binary  | Octal |
|     A     |   65    |    0x41     |0b1000001 | 0o101 |
|     B     |   66    |    0x42     |0b1000010 | 0o102 |
|     C     |   67    |    0x43     |0b1000011 | 0o103 |
|     D     |   68    |    0x44     |0b1000100 | 0o104 |
|     E     |   69    |    0x45     |0b1000101 | 0o105 |
|     F     |   70    |    0x46     |0b1000110 | 0o106 |
|     G     |   71    |    0x47     |0b1000111 | 0o107 |
|     H     |   72    |    0x48     |0b1001000 | 0o110 |
|     I     |   73    |    0x49     |0b1001001 | 0o111 |
|     J     |   74    |    0x4a     |0b1001010 | 0o112 |
|     K     |   75    |    0x4b     |0b1001011 | 0o113 |
|     L     |   76    |    0x4c     |0b1001100 | 0o114 |
|     M     |   77    |    0x4d     |0b1001101 | 0o115 |
|     N     |   78    |    0x4e     |0b1001110 | 0o116 |
|     O     |   79    |    0x4f     |0b1001111 | 0o117 |
|     P     |   80    |    0x50     |0b1010000 | 0o120 |
|     Q     |   81    |    0x51     |0b1010001 | 0o121 |
|     R     |   82    |    0x52     |0b1010010 | 0o122 |
|     S     |   83    |    0x53     |0b1010011 | 0o123 |
|     T     |   84    |    0x54     |0b1010100 | 0o124 |
|     U     |   85    |    0x55     |0b1010101 | 0o125 |
|     V     |   86    |    0x56     |0b1010110 | 0o126 |
|     W     |   87    |    0x57     |0b1010111 | 0o127 |
|     X     |   88    |    0x58     |0b1011000 | 0o130 |
|     Y     |   89    |    0x59     |0b1011001 | 0o131 |
|     Z     |   90    |    0x5a     |0b1011010 | 0o132 |

| Character | Decimal | Hexadecimal |  Binary  | Octal |
|     {     |   123   |    0x7b     |0b1111011 | 0o173 |
|     |     |   124   |    0x7c     |0b1111100 | 0o174 |
|     }     |   125   |    0x7d     |0b1111101 | 0o175 |
|     ~     |   126   |    0x7e     |0b1111110 | 0o176 |

'''
def unicode_lookup(character, print_table=False):
    """
    Look up Unicode information for a given character.

    Args:
        character (str): The character to look up Unicode information for.
        print_table (bool, optional): If True, prints the entire Unicode table. Defaults to False.

    Returns:
        tuple: A tuple containing Unicode information for the input character.
               The tuple structure is (Unicode_code_point, Decimal, Hexadecimal, Binary, Octal).

    Example:
        >> unicode_lookup('A')
        ('U+0041', 65, '0x41', '0b1000001', '0o101')
    """
    unicode_table = {}
    for decimal in range(0, 128):
        unicode_table[chr(decimal)] = (
            f"U+{decimal:x}",
            decimal,
            hex(decimal),
            bin(decimal),
            oct(decimal),
        )

    # Optionally print the Unicode table
    if print_table:
        print(str(unicode_table).replace("),", "),\n"))

    # Print the Unicode information for the input character
    print(unicode_table[character])

#===============================================================================================================================#
'> Special Characters'

#use the back slash (\) as an escape character
'''
  "escaping a character" 
  refers to the use of special sequences 
  or combinations of characters to represent 
  characters that are difficult or impossible 
  to represent directly. 
'''

# \n  newline character, used to insert a new line.
print( "First line\nSecond line")
#                 ^ 
# First line 
# Second line


# \t tab character, used to insert horizontal spacing.
print( "First\tSecond\tThird" )
#            ^       ^
# First   Second  Third


# \\ single backslash character
print( "C:\\Users\\Username\\Documents" )
#         ^      ^         ^
# C:\Users\Username\Documents 


# \' single quote 
print('It\'s an escaped character!')
#        ^
# It's an escaped character!


# \" double quote 
print("\"Look out for double\"")
#      ^                    ^
# "Look out for double"

#\r carriage return character, used to return the cursor to the beginning of the line.
print("123\rabc")
#         ^
# abc


#\b backspace character, used to delete the preceding character.
print("abc\bd")
#         ^
# abd


#\ form feed character, used to advance to the next page or form
print("Page 1\fPage 2")
#            ^


#===============================================================================================================================#
'> Strings Defined'
'>> Strings are immutable (cannot be changed) sequences of characters.'
'>> If a new string is needed you must create a new one.'

#a string is a sequence of characters and is surrounded by quotation marks
"Hello World" or 'Hello World'

#strings can be stored by a variable
str_ = "String of Text"

#String literals can span multiple lines and automatically include the newline character at the end
#use \ to remove the automatic newline character at the end(does not work for the first line).
print("""  
line 1\
line 2\
line 3\
""") 

#more technically strings are objects of the 'str' class in python
print(type("My String")) # <class 'str'>

#===============================================================================================================================#
'> Strings Concatenation and Duplication'
#concatenate means to join

#String literals next to each other are automatically concatenated
#useful for breaking up long strings
"Python is an easy to learn, powerful programming language."
"It has efficient high-level data structures and a simple but "
"effective approach to object-oriented programming."
"Python’s elegant syntax and dynamic typing, together with its interpreted nature, "
"make it an ideal language for scripting and rapid application development in many areas"
" on most platforms."


#to join two strings use +
"Hello" + " World" # Hello World
#          ^ don't forget the space

#to duplicate strings use *
"a" * 3 # aaa


#===============================================================================================================================#
'> Strings Comparision'

'''
Lexicographical Comparison: 
  compares strings character by character, based on their Unicode values.
  can be used to compare characters and strings alphabetically 

  Compare the first character of each string. 
  If they are equal, move on to the next character there are unequal characters 
    or reaching the end of one or both strings.

'''

#compare equality with == 
"Hello" == "Hello" # True
"hello" == "Hello" # False

str1 = "apple"; str2 = "banana"

str1 == str2  # False
str1 != str2  # True
str1 < str2   # True (lexicographically smaller)
str1 > str2   # False

'''
Length Comparison: 
If the strings have different lengths but the shorter string is identical to the longer one up to the length of the shorter string, Python considers the shorter string less than the longer one. 
For example, "abc" is less than "abcd".
''' 
str3 = "abc"
str4 = "abcd"

str3 < str4 # True (even though 'abc' is shorter)

'You can generate a unicode dictionary with the code below'
def gen_unicode_table(start = 1, stop = 1024):
  table = {"Character" : ("Unicode", "Decimal")}
  for num in range(start,stop+1):
    table[chr(num)] =("U+{num:04x}",num)

  print(str(table).replace("),","),\n"))

gen_unicode_table()

#===============================================================================================================================#
'> String Indexing'
' > are a sequence or string of characters.'
' > can be thought of as a list of characters.'
' > strings can be indexed like lists'
' > each character is given an index starting from 0.'
' > do not forget about spaces.'


'''
String -->  P   r   o  g  r  a  m  m  i  n  g
Index  -->  0   1   2  3  4  5  6  7  8  9  10
Reverse--> -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
'''

word = "Programming"

#accessing a single character of a string
print( word[0] )# P
print( word[1] )# r
print( word[2] )# o

print( word[-1] )# g
print( word[-2] )# n
print( word[-3] )# i


#===============================================================================================================================#
'> String Slicing'

word = "Programming"

'''
String -->  P   r   o  g  r  a  m  m  i  n  g
Index  -->  0   1   2  3  4  5  6  7  8  9  10
Reverse--> -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
'''

#slicing returns a substring (or a part of the original string)
#list[start_index:stop_index] Note: the stop_index is not included
print(word[:5])    # Progr
print(word[4:])    # ramming
print(word[0:7])   # Program
print(word[3:11])  # gramming
print(word[-5:-1]) # mmin
#note the stop_index is not included in the slice

#python strings are immutable (cannot be changed)
#you can create a new string but cannot change the old one
#word[0] = "J" results in error

#===============================================================================================================================#
'> Built in String Function Calls'

#len(x)  returns the number of characters in the string (note: spaces count as characters)
len(word) # 11
len(word)-1 # 10 --> the last index of the word

# Returns the maximum character (according to Unicode code point) in a string.
max(word) # r

#  Returns the minimum character (according to Unicode code point) in a string.
min(word) # P


#===============================================================================================================================#
'> Built in String Method Calls'

'''
  Methods are functions defined by a class
    Methods are typically called using an object or class and dot (.) syntax
      object.method(parameters) --> for methods which require objects
        or
      class.method(paramters) --> for methods which do not require objects
'''

#To see what methods you can call on an object use dir(object)
#To see more information on a specific method use help(object.method)

string = "hello world"

#string.capitalize()  No parameters
string.capitalize()    
# Returns a copy of the string with the first character capitalized

#string.casefold()  No parameters
string.casefold()      
# Returns a casefolded copy of the string, suitable for case-insensitive comparisons

#string.center(width, fillchar) 'width' (required): the width of the centered string, 'fillchar' (optional): character used for padding
string.center()        
# Returns a centered string of a specified width

# string.count(substring, start, end) 'substring' (required): the substring to count, 'start' (optional): starting index for the search, 'end' (optional): ending index for the search
string.count()         
# Returns the number of occurrences of a substring in the string

# string.encode(encoding="utf-8", errors="strict")  'encoding' (optional): encoding type, 'errors' (optional): how to handle encoding errors
string.encode()        
# Returns the encoded version of the string


# string.endswith(suffix, start, end) 'suffix' (required): suffix to check, 'start' (optional): start index for the slice, 'end' (optional): end index for the slice
string.endswith()      
# Checks if the string ends with a specified suffix


# string.expandtabs(tabsize=8) 'tabsize' (optional): size of the tab character
string.expandtabs()    
# Expands tabs in the string to spaces


# string.find(substring, start, end) 'substring' (required): substring to search, 'start' (optional): start index for the search, 'end' (optional): end index for the search
string.find()          
# Returns the lowest index of a substring in the string


# string.format(*args, **kwargs) *args (optional): positional arguments, **kwargs (optional): keyword arguments
string.format()        
# Formats the string


# string.format_map(mapping) 'mapping' (required): mapping object containing the formatting parameters
string.format_map()    
# Formats the string using a mapping


# string.index(substring, start, end) 'substring' (required): substring to search, 'start' (optional): start index for the search, 'end' (optional): end index for the search
string.index()         
# Returns the lowest index of a substring in the string


# string.isalnum() No parameters
string.isalnum()       
# Checks if all characters in the string are alphanumeric

# string.isalpha() No parameters
string.isalpha()       
# Checks if all characters in the string are alphabetic


# string.isascii() No parameters
string.isascii()       
# Checks if the string contains only ASCII characters


# string.isdecimal() No parameters
string.isdecimal()     
# Checks if all characters in the string are decimal


# string.isdigit() No parameters
string.isdigit()       
# Checks if all characters in the string are digits


# string.isidentifier() No parameters
string.isidentifier()  
# Checks if the string is a valid identifier


# string.islower() No parameters
string.islower()       
# Checks if all characters in the string are lowercase


# string.isnumeric() No parameters
string.isnumeric()     
# Checks if all characters in the string are numeric


# string.isprintable() No parameters
string.isprintable()   
# Checks if all characters in the string are printable


# string.isspace() No parameters
string.isspace()       
# Checks if all characters in the string are whitespaces


# string.istitle() No parameters
string.istitle()       
# Checks if the string is titlecased


# string.isupper() No parameters
string.isupper()       
# Checks if all characters in the string are uppercase


# string.join(iterable) 'iterable' (required): iterable of strings to join
string.join()          
# Joins the elements of an iterable to create a string


# string.ljust(width, fillchar) 'width' (required): width of the resulting string, 'fillchar' (optional): character used for padding
string.ljust()         
# Returns a left-justified string of a specified width


# string.lower() No parameters
string.lower()         
# Returns a copy of the string converted to lowercase


# string.lstrip(chars) 'chars' (optional): characters to be stripped from the beginning
string.lstrip()        
# Returns a copy of the string with leading whitespace removed


# string.maketrans(x, y, z)  'x' (required): characters to replace, 'y' (required): corresponding replacement characters, 'z' (optional): characters to delete
string.maketrans()     
# Returns a translation table usable for str.translate()


# string.partition(separator)  'separator' (required): separator to partition the string
string.partition()     
# Splits the string at the first occurrence of a separator


# string.removeprefix(prefix)  'prefix' (required): prefix to remove
string.removeprefix()  
# Removes a prefix from the string


# string.removesuffix(suffix)  'suffix' (required): suffix to remove
string.removesuffix()  
# Removes a suffix from the string


# string.replace(old, new, count)  'old' (required): substring to be replaced, 'new' (required): substring to replace with, 'count' (optional): number of occurrences to replace
string.replace()       
# Returns a copy of the string with occurrences of a substring replaced


# string.rfind(substring, start, end)  'substring' (required): substring to search, 'start' (optional): start index for the search, 'end' (optional): end index for the search
string.rfind()         
# Returns the highest index of a substring in the string


# string.rindex(substring, start, end) 'substring' (required): substring to search, 'start' (optional): start index for the search, 'end' (optional): end index for the search
string.rindex()        
# Returns the highest index of a substring in the string


# string.rjust(width, fillchar)  'width' (required): width of the resulting string, 'fillchar' (optional): character used for padding
string.rjust()         
# Returns a right-justified string of a specified width


# string.rpartition(separator) 'separator' (required): separator to partition the string
string.rpartition()    
# Splits the string at the last occurrence of a separator


# string.rsplit(separator, maxsplit)  'separator' (optional): separator to split the string, 'maxsplit' (optional): maximum number of splits
string.rsplit()        
# Splits the string into a list, starting from the right


# string.splitlines(keepends)  'keepends' (optional): whether to keep the line endings
string.splitlines()    
# Splits the string at line breaks and returns a list of lines


# string.startswith(prefix, start, end)  'prefix' (required): prefix to check, 'start' (optional): start index for the slice, 'end' (optional): end index for the slice
string.startswith()    
# Checks if the string starts with a specified prefix


# string.strip(chars)  'chars' (optional): characters to be stripped from both ends
string.strip()         
# Returns a copy of the string with leading and trailing whitespace removed


# string.swapcase()  No parameters
string.swapcase()      
# Returns a copy of the string with uppercase characters converted to lowercase and vice versa


# string.title() No parameters
string.title()         
# Returns a titlecased version of the string


# string.translate(table) 'table' (required): translation table
string.translate()     
# Returns a copy of the string where each character has been mapped through the given translation table


# string.upper() No parameters
string.upper()         
# Returns a copy of the string converted to uppercase


# string.zfill(width) 'width' (required): width of the resulting string
string.zfill()         
# Returns a copy of the string padded with zeros to a specified width

#===============================================================================================================================#
'> Format Strings: f-strings'
'''
  introduced in Python 3.6,f-strings provide a convenient way to embed expressions 
  inside string literals. 
  They are prefixed with an 'f' or 'F' character and contain expressions enclosed in curly braces {}.
'''

'Inserting variables directly into strings'
name = "Sam"
age = 30
#use f"" and {var} for formated strings
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Sam and I am 30 years old.


'Formating Numbers'

#Integers
n = 1000000000
# _ and , can be used to format larger numbers
f'{n:_}'
f'{n:,}'

#Floats (.nf) to round to n decimal places
n = 1234.56789
f"{n:.0f}" # 1235
f"{n:.1f}" # 1234.6
# with separators
f"{n:_.2f}" # 1_234.57
f"{n:,.3f}" # 1,234.568

#Scientific Notation (e)
n = 602200000000000000000000
print(f'{n:e}') #6.022000e+23
print(f'{n:.3e}') #6.022e+23



'Formating Expressions'
#Printing expressions
a = 2; b = 3
f'{a = }'     # a = 2
f'{b = }'     # b = 3
f'{a + b = }' # a + b = 5

c = 0.1; d = 0.2
f'{c + d = :.1f}' # c + d = 0.3

c = 3.141592665
form = ".2f"
f'{c:form}'  # 3.14


'Padding and Alignment'
var = "x"
#right align(>) and pad to n with spaces
print(f'|{var:>5}|') #|    x|

#left align(<) and pad to n with spaces
print(f'|{var:<5}|') #|x    |

#center align (^) and pad to n with spaces
print(f'|{var:^5}|') #|  x  |

#align and pad to n with character
print(f'|{var:_>5}|') #|____x|
print(f'|{var:#<5}|') #|x####|
print(f'|{var:|^5}|') #|||x|||
print(f'|{var:a^5}|') #|aaxaa|

'Misc'
#removing quotes
name = "Alice"
f'{name = }' # name = 'Alice'
f'{name = !s}' # name = Alice

'Formating Dates and Times'
from datetime import datetime

now = datetime.now() # example: 2024-03-22 18:45:56.313427

#   day (d) month (m) year (y) Hour (H) Minute (M) Second (S)
print(f'{now:%d.%m.%y (%H:%M:%S)}') # 22.03.24 (18:48:33)
print(f'{now:%c}') # Fri Mar 22 18:50:10 2024
print(f'{now:%I%p}') # 06PM

'''
%Y: Year with century as a decimal number (e.g., 2024).
%m: Month as a zero-padded decimal number (e.g., 03 for March).
%B: Full month name (e.g., March).
%b: Abbreviated month name (e.g., Mar).
%A: Full weekday name (e.g., Friday).
%a: Abbreviated weekday name (e.g., Fri).
%H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 18).
%M: Minute as a zero-padded decimal number (e.g., 50).
%S: Second as a zero-padded decimal number (e.g., 10).
%Z: Time zone name (e.g., UTC).
%c: Preferred date and time representation for the current locale.
%d: Day of the month as a zero-padded decimal number (e.g., 22).
%I: Hour (12-hour clock) as a zero-padded decimal number (e.g., 06).
%p: AM/PM indicator (e.g., PM).
'''


#Examples
num = 42
formatted_num = f"{num:03}"
print(formatted_num)  # Output: 042

pi = 3.14159
formatted_pi = f"{pi:.2f}"
print(formatted_pi)  # Output: 3.14

hex_num = 255
formatted_hex = f"{hex_num:08X}"
print(formatted_hex)  # Output: "000000FF"

product = "apple"
price = 1.99
quantity = 5
total_cost = f"The total cost of {quantity} {product}s is ${price * quantity:.2f}."
print(total_cost)  # Output: "The total cost of 5 apples is $9.95."
'''
Conversion Flags
+------+---------------------------------------+
| Flag |               Meaning                 |
+------+---------------------------------------+
| '#'  | The value conversion will use the     |
|      | "alternate form" (where defined below)|
+------+---------------------------------------+
| '0'  | The conversion will be zero padded    |
|      | for numeric values.                   |
+------+---------------------------------------+
| '-'  | The converted value is left adjusted  |
|      | (overrides the '0' conversion if both |
|      | are given).                           |
+------+---------------------------------------+
| ' '  | A blank should be left before a       |
|      | positive number (or empty string)     |
|      | produced by a signed conversion.      |
+------+---------------------------------------+
| '+'  | A sign character ('+' or '-') will    |
|      | precede the conversion (overrides a   |
|      | "space" flag).                        |
+------+---------------------------------------+

+-----------+---------------------------+----------+
| Conversion| Meaning                   | Notes    |
+-----------+---------------------------+----------+
|    'd'    | Signed integer decimal.   |          |
+-----------+---------------------------+----------+
|    'i'    | Signed integer decimal.   |          |
+-----------+---------------------------+----------+
|    'o'    | Signed octal value.       | (1)      |
+-----------+---------------------------+----------+
|    'u'    | Obsolete type – it is     | (6)      |
|           | identical to 'd'.         |          |
+-----------+---------------------------+----------+
|    'x'    | Signed hexadecimal        | (2)      |
|           | (lowercase).              |          |
+-----------+---------------------------+----------+
|    'X'    | Signed hexadecimal        | (2)      |
|           | (uppercase).              |          |
+-----------+---------------------------+----------+
|    'e'    | Floating point exponential| (3)      |
|           | format (lowercase).       |          |
+-----------+---------------------------+----------+
|    'E'    | Floating point exponential| (3)      |
|           | format (uppercase).       |          |
+-----------+---------------------------+----------+
|    'f'    | Floating point decimal    | (3)      |
|           | format.                   |          |
+-----------+---------------------------+----------+
|    'F'    | Floating point decimal    | (3)      |
|           | format.                   |          |
+-----------+---------------------------+----------+
|    'g'    | Floating point format.    | (4)      |
|           | Uses lowercase exponential|          |
|           | format if exponent is less|          |
|           | than -4 or not less than  |          |
|           | precision, decimal format |          |
|           | otherwise.                |          |
+-----------+---------------------------+----------+
|    'G'    | Floating point format.    | (4)      |
|           | Uses uppercase exponential|          |
|           | format if exponent is less|          |
|           | than -4 or not less than  |          |
|           | precision, decimal format |          |
|           | otherwise.                |          |
+-----------+---------------------------+----------+
|    'c'    | Single character          |          |
|           | (accepts integer or       |          |
|           | single character string). |          |
+-----------+---------------------------+----------+
|    'r'    | String converts any       | (5)      |
|           | Python object using repr()|          |
+-----------+---------------------------+----------+
|    's'    | String (converts any      | (5)      |
|           | Python object using str())|          |
+-----------+---------------------------+----------+
|    'a'    | String converts any       | (5)      |
|           | Python object using ascii()|         |
+-----------+---------------------------+----------+
|    '%'    | No argument is converted, |          |
|           | results in a '%' character|          |
|           | in the result.            |          |
+-----------+---------------------------+----------+

1. The alternate form causes a leading octal specifier ('0o') to be inserted before the first digit.

2. The alternate form causes a leading '0x' or '0X' (depending on whether the 'x' or 'X' format was used) to be inserted before the first digit.

3. The alternate form causes the result to always contain a decimal point, even if no digits follow it.
   > The precision determines the number of digits after the decimal point and defaults to 6.

4. The alternate form causes the result to always contain a decimal point, and trailing zeroes are not removed as they would otherwise be.
   > The precision determines the number of significant digits before and after the decimal point and defaults to 6.

5. f precision is N, the output is truncated to N characters.

6. See PEP 237.
'''

#===============================================================================================================================#
'> Raw Strings'
'''
R Raw strings are string literals prefixed with an 'r' or 'R' character. 
  They treat backslashes \ as literal characters, and they are often used 
  for regular expressions, file paths, or any string where backslashes are prevalent 
  and should not be treated as escape characters.
'''

#instead of this
print('C:\\Users\\Username\\Desktop\\Myfolder') # C:\Users\Username\Desktop\Myfolder

#Try this
#r"" for raw strings
print(r'C:\Users\Username\Desktop\Myfolder') # C:\Users\Username\Desktop\Myfolder

#===============================================================================================================================#
'> Bytes Strings'
'''
  Bytes literals, prefixed with a 'b' or 'B' character, represent sequences of bytes. 
  They are used to store binary data such as images, audio files, or any data that 
  is not necessarily text.
'''
b'\x48\x65\x6C\x6C\x6F' #bytes literal

print(b'\x48\x65\x6C\x6C\x6F'.decode()) # Hello
print(b'Hello') # b'Hello'

#Function to display the bytes
def return_bytes(bytes):
  string = r""
  for byte in bytes:
    string += str(hex(byte)).replace("0","\\")

  print(string)
  return(string)


return_bytes(b"hello")



 

























































'''
Extension:
  > f strings

'''


'ASCII table/ UTF-8'

'''


Generated ascii table with the code below

def make_chars(start, end):
   str = ""
   for x in range(start,end+1):
      str+=chr(x)
   return str

def encode(characters):
   print("| Character | Decimal | Hexadecimal |  Binary  | Octal |")

   for char in characters:
      dec_ = ord(char)
      hex_ = str(hex(dec_))
      bin_ = str(bin(dec_))
      oct_ = str(oct(dec_))
      dec_ = str(dec_)
      
      print(f"|     {char}     |",end ="")
      print_spaced(" Decimal ",dec_)
      print_spaced(" Hexadecimal ",hex_)
      print_spaced("  Binary  ",bin_)
      print_spaced(" Octal ",oct_)
      print()

def print_spaced(str, data):
   diff = len(str) - len(data)
   front = diff//2
   back = diff - front
   print((front*" ") + data + (back*" ") + "|",end="")

symbols1 = make_chars(33,47)# !"#$%&'()*+,-./
numbers = "0123456789"
symbols2 = make_chars(58,64)# :;<=>?@
lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
symbols3 = make_chars(91,96)# [\]^_`
upper_alphabet = lower_alphabet.upper() #ABCDEFGHIJKLMNOPQRSTUVWXYZ

symbols4 = make_chars(123,126)# {|}~

ascii_chars = [symbols1,numbers,symbols2,lower_alphabet,symbols3,upper_alphabet,symbols4]
for group in ascii_chars:
   encode(group)
   print()

'''