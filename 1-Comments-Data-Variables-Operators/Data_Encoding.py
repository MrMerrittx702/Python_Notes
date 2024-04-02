#===============================================================================================================================#
'''Data_Encoding in Python'''
#===============================================================================================================================#
'''
Covered in this file:
> Convert to Integer: int()
> Convert to Binary: bin()
> Convert to Hexadecimal: hex()
> Convert to String: str()
> Convert to Character: chr()
> Convert to Ordinal: ord()
> Convert to Octal: oct()
> Convert to List: list()
> Convert to Tuple: tuple()
> Convert to Set: set()
'''

#===============================================================================================================================#
'> Convert to Integer: int()'

#From float to integer
int(2.71) #2
#the decimal is truncated not rounded


#From number string to integer
int("97") # 97

#From binary to decimal integer
int(0b1100001) or int("1100001",2) #returns: 97


#From hexadecimal to decimal integer
int(0x61) or int("61",16) #returns: 97 

#===============================================================================================================================#
'> Convert to Binary: bin()'
# 0b is used to indicate binary values

#From decimal to binary
bin(97) #returns binary: 0b1100001  

#From hex to binary
bin(0x61) #returns binary: 0b1100001   

#From octal to binary
bin(0o141) #returns binary: 0b1100001  

#From character to binary
#bin("a") #TypeError: 'str' object cannot be interpreted as an integer
bin(ord("a")) #returns binary: 0b1100001 
#use the ord(str) call to convert to decimal first


#===============================================================================================================================#
'> Convert to Hexadecimal: hex()'
#0x is used to indicate hex values


#From decimal to hex
hex(97) #returns hex: 0x61

#From binary to hex
hex(0b1100001) #returns hex: 0x61

#From octal to hex
hex(0o141) #returns hex: 0x61

#From character to hex
#hex("a") #TypeError: 'str' object cannot be interpreted as an integer
hex(ord("a")) #returns hex: 0x61
#use the ord(str) call to convert to decimal first


#===============================================================================================================================#
'> Convert to String: str()'

#converts the provide value to a string
str(97) #returns string: 97

#===============================================================================================================================#
'> Convert to Character: chr()'
#chr() converts to a character

#From decimal to character
chr(97) #returns character: a

#From binary to character
chr(0b1100001) #returns character: a

#From hex to character
chr(0x61) #returns character: a

#From octal to character
chr(0o141) #returns character: a


#===============================================================================================================================#
'> Convert to Ordinal: ord()'
#converts characters into decimal representation

# From character to decimal
ord("a") #returns decimal: 97


#===============================================================================================================================#
'> Convert to Octal: oct()'

#From decimal to octal
oct(97) #returns octal: 0o141

#From binary to octal
oct(0b1100001) #returns octal: 0o141

#From hex to octal
oct(0x61) #returns octal: 0o141

#From character to octal
#oct"a") #TypeError: 'str' object cannot be interpreted as an integer
oct(ord("a")) #returns octal: 0o141
#use the ord(str) call to convert to decimal first

#===============================================================================================================================#
'> Convert to List: list()'

#From tuple to list
list((1,2,3,4,5)) # returns list: [1,2,3,4,5]


#From set to list
list({1,2,3,4,5}) #returns list: [1,2,3,4,5]


#===============================================================================================================================#
'> Convert to Tuple: tuple()'

#From list to tuple
tuple([1,2,3,4,5]) # returns tuple: (1,2,3,4,5)

#From set to tuple
tuple({1,2,3,4,5}) #returns tuple: (1,2,3,4,5)

#===============================================================================================================================#
'> Convert to Set: set()'

#From list to set
set([1,2,2,3,3,4,4,4,5])#returns set: {1,2,3,4,5}

#From tuple to set
set((1,2,2,3,4,5,5))#returns set: {1,2,3,4,5}















# #you will need to change to one of the following

# print(chr(int("101010", 2))) #converts from binary to a character(ASCII)

# print(chr(int("0x2a", 16))) #converts from hexadecimal to a character(ASCII)


# #Converting Data Types in Python

# #str to int
# a = "400" 
# print(a)
# print(type(a))

# a = int(a)# use the 'int' function to convert a value to an integer
# print(a)
# print(type(a))
# print("\n")


# #int to str
# b = 500
# print(b)
# print(type(b))

# b = str(b)# use the 'str' function to convert a value to a string
# print(b)
# print(type(b))
# print("\n")


# #float to int
# c = 3.14
# print(c)
# print(type(c))

# c = int(c)
# print(c)#integers do not include decimal points and do not round. 
# print(type(c))
# print("\n")


# #Convert list to tuple
# a_list = [7,8,9]
# print(a_list)
# print(type(a_list))
# a_tuple = tuple(a_list)# use the 'tuple' function to convert a list to a tuple
# print(a_tuple)
# print(type(a_tuple))
# print("\n")

