#===============================================================================================================================#
'''Script Kiddies First Python Program'''
#===============================================================================================================================#

#As a new programmer you might be refered to as a Script Kiddie, 
#This is a programmer joke to describe someone who does not know much about programming
#Script Kiddies often use code they do not understand written by other programmers

#Welcome to the Python Programming Language.
#Python is an interpreted procedural object oriented programming language
#Python files have the (.py) extension.

#===============================================================================================================================#
'''
Covered in this file:
> Single/Multi Line Comments
> First Program: Console Output
> First Program: User Input
> Executing Python Programs
'''
#===============================================================================================================================#
'> Single/Multi Line Comments'

# use a hash tag to make a single line python comment

'''
use three single quotes to make a 
  multi
    line 
      comment 
          called 
                a 
                  docstring
'''

# Use
# Ctrl + /
# to make quick multi-line comments
# or to comment out a single line easily

#===============================================================================================================================#
'> First Program: Console Output'

#To build your first program
#Use the built-in print() function call to send output to the console
print("Hello World") 
# text must be written in quotes and is called a string. 
#===============================================================================================================================#
'> First Program: User Input'

#To build your first program
#Use the built-in input() function call to accept input from a user
# input()

#Place a string of text inside the input() function call to prompt the user
# input("Type your input: ")

#If you place the input() function call inside of the  print() function call to see the input output
print(input("Type your input: ")) 
# text must be written in quotes and is called a string. 
#===============================================================================================================================#
'> Executing Python Programs'

'''
Congrats you have written your first python program!

  Scource code like this is compiled into byte code by the python interpretor(python.exe on windows|python3 on linux/MacOS).
    Then the python virtual machine PVM executes the bytecode instructions one by one.


Python Programs can be executed by invoking the interpreter through the command prompt or python shell.

  Python is installed by default here C:\Program Files\Python3xx on Windows depending on the version installed.
  Python may also be installed here for a specific user: C:\Users\%USERPROFILE%\AppData\Local\Programs\Python\Python3xx
    To check the current version type the following on the command line interface

      python --version

    To execute .py files on windows type the following on the command line interface

      python filename.py


    
  Python is installed by default here /usr/bin/python3 on Linux/MacOS depending on the version installed. 
    To check the current version type the following on the command line interface

      python3 --version
      
    To execute .py files on linux and Mac type the following on the command line interface

      python3 filename.py

'''

