#===============================================================================================================================#
'''Python Objects'''
#===============================================================================================================================#
'''
  Covered in this video:
  > Importing a Class
  > Instances of a Class: Objects
  > Constructors: Building Objects
  > Built-in Constructors
  > Instance Variables : Attributes 
  > Instance Methods : Functions
'''
#===============================================================================================================================#
'> Importing a Class'
# To use a class that is not defined in this file, you must import the class from another file.
from Classes import Player
#from Module import Class
#     File
#Modules are files
#If the file with the class definition is not in the same folder, you will need to add it to the path

#===============================================================================================================================#
'> Instances of a Class: Objects'
'''
You have already been using objects

In python 'everything is an object' 

When we say "everything is an object, 
  we mean that every piece of data (variables, functions, classes, modules, etc.) 
    in Python is represented by an object in memory.
'''

type(10)              #<class 'int'>
type(3.14)            #<class 'float'>
type(True)            #<class 'bool'>
type("Hello")         #<class 'str'>
type(["a","b","c"])   #<class 'list'>
type(("a","b","c"))   #<class 'tuple'>
type({"a","b","c"})   #<class 'set'>
type({"a":1,"b":2})   #<class 'dict'>
type(range(10))       #<class 'range'>
type(bytes(b"hello")) #<class 'bytes'>

# Example with our class
player1 = Player()
#                              Module.Class
print(type(player1)) #<class 'Classes.Player'>

#===============================================================================================================================#
'> Constructors: Building Objects'
' > Constructors are special methods defined by the class(def __init__), and used to create instances of a class(objects)'

# Constructor Call with 0 Arguments
player1 = Player()     #Create a new Player object referenced using player1


#Constructor Call with Arguments
player2 = Player("Player 2", 100, 100, 5, attack = 75, defense = 75, bag = {})
#         Player(name, stamina = 75, *args, attack = 50 *kwargs)



#===============================================================================================================================#
'> Built-in Constructors'

int()            # Constructs an integer object with a default value of 0.
float()          # Constructs a float object with a default value of 0.0.
bool()           # Constructs a boolean object with a default value of False.
str()            # Constructs an empty string object.
list()           # Constructs an empty list object.
tuple()          # Constructs an empty tuple object.
set()            # Constructs an empty set object.
dict()           # Constructs an empty dictionary object.
complex()        # Constructs a complex number object. It takes two optional arguments: real and imag.
bytes()          # Constructs a bytes object from an optional iterable of integers representing byte values.
range()          # Constructs a range object that represents a sequence of numbers. It can take up to three arguments: start, stop, and step.
frozenset()      # Constructs an immutable set object from an optional iterable.
memoryview()     # Constructs a memory view object that exposes the buffer interface of an object.
enumerate()      # Constructs an enumerate object that pairs each element of an iterable with its index.
filter()         # Constructs an iterator that filters elements from an iterable based on a function.
map()            # Constructs an iterator that applies a function to every item of an iterable, yielding the results.
zip()            # Constructs an iterator that aggregates elements from multiple iterables into tuples.
super(None)      # Constructs a super object, typically used for delegating method calls to a superclass.

#===============================================================================================================================#
'> Instance Variables : Attributes' 
' > Attributes are instance variables (variables associated with an object)'


'> Access Instance Variables with object.variable'
#Player 1
print( type(player1) )   #<class 'Classes.Player'>
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#       object.variable
print( player1.name )    # Player 1
print( player1.stamina ) # 50
print( player1.magic )   # 50
print( player1.level )   # 1
print( player1.attack )  # 10
print( player1.defense ) # 10
print( player1.bag )     # {}
#             ^
#Dot syntax is used for variables and methods attached to Classes and Objects 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#Player 2 (Notice that the values for player2 are different than player 1)
print(type(player2))   #<class 'Classes.Player'>
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#       object.variable
print( player2.name )    # Player 2
print( player2.stamina ) # 100
print( player2.magic )   # 100
print( player2.level )   # 5
print( player2.attack )  # 75
print( player2.defense ) # 75
print( player2.bag )     # {}
#             ^
#Dot syntax is used for variables and methods attached to Classes and Objects 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#===============================================================================================================================#
'> Instance Methods : Functions'
' > Instance Methods are functions associated with an object'

'> Call an Instance Method with object.method(parameters)'

#Player 1
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#object.method()
player1.fight() # Player 1 does 10 point(s) of damage!
player1.run() # Player 1 attemps to flee!... Player 1 got away!
player1.check_bag("stuff") # Looks like stuff is not in the bag...
player2.check_level() # 1
#      ^
#Dot syntax is used for variables and methods attached to Classes and Objects 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#Player 2
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#object.method()
player2.fight() # Player 2 does 75 point(s) of damage!
player2.run() # Player 2 attemps to flee!... Oh No! the path is blocked!
player2.check_bag("thing") # Looks like thing is not in the bag...
player2.check_level() # 5
#      ^
#Dot syntax is used for variables and methods attached to Classes and Objects 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


#===============================================================================================================================#








































# class BluePrint():
#   def __init__(self):
#     self.attribute = 1

#   def __init__(self,number):
#     self.attribute = number

#   def method(self):
#     return "The method was called"

# 'Objects'
# # an object is an instance of a class
# # in other words if the class is a blueprint, and object is a building made from that blueprint.
# #Objects store two things attributes and methods. 
# #Object is a collection of data(variables) and methods that operate on that data

# 'Creating Objects'
# #an object is created by calling a special method(function) called a constructor

# object = BluePrint() #BluePrint() is the constructor. It makes the object

# #some constructors accept arguments

# object = BluePrint(10) 

# 'Attributes'
# #variables that are associated with an object
# object.attribute

# #===============================================================================================================================#

# #Object is a collection of data(variables) and methods that operate on that data
# #Classes are blueprints for one or more objects

# #methods are functions that are apart of an object
# print("test".__len__())
# print("test".islower())

# print("abcd".replace("a","b"))



# #Converting
# print("Convert" + str(702)) #str converts the text to a string
# print(int("2") + 3) #int converts the text into an interger



# class Car1:
#     def __init__(self.started = False, speed = 0):
#         self.started = started
#         self.speed = speed
    
#     def start(self):
#         self.started = True
#         print("Car started, let's ride!")
        
#     def increase_speed(self,delta):
#         if self.started:
#             self.speed = self.speed + delta
#             print("Vroooom!")
#         else:
#             print("You need to start the car first")
            
#     def stop(self):
#         self.speed = 0
#         print("Halting")
        
# c1=Car1()
# c2=Car1(True)
# c3=Car1(True,50)
# c4=Car1(started=True, speed=40)

# print(c1.speed)
# c1.start()
# c1.increase_speed(50)
# print(c1.speed)
# print(c2.speed)
# print(c3.speed)
# print(c4.speed)

# #Python Inheritance
# # Here we define a class called Vehicle and define 4 methods. 
# class Vehicle:
#     def __init__(self,started = False,speed = 0):
#         self.started = started
#         self.speed = speed
        
#     def start(self):
#         self.started = True
#         print("Started, let's ride!")
    
#     def stop (self):
#         self.speed = 0
        
#     def increase_speed(self, delta):
#         if self.started:
#             self.speed = self.speed + delta
#             print("Vrooooom!")
#         else:
#             print("You need to start me first")

# # The car class inherits all methods and variables from the vehicle class but adds the extra variable and two methods. 
# class Car3 (Vehicle): #here the parameter Vehicle allows inheritance of the methods and variables from the vehicle class. 
#     trunk_open = False
#     def open_trunk(self):
#         trunk_open = True
#     def close_trunk(self):
#         trunk_open = False
        


# c5 = Car3()#Instantiate a the class instance c5 = Car3()
# c5.start()#Call the method inherited from the Vehicle class by the Car3 class.

# #Overriding Methods in Python

# class Motorcycle(Vehicle):
#      def __init__(self,center_stand_out = False):
#          self.center_stand_out = center_stand_out
#          super().__init__()#super allows us to call the constructor of the parent class (Vehicle) and removes the parameters self,started = false, speed = "0"
# #added functionality for center stand but removed option to set speed and started state.
         
# #Overriding other methods
# class Motorcycle1(Vehicle):
#     def __init__(self, center_stand_out = False):
#         self.center_stand_out = center_stand_out
#         super().__init__()
#     def start(self):#Overrides the (Vehicle) start method. 
#         print("Sorry, out of fuel!")
        
        
# motorcycle = Motorcycle1()
# motorcycle.start()

# # When called without arguments, dir() returns a list of names in the current local scope, including variables, functions, and imported modules.
# print(dir())
# # When called with an object as an argument, dir() returns a list of valid attributes and methods for that object.
# print(dir(5))
# print(dir("I"))
# print(dir(True))

# # When used with a module object, dir() returns a list of names defined in that module.
# import math
# print(dir(math))


# del object