'''
Programming 101
Unit 4 Review
'''

'''
datatype: list (list)
'Ordered' and 'changeable' sequences of items.
Lists are defined using square brackets []
Items are separated with commas ,
Since lists are 'ordered', their items can be retrieved using their positions in the list.
An item's position in the list is called its 'index' (indices plural)
'''

# define a list of strings
fruits = ['gauva', 'apricot', 'kiwi']

# organized vertically
fruits = [
    'guava',
    'apricot',
    'kiwi'
]

# print(fruits) # ['guava', 'apricot', 'kiwi']

# ------------------------------------------------------------------------------------ #

# because lists are 'ordered', their items can be retrieved using their indices
# list indices start at 0
# print(fruits[0]) # guava
# print(fruits[1]) # apricot
# print(fruits[2]) # kiwi

# step off the right edge of the list
# print(fruits[3]) # IndexError: list index out of range

# ---------------------------------------------------------------------- #


# Python allows negative indices
# -1 will be the last index in the list
# print(fruits[-1]) # kiwi
# print(fruits[-2]) # apricot
# print(fruits[-3]) # guava

# step off the left edge of the list
# print(fruits[-4]) # IndexError: list index out of range

# ------------------------------------------------------------------------------------------ #


# lists are changeable
fruits[1] = 'lime'
# print(fruits) # ['guava', 'lime', 'kiwi']

# cannot add items this way
# fruits[3] = 'lemon' # IndexError: list assignment index out of range

# --------------------------------------------------------------------------------------------- #

# use list methods to add items to a list
# .append(item) - add the item to the end of the list
fruits.append('lemon')
# print(fruits) # ['guava', 'lime', 'kiwi', 'lemon']

# .insert(index, item) - add the item at the index
fruits.insert(2, 'gooseberry')
# print(fruits) # ['guava', 'lime', 'gooseberry', 'kiwi', 'lemon']

# .extend(sequence) - add the items from the sequence to the end of the list
fruits.extend(['guava', 'lingonberry', 'strawberry'])
# print(fruits) # ['guava', 'lime', 'gooseberry', 'kiwi', 'lemon', 'guava', 'lingonberry', 'strawberry']

# ----------------------------------------------------------------------------------------- #

# delete items with list methods

# .remove(item) - remove the first occurrence of the item from the list
fruits.remove('guava')
# print(fruits) # ['lime', 'gooseberry', 'kiwi', 'lemon', 'guava', 'lingonberry', 'strawberry']

# .pop(index) - remove the item at the index and return it. index is -1 if not provided

# fruits.pop() # remove the last item from the list
# print(fruits) # ['lime', 'gooseberry', 'kiwi', 'lemon', 'guava', 'lingonberry']

# fruit = fruits.pop(1) # remove the item at index 1
# print(fruit, fruits) # gooseberry ['lime', 'kiwi', 'lemon', 'guava', 'lingonberry']


# -------------------------------------------------------------------------------------- #

# .index(item) - return the index of the first occurrence of the item, if it exists
lemon_index = fruits.index('lemon')
# print(lemon_index, fruits[lemon_index]) # 3 lemon

# value must exist in the list to get its index
# print(fruits.index('peach')) # ValueError: 'peach' is not in list

fruit = 'kiwi'
if fruit in fruits:
    index = fruits.index(fruit)
else:
    index = f'That item ({fruit}) is not in the list'

# print(index)

# --------------------------------------------------------------------------------------- #

# .sort() - sort a list in ascending order in place (returns None)
# fruits.sort()
# print(fruits) # ['gooseberry', 'guava', 'kiwi', 'lemon', 'lime', 'lingonberry', 'strawberry']

# use reverse=True to sort in descending order
# fruits.sort(reverse=True)
# print(fruits) # ['strawberry', 'lingonberry', 'lime', 'lemon', 'kiwi', 'guava', 'gooseberry']

# ------------------------------------------------------------------------------------ #

# typecast to list
# list(sequence) - return the sequence as a list, if possible
letters = list('ABCDEFG')
# print(letters) # ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# ----------------------------------------------------------------------------------- #


# for item in sequence - loop through each item in a sequence
'''
for fruit in fruits:
    print(fruit)
'''

# --------------------------------------------------------------------------------------------- #

# print only the fruits that start with the letter 'L'
'''
for fruit_name in fruits:
    # check if the first letter of the fruit's name is 'L'
    if fruit_name[0].upper() == 'L':
    # if 'berry' in fruit_name: # only print the berries
        print(fruit_name)
    else:
        print('...')
'''
# ----------------------------------------------------------------------------------------------- #

# for x in range() - loop a certain number of times

# range(stop) - return a range of numbers from 0 to stop-1
'''
for x in range(10):
    print(x, x * '*')
'''

