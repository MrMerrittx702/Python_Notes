#===============================================================================================================================#
'''Classes'''
#===============================================================================================================================#
'''
Covered in this file:
> Class Definition
> Class Variables
> Class Methods
> Constructors: __init__(self)
  > self
  > Instance Variables 
> Instance Methods
> Getters and Setters: Property Function
> Special Methods to define:
> Accessing Class Variables 
> Calling Class Methods

'''
#===============================================================================================================================#
import random #This is not necessary to make a class


'> Class Definition (Blueprint for Objects)'
' > Also think of classes as custom data types'
class Player():
        
    '> Class Variables (access with Class.variable syntax)'
    player_list = [] #a list of all Player objects
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

    '> Class Method Definition (call with Class.method() syntax)'
    def display_players():
        print(Player.player_list)
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

    '> Special Method Definition: Constructor, builds an object (call with Class() )'

    #No Argument Constructor
    # def __init__(self):
    #     self.health = 100 #set by default here
    #     #   ^
    #     #Dot syntax is used for variables and methods attached to Classes and Objects 

    #     self.name = "Player 1"
    #     self.stamina = 50
    #     self.magic = 50
    #     self.level = 1

    #     self.attack = 10
    #     self.defense = 10
    #     self.bag = {}
            

    #     # SEE __iter__ below
    #     self.number_of_attributes = 8 #set by default here
    #     self.count = 0
    #     self.attributes = (
    #         self.health, self.name, self.stamina,
    #         self.magic, self.level, self.attack, 
    #         self.defense, self.bag
    #     )

    #Parameterized Constructor  
    def __init__(self,name,stamina = 75,*args, attack = 50, **kwargs):
        
        '> Instance Variables: What an object is (access with object.variable syntax)'
    #   self is a reference to the instance of the class (object)  
    #   self.variable
        self.health = 100 #set by default here
        #   ^
        #Dot syntax is used for variables and methods attached to Classes and Objects 

        self.name = name #required set by argument
        self.stamina = stamina #optionally set by argument or default
        self.magic = args[0] #required additional positional args (accessed like a list)
        self.level = args[1] #required additional positional args (accessed like a list)

        self.attack = attack #required set by keyword argument
        self.defense = kwargs["defense"] #additonal keyword args accessed like a dictionary
        self.bag = kwargs["bag"]
        #Note: The variables colored purple are local variables not instance variables

        # SEE __iter__ below
        self.number_of_attributes = 8 #set by default here
        self.count = 0
        self.attributes = (
            self.health, self.name, self.stamina,
            self.magic, self.level, self.attack, 
            self.defense, self.bag
        )
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

    '> Instance Method Definitions: What an object does (call with object.method() syntax)'
    def fight(self):
        print(f"{self.name} does {self.attack} point(s) of damage!")


    def run(self):
        print(f"{self.name} attemps to flee!...")

        if(5 < random.randint(1,10)):
            print(f"{self.name} got away!")
        else:
            print(f"Oh No! the path is blocked!")


    def check_bag(self,item):      
        if(item in self.bag):
            print(f"{item} was found in the bag!")
        else:
            print(f"Looks like {item} is not in the bag...")

    def check_level(self):
        return self.level
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    '> Getters and Setters: Property Function'
    ' > Getters are used to control how data is retrieved'
    ' > Setters are used to control how data is changed'

    ''' > The property() function maps these functions to 
            a variable so that they are automatically called when the variable is accessed'''

    def get_health(self):
        return self.health
    
    def set_health(self, number):
        if (1000 >= self.health + number):
            self.heath += number
        else:
            self.health = 1000
    
    def del_health(self):
        del self.health

    # health = property(get_health,set_health,del_health,"Health determines if the Player can continue")
    #p1 = Player()
    #p1.health #Calls get_health()
    #p1.health = 1500 Calls set_health()
    #del p1.health  Calls del_health()
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    '''
        Special Methods: dunder methods 
        __init__
        __str__
        __repr__
        __len__
        __getitem__ 
        __setitem__
        __delitem__
        __iter__ 
        __next__
        __contains__
        __eq__, __lt__, __le__, __gt__, __ge__
        __add__, __sub__, __mul__, __truediv__
        __call__
        __getattr__
        __setattr__
        __delattr__
                
        __hash__
        __enter__
        __exit__
    '''
    #__str__(self): Returns a string representation of an object, used by the str() function and print() function.
    def __str__(self):
        return self.name
    #Is automatically called when trying to use the object as a string
    #call -->  print(object) 
    #call --> str(object)

    #__repr__(self): Returns a string representation of an object for debugging, used by the repr() function.
    def __repr__(self):
        return "Player()"
    #call --> repr(object)

    # __len__(self): Returns the length of an object, used by the len() function.
    def __len__(self):
        return self.number_of_attributes
    #call len(object)

    # __getitem__(self, key): Returns the value associated with a given key, used for indexing (e.g., obj[key]).
    def __getitem__(self,key):
        #used to define behavior when an object is access using indexing notation
        return self.bag[key]
    #call object.__getitem__(key_arg)

    # __setitem__(self, key, value): Sets the value associated with a given key, used for item assignment (e.g., obj[key] = value).
    def __setitem__(self,key,value):
        self.bag[key] = value
    #call object.__setitem__(key_arg, value_arg)

    # __delitem__(self, key): Deletes the item associated with a given key, used by the del statement.
    def __delitem__(self,key): 
        del self.bag[key]

    # __iter__(self): Returns an iterator object, used by the iter() function to iterate over an object.
    def __iter__(self):
        # Iterators must return themselves as an iterator
        return self

    # __next__(self): Returns the next item in the iteration, used by the next() function.
    def __next__(self):
        if(self.count < self.number_of_attributes):
            self.count += 1
            return self.attributes[self.count-1]
        else:
            raise StopIteration

    # __contains__(self, item): Returns True if an object contains a specified item, used by the in operator.
    def __contains__(self, item):
        return item in self.attributes
    #example --> value in object
    
    # __eq__(self, other): Checks for equality between two objects, used by the == operator.
    def __eq__(self,other):
        return (self.name == other.name) and (self.level == other.level) 
    #example --> object1 == object2

    #Comparison operators for less than, less than or equal to, greater than, and greater than or equal to respectively.
    #__lt__(self, other) Less Than
    def __lt__(self,other):
        if isinstance(other,Player): 
            return self.level < other.level
        else:
            raise TypeError("Unsupported operand type(s) for < : Player() and {}".format(type(other)))


    #__le__(self, other) Less Than or Equal To
    def __le__(self,other):
        if isinstance(other,Player): 
            return self.level <= other.level
        else:
            raise TypeError("Unsupported operand type(s) for <= : Player() and {}".format(type(other)))

    
    # __gt__(self, other) Greater Than
    def __gt__(self,other):
        if isinstance(other,Player): 
            return self.level < other.level
        else:
            raise TypeError("Unsupported operand type(s) for > : Player() and {}".format(type(other)))

    
    # __ge__(self, other) Greater Than or Equal To
    def __ge__(self,other):
        if isinstance(other,Player): 
            return self.level < other.level
        else:
            raise TypeError("Unsupported operand type(s) for >= : Player() and {}".format(type(other)))

    
    #Arithmetic operators for addition, subtraction, multiplication, and division respectively.
    
    # __add__(self, other): Addition
    def __add__(self, other): 
        # Add corresponding attributes of two objects and return a new instance
        if isinstance(other, Player):
            # Create a new instance with combined attributes
            combined= Player(
                name = self.name, 
                stamina = self.stamina + other.stamina,
                attack = self.attack + other.attack,
                defense = self.defense + other.defense,
                bag = self.bag  
            )
            return combined
        else:
            raise TypeError("Unsupported operand type(s) for +: Player() and {}".format(type(other)))

    # __sub__(self, other): Subtraction
    def __sub__(self, other):
            # Subtract corresponding attributes of two objects and return a new instance
            if isinstance(other, Player):
                # Create a new instance with subtracted attributes
                subtracted = Player(
                    name= self.name,
                    stamina=self.stamina - other.stamina,
                    attack=self.attack - other.attack,
                    defense=self.defense - other.defense,
                    bag = self.bag  
                )
                return subtracted
            else:
                raise TypeError("Unsupported operand type(s) for -: Player() and {}".format(type(other)))

    # __mul__(self, other): Multiplication
    def __mul__(self, other):
        # Multiply corresponding attributes of two objects and return a new instance
        if isinstance(other, Player):
            # Create a new instance with multiplied attributes
            multiplied = Player(
                name = self.name,
                stamina = self.stamina * other.stamina,
                attack = self.attack * other.attack,
                defense = self.defense * other.defense,
                bag = self.bag 
            )
            return multiplied
        else:
            raise TypeError("Unsupported operand type(s) for *: Player() and {}".format(type(other)))

    #  __truediv__(self, other): Division
    def __truediv__(self, other): 
        # Divide corresponding attributes of two objects and return a new instance
        if isinstance(other, Player):
            # Create a new instance with divided attributes
            divided = Player(
                name = self.name,
                stamina = self.stamina / other.stamina,
                attack = self.attack / other.attack,
                defense = self.defense / other.defense,
                bag=self.bag  
            )
            return divided
        else:
            raise TypeError("Unsupported operand type(s) for /: Player() and {}".format(type(other)))


    # __call__(self, *args, **kwargs): Allows the instance of a class to be called as a function.
    def __call__(self,*args,**kwargs):
        print(f"Greetings Traveler, I am {self.name} the great hero of this world!")
        
    # __getattr__(self, name): Called when an attribute lookup fails.
    def __getattr__(self,name):
        if name in self.attributes:
            index = self.attributes.index(name)
            return self.attributes[index]
        else:
            # If the attribute doesn't exist, raise an AttributeError
            raise AttributeError(f"'Player' object has no attribute '{name}'")

        
    # __setattr__(self, name, value): Called when an attribute assignment is attempted.
    def __setattr__(self,name,value):
        if name == 'health' and value < 0:
            raise ValueError("Health cannot be negative")
        else:
            # Assign the attribute normally
            super().__setattr__(name, value)
    
    # __delattr__(self, name): Called when an attribute deletion is attempted.
    def __delattr__(self, name):
        if name == 'name':
            raise AttributeError("Cannot delete 'name' attribute")
        else:
            # Delete the attribute normally
            super().__delattr__(name)
#===============================================================================================================================#
'End of Class Definition'
#===============================================================================================================================#

'> Access Class Variables with Class.variable'

#       Class.variable
print( Player.player_list )
#            ^
#Dot syntax is used for variables and methods attached to Classes and Objects 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

'> Call a Class Method with Class.method(parameters)'
#Class.method()
Player.display_players()
#     ^
#Dot syntax is used for variables and methods attached to Classes and Objects 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
