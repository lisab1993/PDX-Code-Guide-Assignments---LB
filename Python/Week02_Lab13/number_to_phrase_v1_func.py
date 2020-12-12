
single = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    0:"",
}

teens = {
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
}

tens = {
    0:"",
    2:"twenty",
    3:"thirty",
    4:"fourty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"niney",
}

    
def number_to_phrase(number):#
    '''turns a number into its written counterpart'''
    tens_digit = number//10#find the tens digit and ignore the ones place
    ones_digit = number%10#find the remainder that is the ones digit

    if tens_digit == 0:#if a single digit is entered, only use the dictionary for single numbers
        return single[number]#return the value from the dictionary
    elif tens_digit == 1:#if 10-19 entered, use that specific dictionary to account for the inconsistencies in English
        return teens[number]
    else:
        output = (tens[tens_digit] + "-" + single[ones_digit])#otherwise, find the value in the tens dictionary, and concatenate it with the value from the singles dictionary
        return output


print(number_to_phrase(25))#print the results of the function, using 13 as our initial number
       
