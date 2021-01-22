'''
types
    none
    boolean 
    string
    int
    float
    list
    dictionary
    range
operators
    =
    +, -, *, /, //, **, %
    +=, -=, *=, /=, //=, **=, %=
    ==, !=, <, <=, >, >=
    and, or, not
    in
    is
    del
keywords
    if, elif, else
    for, while
    break, continue
    return
    # (comment)
built-in functions
    input
    print
    len (gets the length of a list)
    ord, chr (switches back and forth between characters and their ascii codes)
    abs
    int, str, list

    ############################################################
    string methods
    *count 
        -returns the number of occurences of a

        print('abcacba'.count('a')) # 3

    *startswith
        -returns true if a starts with b

        a.startswith(b) 
        print('hello world'.startswith('hello')) # True
        print('hello world'.startswith('world')) # False

    *endswith
        -returns true if the string ends with b

        a.endswith(b) 
        print('hello world'.endswith('hello')) # False
        print('hello world'.endswith('world')) # True

    *split 
        -splits a string into a list. If no parameter is given, it'll split on whitespace

        s.split(...delimeter) 
        fruits = 'apples, bananas, pears'
        print(fruits.split(', ')) # ['apples', 'bananas', 'pears']

    *join
        -combines the elements of a list into a single string, separated by the delimeter

        delimeter.join(list) 
        print(' - '.join(['apples', 'bananas', 'pears']) # apples - bananas - pears


    *lower 
        -everything entered will be converted to lowercase letters. 
        print('Hello'.lower()) # hello
    *upper
        -everything will be uppercase.
    *title 
        -the first letter of each word will be capitalized.
    *capitalize
        -the first letter of the first word will be capitalized

    *strip
        -removes leading and trailing characters. If given no parameter, it'll strip whitespace
        s.strip()

        print('   hello\t\n  '.strip()) #hello
        print('__%__hello_world__%__'.strip('_%')) # hello_world

    *replace
        -replaces occurances of string b with string c
        a.replace(b, c) 

        print('hello world'.replace('hello', 'goodbye')) # goodbye world

    *isdigit
        -Check if all the characters in the text are digits:

        txt = "50800"
        x = txt.isdigit()
        print(x)
    ---------------------------------------------------------------------------------------------------------  
    list methods
    *append
    mylist.append(element)
        -We can use the append method to add an element to the end of a list.

        fruits = ['apple', 'banana', 'peach', 'pear']
        fruits.append('pineapple')
        print(fruits) # ['apple', 'banana', 'peach', 'pear', 'pineapple']

    *insert
    mylist.insert(index, element)
        -We can insert an element into an arbitrary place in the list

        fruits = ['apples', 'bananas', 'pears']
        fruits.insert(1, 'cherries') # insert an element at index 1
        print(fruits) # ['apples', 'cherries', 'bananas', 'pears']

    *pop
    mylist.pop(index)
        -The pop method removes an element at a given index and returns it.

        fruits = ['apples', 'bananas', 'pears']
        print(fruits.pop(1)) # 'bananas'
        print(fruits) # ['apples', 'pears']

    *remove
    mylist.remove(element)
        -We can use the remove method to remove an element. This only removes the first occurance.

        fruits = ['apples', 'pears', 'bananas', 'pears']
        fruits.remove('pears')
        print(fruits) # ['apples', 'bananas', 'pears']

    *reverse
    mylist.reverse()
        -We can use the reverse method to reverse a list:

        fruits = ['apples', 'bananas', 'pears']
        fruits.reverse()
        print(fruits) # ['pears', 'bananas', 'apples']

    *sort
    mylist.sort()
        -We can use the sort method to sort a list:

        fruits = ['cherries', 'bananas', 'pears', 'apples']
        fruits.sort()
        print(fruits) # ['apples', 'bananas', 'cherries', 'pears']

    *extend
    mylist.extend(otherlist)
        -The extend method appends all the elements from one list to another.

        fruits1 = ['apples', 'bananas', 'pears']
        fruits2 = ['cherries', 'pineapples']
        fruits1.extend(fruits2) # ['apples', 'bananas', 'pears', 'cherries', 'pineapples']
        print(fruits1)

    *copy
    mylist.copy()
        -We can use the copy method to create a copy of a list. Editing a copy won't change the original.

        fruits1 = ['apples', 'bananas', 'pears']
        fruits2 = fruits1.copy()
        fruits2[0] = 'pineapples'
        print(fruits1) # ['apples', 'bananas', 'pears']
        print(fruits2) # ['pineapples', 'bananas', 'pears']

    *index
    mylist.index(element)
        -The index method gives us the index of the first occurrence of an element.

        fruits = ['apples', 'bananas', 'pears']
        print(fruits.index('bananas')) # 1

    *find
    s.find(a) 
        -returns the index of a the first occurance of a

        print('hello world'.find('l')) #2

        #########################################################################################

modules
    random
        randint
        choice
    string

---------------------------------------------------------
    -to iterate over the indices of a list, use range(). to iterate over the values within a list, for num in nums:

    -Json.load()
        takes a file object and returns the json object.
        It is used to read JSON encoded data from a file and convert it into a Python dictionary and deserialize a file itself i.e. it accepts a file object.


    -json.loads()
        method can be used to parse a valid JSON string and convert it into a Python Dictionary. 
        It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.
        If you have a JSON string, you can parse it by using the json.loads() method.

    -json only uses double quotes.

    -is tests for identity, not value. 

    -while loops are good if you don't know how many times you're going to loop, and for loops are good when you know how many times you'll loop.

    -ctrl + d and trype to change all of that element
'''
