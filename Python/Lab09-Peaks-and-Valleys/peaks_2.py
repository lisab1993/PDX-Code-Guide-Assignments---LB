import string

def peaks(data):
    '''Shows you where the peaks are in a given list'''#add a docstring to explain what the function's purpose is
    data2 = []
    for i in range(1,len(data)-1):#iterate over the all indices, except for the fist and last ones
        if data[i-1] < data[i] and data[i+1] < data[i]:#if the element to the left is smaller than the 
            data2.append(i)#add it to the new list
    return data2#return the data after we've searched our specified range.

def valleys(data):
    '''Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.'''
    data2 = []#make a blank list for our valleys
    for i in range(1,len(data)-1):#iterate over the list from the second element, to the second-to-last element
        if data[i-1] > data[i] and data[i+1] > data [i]:#make the comparisons to find the valleys
            data2.append(i)#add the valleys to the list
    return data2#return the data after we've searched our specified range.

def peaks_and_valleys(data):# - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
    '''Compiles a list of peaks and valleys in order of appearance in their original list'''
    data2 = []#make a blank list for our valleys
    for i in range(1,len(data)-1):#iterate over the all indices, except for the fist and last ones
        if data[i-1] < data[i] and data[i+1] < data[i]:#find the peaks 
            data2.append(i)#add the peaks to the list
        if data[i-1] > data[i] and data[i+1] > data [i]:#find the vallyes
            data2.append(i)#add the valleys to the list
    return data2#return the data after we've searched our specified range.      

'''
Hint 1: If you wanted to draw this horizontally, you could do so very easily like this.
# Hint 2: print can only work on one line at a time, so you'll have to loop and decide to either print a space ' ' or an 'X' for every column.

for num in data:
    print('x' * num)

    Example I/O:

                                                  X                 X
                                               X  X  X           X  X
                          X                 X  X  X  X  X     X  X  X
                       X  X  X           X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks(data) # [6, 14]
valleys(data) # [9, 17]
peaks_and_valleys(data) # [6, 9, 14, 17]

I want to repeat the whole loop 9 times. 


'''

def picasso(data):
    '''Vertically prints a data picture to show peaks and valleys'''
    row = []#Make a blank list for the X's and spaces to be printed out
    column = []#a blank list to iterate through to show the actual height of the mountains.

    sorted_list = data.copy()#copy the first list into another one to preserve the original list
    sorted_list.sort()#arrage the new list in order#####If I remove the duplicates in this list, I can go in descending order down this one for the outside for loop.
    largest_number = sorted_list[-1]#create a variable to hold the highest value within the list
    
    count = 1#loop control
    while count < largest_number + 1:#Iterate through all integers less than the largest number, and add them to the column list. +1 added to include the largest number itself
        column.append(count)#add the inters to the column list
        count += 1#step up the count
    column.reverse()#reverse it so that the largest value is always at [0]
    highest_point = column[0]

    row_across = " ".join(row)#make a new variable, and use .join to convert it into a string

    for i in column: 
        for x in data:#Iterate through the values within the list.
            if x < highest_point:#see if the value at the list index is smaller than the current largest number
                row.append(" ")#if it's smaller, add a blank space for that index
                continue#and continue until the list is done
            else:
                row.append("X")#if the value is equal or greater to the current largest number, print an X
        print(row_across)
        highest_point -= 1
    str(row)#convert our list into a string
    return row_across 
      
    


        


        
#            0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20
mountains = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

print(picasso(mountains))


