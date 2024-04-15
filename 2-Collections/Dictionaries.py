#===============================================================================================================================#
'''Python Dictionaries '''
#===============================================================================================================================#

'''
Covered in this video:
> Dictionaries Defined: Key:Value Pairs
> Creating a Dictionary
> Converting Dictionaries
> Accessing Items
> Changing Items
> Dictionary Operations
> Built-in dictionary function calls 
> Built-in dictionary methods calls
> Nested Dictionaries
> Looping through dictionaries
> Unpacking Dictionaries
> Dictionary Comprehension
'''
#===============================================================================================================================#
'> Dictionaries Defined: Key:Value Pairs'
#Dictionaries aka associative arrays
'''
Dictionary is a built-in collection which is ordered**, mutable, and has no duplicate members.
Dictionaries store key-value pairs. 
'''

# dictionaries are defined using curly braces {} 
{"name": "John", "age" :22, "school" : "University of Louisville","good_standing" : True}
# key  : value ,  
#They store key: value pairs. Keys must be an immutable type.


'''
There are four collection data types in the Python programming language:

> List: collection which is ordered and mutable. Allows duplicate members.

> Tuple: collection which is ordered and immutable. Allows duplicate members.

> Set: collection which is unordered, unchangeable*, and unindexed. No duplicate members.

> Dictionary: collection which is ordered** and changeable. No duplicate members.
'''

#===============================================================================================================================#
'> Creating a Dictionary'

#Use a comma separated list of key:value pairs with curly braces
dictionary = {"name": "John", "age" :22, "school" : "University of Louisville","good_standing" : True}

#use the dict(iterable) constructor to build dictionaries from sequences of key-value pairs

dict() #returns empty dictionary {}

#using an iterable with key:value pairs
dict(('name', 'John'),('age', 22),('school', 'University of Louisville'),('good_standing', True)) #{"name": "John", "age" :22, "school" : "University of Louisville","good_standing" : True}

#using keyword arguments
dict(name="John", age=22, school = "University of Louisville", good_standing=True ) # {'name': 'John', 'age': 22, 'school': 'University of Louisville', 'good_standing': True}

numerals = {
  '0': 48, '1': 49, '2': 50, '3': 51, '4': 52,
  '5': 53, '6': 54, '7': 55, '8': 56, '9': 57
}

ucase_alpha = {
  'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 
  'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 
  'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 
  'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 
  'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 
  'Z': 90
}

lcase_alpha = {
  'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 
  'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 
  'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 
  'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116,
  'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121,
  'z': 122
} 



#===============================================================================================================================#
'> Converting Dictionaries'

#Convert a dictionary to a list,tuple, or set of keys
key_list = list(lcase_alpha) #['a', 'b', 'c', 'd', 'e', 'f',...
key_tuple = tuple(lcase_alpha) #('a', 'b', 'c', 'd', 'e', 'f',...
key_set = set(lcase_alpha) #{'a', 'e', 'l', 'y', 'h', 'o',...
#remember that sets are unordered

#===============================================================================================================================#
'> Accessing Items'

#dict[key] or dict.get(key[,default]) returns the value of key. Note: [] indicates optional
ucase_alpha["A"]
ucase_alpha.get("A") 

# dict.keys() returns a list of keys
ucase_alpha.keys()

#dict.values() returns a list of values
ucase_alpha.values()

#dict.items() returns a list of tuples containing key value pairs
ucase_alpha.items() 

#===============================================================================================================================#
'> Changing Items'

#dict[key] = new_value
numerals["0"] = "0b110000" #{'0': '0b110000', '1': 49,...

#dict.update(iterable) updates dict with the key:value pairs of another dictionary or iterable of key:value pairs. returns None
alphanumeric ={}
alphanumeric.update(numerals)
alphanumeric.update(ucase_alpha)
alphanumeric.update(lcase_alpha)
{
  '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, 
  '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, 
  'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 
  'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 
  'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 
  'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 
  'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 
  'Z': 90, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 
  'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 
  'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 
  'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 
  't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 
  'y': 121, 'z': 122
}



#===============================================================================================================================#
'> Dictionary Operations'

#Check if a key exists 
"a" in numerals  #False
"a" in ucase_alpha #False
"a" in lcase_alpha #True


#Check if a key does not exist 
"z" not in numerals #True
"z" not in ucase_alpha #True
"z" not in lcase_alpha #False


#delete a key:value pair
del numerals["0"] #{'1': 49, '2': 50, '3': 51, '4': 52,...
del ucase_alpha["A"] #{'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70,...
del lcase_alpha["a"] #{'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102,...
del numerals # None

#use == for comparision. Returns true if both dicts have the same key:value pair regardless of order.
dict1 = {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102}
dict2 = {'d': 100, 'e': 101, 'f': 102,'a': 97, 'b': 98, 'c': 99 }

dict1 == dict2 #True
ucase_alpha == lcase_alpha #False

#merge (|) two dictionaries the values of the 2nd dictionary take priority when keys are shared
bin_dict = {'a': '0b1100001', 'b': '0b1100010', 'c': '0b1100011', 'd': '0b1100100', 'e': '0b1100101', 'f': '0b1100110'}
hex_dict = {'a': '0x61', 'b': '0x62', 'c': '0x63', 'd': '0x64', 'e': '0x65', 'f': '0x66'} 

bin_dict | hex_dict #returns new dictionary
#{'a': '0x61', 'b': '0x62', 'c': '0x63', 'd': '0x64', 'e': '0x65', 'f': '0x66'}


#update one dict with the values of another the 2nd dictionary's values take priority
hex_dict = {'a': '0b1100001', 'b': '0b1100010', 'c': '0b1100011', '1': '0b110001', '2': '0b110010', '3': '0b110011'}

bin_dict |= hex_dict #updates bin_dict
# {
#  'a': '0b1100001', 'b': '0b1100010', 'c': '0b1100011', 
#  'd': '0b1100100', 'e': '0b1100101', 'f': '0b1100110', 
#  '1': '0b110001', '2': '0b110010', '3': '0b110011'
# }


#===============================================================================================================================#
'> Built-in dictionary function calls'
'''
Functions are blocks of reusable code
  Functions are typically called using their name followed by parentheses 
    and any required arguments inside
  
      function_name(arguments)
'''

#len(dictionary) return the number of elements
len(ucase_alpha) #26

#iter(dictionary) return an iterator over the keys of the dictionary. 
iter(ucase_alpha)

#reversed(dictionary) return a reverse iterator over the keys of the dictionary.
reversed(ucase_alpha)

#===============================================================================================================================#
'> Built-in dictionary methods calls'
'''
  Methods are functions defined by a class
    Methods are typically called using an object or class and dot (.) syntax
      object.method(parameters) --> for methods which require objects
        or
      class.method(paramters) --> for methods which do not require objects
'''
#To see what methods you can call on an object use dir(object)
#To see more information on a specific method use help(object.method)

# dict.copy() return a shallow copy of a dictionary
ucase_alpha.copy()

# dict.fromkeys(iterable[, value=None]) returns a new dictionary with specified keys and optional default values.
keys = ['a', 'b', 'c']
default_value = 0
dict.fromkeys(keys, default_value)

#dict.pop(key[,default=]) iff key is in the dictionary, remove it and return its value, else return default. 
ucase_alpha.pop()

#dict.popitem() remove and return a (key, value) pair from the dictionary. Pairs are returned in last in first out(LIFO) order.
ucase_alpha.popitem()

# setdefault(key[, default]) If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
ucase_alpha.setdefault()

# dict.clear() remove all items from the dictionary.
ucase_alpha.clear() # {}

#===============================================================================================================================#
'> Looping through dictionaries'
#Looping items() returns a iterable view object offering keys and values
dictionary.items()

for name, num in dictionary.items():
    print(name,":", num)

#===============================================================================================================================#
'> Unpacking Dictionaries'
'''
 refers to the process of extracting individual elements 
 from a container (such as a list, tuple, dictionary)
'''

#Unpack dictionary types using **
old_contacts = {"Alice": "123-4567", "Bob": "987-6543"}
new_contacts = {"Bob": "555-5555", "Charlie": "333-3333"}
merged_contacts = {**old_contacts, **new_contacts}
#{'Alice': '123-4567', 'Bob': '555-5555', 'Charlie': '333-3333'}

#===============================================================================================================================#
'> Dictionary Comprehension'

#Dictionary Comprehension syntax
#{key_expression: value_expression for item in iterable}

dictionary = { x : x*5 for x in range(10)}#{0: 0, 1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45}

list1d = list(lcase_alpha)
dictionary = { list1d[x] : x*5 for x in range(10)} #{'a': 0, 'b': 5, 'c': 10, 'd': 15, 'e': 20, 'f': 25, 'g': 30, 'h': 35, 'i': 40, 'j': 45}



#===============================================================================================================================#
'> ASCII Table Dictionary'
ascii_dictionary = {}

for dec_ in range(32,127):
  # char = (dec, hex, oct, bin)
  ascii_dictionary[chr(dec_)] = (dec_,hex(dec_),oct(dec_),bin(dec_))

print(ascii_dictionary)
{
  ' ': (32, '0x20', '0o40', '0b100000'), 
  '!': (33, '0x21', '0o41', '0b100001'), 
  '"': (34, '0x22', '0o42', '0b100010'), 
  '#': (35, '0x23', '0o43', '0b100011'), 
  '$': (36, '0x24', '0o44', '0b100100'), 
  '%': (37, '0x25', '0o45', '0b100101'), 
  '&': (38, '0x26', '0o46', '0b100110'), 
  "'": (39, '0x27', '0o47', '0b100111'), 
  '(': (40, '0x28', '0o50', '0b101000'), 
  ')': (41, '0x29', '0o51', '0b101001'), 
  '*': (42, '0x2a', '0o52', '0b101010'), 
  '+': (43, '0x2b', '0o53', '0b101011'), 
  ',': (44, '0x2c', '0o54', '0b101100'), 
  '-': (45, '0x2d', '0o55', '0b101101'), 
  '.': (46, '0x2e', '0o56', '0b101110'), 
  '/': (47, '0x2f', '0o57', '0b101111'),

  '0': (48, '0x30', '0o60', '0b110000'), 
  '1': (49, '0x31', '0o61', '0b110001'), 
  '2': (50, '0x32', '0o62', '0b110010'), 
  '3': (51, '0x33', '0o63', '0b110011'), 
  '4': (52, '0x34', '0o64', '0b110100'), 
  '5': (53, '0x35', '0o65', '0b110101'), 
  '6': (54, '0x36', '0o66', '0b110110'), 
  '7': (55, '0x37', '0o67', '0b110111'), 
  '8': (56, '0x38', '0o70', '0b111000'), 
  '9': (57, '0x39', '0o71', '0b111001'),

  ':': (58, '0x3a', '0o72', '0b111010'), 
  ';': (59, '0x3b', '0o73', '0b111011'), 
  '<': (60, '0x3c', '0o74', '0b111100'), 
  '=': (61, '0x3d', '0o75', '0b111101'), 
  '>': (62, '0x3e', '0o76', '0b111110'), 
  '?': (63, '0x3f', '0o77', '0b111111'), 
  '@': (64, '0x40', '0o100', '0b1000000'),

  'A': (65, '0x41', '0o101', '0b1000001'), 
  'B': (66, '0x42', '0o102', '0b1000010'), 
  'C': (67, '0x43', '0o103', '0b1000011'), 
  'D': (68, '0x44', '0o104', '0b1000100'), 
  'E': (69, '0x45', '0o105', '0b1000101'), 
  'F': (70, '0x46', '0o106', '0b1000110'), 
  'G': (71, '0x47', '0o107', '0b1000111'), 
  'H': (72, '0x48', '0o110', '0b1001000'), 
  'I': (73, '0x49', '0o111', '0b1001001'), 
  'J': (74, '0x4a', '0o112', '0b1001010'), 
  'K': (75, '0x4b', '0o113', '0b1001011'), 
  'L': (76, '0x4c', '0o114', '0b1001100'), 
  'M': (77, '0x4d', '0o115', '0b1001101'), 
  'N': (78, '0x4e', '0o116', '0b1001110'), 
  'O': (79, '0x4f', '0o117', '0b1001111'), 
  'P': (80, '0x50', '0o120', '0b1010000'), 
  'Q': (81, '0x51', '0o121', '0b1010001'), 
  'R': (82, '0x52', '0o122', '0b1010010'), 
  'S': (83, '0x53', '0o123', '0b1010011'), 
  'T': (84, '0x54', '0o124', '0b1010100'), 
  'U': (85, '0x55', '0o125', '0b1010101'), 
  'V': (86, '0x56', '0o126', '0b1010110'), 
  'W': (87, '0x57', '0o127', '0b1010111'), 
  'X': (88, '0x58', '0o130', '0b1011000'), 
  'Y': (89, '0x59', '0o131', '0b1011001'), 
  'Z': (90, '0x5a', '0o132', '0b1011010'),

  '[': (91, '0x5b', '0o133', '0b1011011'), 
  '\\': (92, '0x5c', '0o134', '0b1011100'), 
  ']': (93, '0x5d', '0o135', '0b1011101'), 
  '^': (94, '0x5e', '0o136', '0b1011110'), 
  '_': (95, '0x5f', '0o137', '0b1011111'), 
  '`': (96, '0x60', '0o140', '0b1100000'),

  'a': (97, '0x61', '0o141', '0b1100001'), 
  'b': (98, '0x62', '0o142', '0b1100010'), 
  'c': (99, '0x63', '0o143', '0b1100011'), 
  'd': (100, '0x64', '0o144', '0b1100100'), 
  'e': (101, '0x65', '0o145', '0b1100101'), 
  'f': (102, '0x66', '0o146', '0b1100110'), 
  'g': (103, '0x67', '0o147', '0b1100111'), 
  'h': (104, '0x68', '0o150', '0b1101000'), 
  'i': (105, '0x69', '0o151', '0b1101001'), 
  'j': (106, '0x6a', '0o152', '0b1101010'), 
  'k': (107, '0x6b', '0o153', '0b1101011'), 
  'l': (108, '0x6c', '0o154', '0b1101100'), 
  'm': (109, '0x6d', '0o155', '0b1101101'), 
  'n': (110, '0x6e', '0o156', '0b1101110'), 
  'o': (111, '0x6f', '0o157', '0b1101111'), 
  'p': (112, '0x70', '0o160', '0b1110000'), 
  'q': (113, '0x71', '0o161', '0b1110001'), 
  'r': (114, '0x72', '0o162', '0b1110010'), 
  's': (115, '0x73', '0o163', '0b1110011'), 
  't': (116, '0x74', '0o164', '0b1110100'), 
  'u': (117, '0x75', '0o165', '0b1110101'), 
  'v': (118, '0x76', '0o166', '0b1110110'), 
  'w': (119, '0x77', '0o167', '0b1110111'), 
  'x': (120, '0x78', '0o170', '0b1111000'), 
  'y': (121, '0x79', '0o171', '0b1111001'), 
  'z': (122, '0x7a', '0o172', '0b1111010'),

  '{': (123, '0x7b', '0o173', '0b1111011'), 
  '|': (124, '0x7c', '0o174', '0b1111100'), 
  '}': (125, '0x7d', '0o175', '0b1111101'),
  '~': (126, '0x7e', '0o176', '0b1111110')
}










    








