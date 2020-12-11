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


the_rockies = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks(the_rockies))
print(valleys(the_rockies))
print(peaks_and_valleys(the_rockies))