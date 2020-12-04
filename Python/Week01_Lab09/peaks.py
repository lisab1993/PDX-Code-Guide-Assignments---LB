
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
    return data2


def peaks_and_valleys(data):# - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
    '''Compiles a list of peaks and valleys in order of appearance in their original list'''
    data2 = []#make a blank list for our valleys
    for i in range(1,len(data)-1):#iterate over the all indices, except for the fist and last ones
        if data[i-1] < data[i] and data[i+1] < data[i]:#find the peaks 
            data2.append(i)#add the peaks to the list
        if data[i-1] > data[i] and data[i+1] > data [i]:#find the vallyes
            data2.append(i)#add the valleys to the list
    return data2#return the data after we've searched our specified range.      

            
#       0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]




def painting(data):
    '''Prints a visual representation of the peaks and valleys'''
    for i in range(20):#iterate through the list
        if



# ---Steps:
# 1. iterate through the list

# 2. find the biggest number in the list.
# 3. compare the index to the biggest value
# 4. if the value at the index is smaller than the biggest value, print a whitespace
# 5. if the value at the index is the same as the biggest value, print an x
# 6. if the value at the index is larger than the biggest value, print an x

#going to need a double for loop. the outer loop will go down the rows, and the inner loop will go across the columns.

'''
Version 2 (optional)
Using the data list above, draw the image of X's above.

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

---Brain Dump:
- the largest value is how many lines we will print. So when I make the loop, I want to use len() to get the highest value. 
-I want it to iterate over the list, and depending on how far it is from the largest number, it will print an x, or a space. 
-The first time it goes through the list, it will find the largest number. 
-Then, when it goes through the list, it will see if the number is smaller than the lartest value. 
-if it's smaller, print a space. 
-If it's the same, pring an x. 

-the next time I go through, I want to look for the second smallest value, and do the same thing. 

---Steps:
1. iterate through the list
2. find the biggest number in the list.
3. compare the index to the biggest value
4. if the value at the index is smaller than the biggest value, print a whitespace
5. if the value at the index is the same as the biggest value, print an x
6. if the value at the index is larger than the biggest value, print a whitespace


'''




