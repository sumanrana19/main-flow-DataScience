#Task-1
"Write a Python program to create a list, a dictionary, and a set. Perform basic operations like adding, removing, and modifying elements"

#List
print("List Operations")
list_op = [1, 2, 3]
print("Initial list:", list_op)

#Adding an element to the list
list_op.append(7)
print("After adding an element:", list_op)

#Removing an element from the list
list_op.remove(7)
print("After removing an element:", list_op)

# Modifying an element in the list
list_op[1] = 7
print("After modifying an element:", list_op)

#Dictionary
print("\nDictionary Operations")

dict_op = {'a': 11, 'b': 22, 'c': 33}
print("Initial dictionary:", dict_op)

#Adding an element to the dictionary
dict_op['d'] = 44
print("After adding an element:", dict_op)

#Removing an element from the dictionary
del dict_op['b']
print("After removing an element:", dict_op)

#Modifying an element in the dictionary
dict_op['a'] = 55
print("After modifying an element:", dict_op)

#Set
print("\nSet Operations")
set_op = {11, 12, 13}
print("Initial set:", set_op)

#Adding an element to the set
set_op.add(14)
print("After adding an element:", set_op)

#Removing an element from the set
set_op.remove(12)
print("After removing an element:", set_op)

#Modifying an element in the dictionary
set_op.add(15)
print("After modifying the set by adding another element:", set_op)