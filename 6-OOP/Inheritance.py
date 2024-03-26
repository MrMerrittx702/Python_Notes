'''Inheritance'''

'''Biology'''
class Living_Thing:
  cells = True
  reproduce = True
  grow = True
  response = True
  homeostatis = True
  adaptation = True
  metabolism = True


class Eukarya(Living_Thing):

class Animalia(Eukarya):

class Plantae(Eukarya):

class Fungi(Eukarya):

class Archaea(Living_Thing):

class Bacteria(Living_Thing):
##########################################################################################################################################################
'''Geometry'''
class Shape:
  pass
class Rectangle(Shape):
  pass
class Square(Rectangle):
  pass

class Ellipse(Shape):
  pass
class Circle(Ellipse):
  pass

class Triangle(Shape):
  pass
class Equalatoral(Triangle):
  pass
class Isoscles(Triangle):
  pass
class Scalene(Triangle):
##########################################################################################################################################################
'''Chemistry'''
class Matter:
  pass
class Pure_Substance(Matter):
  pass
class Element(Pure_Substance):
  pass
class Compound(Pure_Substance):
  pass
class Mixture(Matter):
  pass
class Homogenous(Mixture):
  pass
class Solution(Homogenous):
  pass
class Heterogenous(Mixture):
  pass
class Suspension(Heterogenous):
#######################################################################################################################
'''English'''
class Word:
  pass
class Noun(Word):
  pass
class Adjective(Word):
  pass
class Verb(Word):
  pass

###############################################################################################################



class Player:
  
  def __init__(self,name,hp,mp,xp):
    self.name = name
    self.hp = hp
    self.mp = mp
    self.xp = xp

  def __str__(self):#defines what is returned when an object of the class is represented as a string
    return self.name 

player_1 = Player("Jack",100,100,0)
player_2 = Player("Jill",300,50,0)
print(player_1)
print(player_2)




class Enemy:
  hp = 100
  mp = 100



'''Good Example Below'''

#What is "self" in Python?
#When we call a method on an object, Python automatically fills in the first variable, which we call self by convention.
#This first variable is a reference to the object itself, hence its name.
#We can use this variable to reference other instance variables and functions of this object, like self.speed and self.start().
#So only inside the class definition, we use self to reference variables that are part of the instance. 

class Car:
    started = False
    speed = 0
    
    def start(self):
        self.started = True
        print("Car started, let's ride!")
        
    def increase_speed(self,delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vroooom!")
        else:
            print("You need to start the car first")
            
    def stop(self):
        self.speed = 0
        print("Halting")
        
        
car = Car()
car.increase_speed(10)

car.start()
car.increase_speed(40)

#Multiple Objects
car1 = Car() #car1 object is assigned the Car() class.
car2 = Car()
print(id(car1))
print(id(car2))

car1.start() #the start method is called on the car1 object.
car1.increase_speed(10) #The increase_speed method is called on the car1 object and given the 10 argument
print(car1.speed)
print(car2.speed)

#Converting
print("Convert" + str(702)) #str converts the text to a string
print(int("2") + 3) #int converts the text into an interger



class Car1:
    def __init__(self.started = False, speed = 0):
        self.started = started
        self.speed = speed
    
    def start(self):
        self.started = True
        print("Car started, let's ride!")
        
    def increase_speed(self,delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vroooom!")
        else:
            print("You need to start the car first")
            
    def stop(self):
        self.speed = 0
        print("Halting")
        
c1=Car1()
c2=Car1(True)
c3=Car1(True,50)
c4=Car1(started=True, speed=40)

print(c1.speed)
c1.start()
c1.increase_speed(50)
print(c1.speed)
print(c2.speed)
print(c3.speed)
print(c4.speed)

#Python Inheritance
# Here we define a class called Vehicle and define 4 methods. 
class Vehicle:
    def __init__(self,started = False,speed = 0):
        self.started = started
        self.speed = speed
        
    def start(self):
        self.started = True
        print("Started, let's ride!")
    
    def stop (self):
        self.speed = 0
        
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooooom!")
        else:
            print("You need to start me first")

# The car class inherits all methods and variables from the vehicle class but adds the extra variable and two methods. 
class Car3 (Vehicle): #here the parameter Vehicle allows inheritance of the methods and variables from the vehicle class. 
    trunk_open = False
    def open_trunk(self):
        trunk_open = True
    def close_trunk(self):
        trunk_open = False
        


c5 = Car3()#Instantiate a the class instance c5 = Car3()
c5.start()#Call the method inherited from the Vehicle class by the Car3 class.

#Overriding Methods in Python

class Motorcycle(Vehicle):
     def __init__(self,center_stand_out = False):
         self.center_stand_out = center_stand_out
         super().__init__()#super allows us to call the constructor of the parent class (Vehicle) and removes the parameters self,started = false, speed = "0"
#added functionality for center stand but removed option to set speed and started state.
         
#Overriding other methods
class Motorcycle1(Vehicle):
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__()
    def start(self):#Overrides the (Vehicle) start method. 
        print("Sorry, out of fuel!")
        
        
motorcycle = Motorcycle1()
motorcycle.start()




