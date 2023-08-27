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

