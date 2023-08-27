'''Python Lists'''

'''
Covered in this video:
> Defining a list
> Declaring and Initializing 
> Accessing Data
> Changing Data
> Common built-in functions used with lists
> Common built-in methods used with lists

'''
#################################################################################
'Defining a list'

'A list is an ordered mutable collection of data.'
# ordered meaning it has a specific order 0,1,2,...
# mutable meaning it can be changed

["a","b","c","d","e"] #list (contains multiple items called elements)
# 0   1   2   3   4   #indexes (are used to access each element)
# length = 5          #The length is the total number of elements

# List indexes always start at 0 
#In this example:
#   a,b,c,d,e are elements
#   0,1,2,3,4 are indexes
#   length = 5

#################################################################################
'Declaring and Initializing'

list1d = [1,2,3,4,5,6,7,8,9] #declare and initialize
#index    0 1 2 3 4 5 6 7 8
#length = 9

#################################################################################
'Accessing Data'
list1d = ["a","b","c","d","e","f","g","h","i","j","k","l"]
#index     0   1   2   3   4   5   6   7   8   9   10  11
#reverse  -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1

# elements in a list are accessed by their index

#Starting from the front end
list1d[0] #a
list1d[5] #f
list1d[10] #k

#Starting from the back end
list1d[-1] #l
list1d[-5] #h
list1d[-10] #c

#################################################################################
'Changing Data'
list1d = ["a","b","c","d","e","f","g","h","i","j","k","l"]
#index     0   1   2   3   4   5   6   7   8   9   10  11
#reverse  -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1

# elements in a list are changed by assigning a new value to its index

#Starting from the front end
list1d[0] = "z" 
list1d[5] = "y" 
list1d[10] = "x" 

#Starting from the back end
list1d[-1] = "m"
list1d[-5] = "n"
list1d[-10] = "o"

#Here is the new list:
list1d = ["z","b","o","d","e","y","g","n","i","j","x","m"]
#index     0   1   2   3   4   5   6   7   8   9   10  11
#reverse  -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1

#################################################################################
'Common built-in functions used lists'

len(list1d) #returns number of elements in a list


#################################################################################
'Common built-in methods used lists'

