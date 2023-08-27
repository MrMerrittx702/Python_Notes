'''Sets'''
'''
sets are unordered, immutable, unindexed, and do not allow duplicate values

you can add and remove items only
'''

_set = {1,2,3}#use curly braces

#add with update from any iterable(tuples,lists,dictionaries,sets)

_set.update({4})
print(_set)

#remove from ste with remove() and discard()
_set.remove(4)#if item doesn't exist will cause error

_set.discard(4)#if item doesn't exit will not cause error

#clear empties the set
_set.clear()

#use union() method to join items
_set1 = {1,2,3,4,5}
_set2 = {6,7,8,9,0}
_set3 = _set1.union(_set2)

#to keep only the duplicates use intersection_update()
_set4 = {1,2,2}
_set5 = {3,2,4}
_set4.intersection_update(_set5)

#to keep all but the duplicates
_set4 = {1,2,2}
_set5 = {3,2,4}
_set4.symmetric_difference(_set5)



#del keyword removes the set completely
del _set







