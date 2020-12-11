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
    0:"zero",
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
    2:"twenty",
    3:"thirty",
    4:"fourty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"niney",
}

x = 918

hundreds_digit = x//100 #get the hundreds place
tens_digit = (x - hundreds_digit*100)//10#strip off the first number to find the tens place
teens_special = (x - hundreds_digit *100)#find the teens place 
ones_digit = x%10#the remainder will be our ones

if hundreds_digit == 0:#if there isn't a digit in the 100s place, I want to do what I did during version 1.
    if tens_digit == 0:#if only one number was entered:
        print(single[x]) 
    elif tens_digit == 1:#if the tens place is 1, look for the dictionary for that specific group of ten.
        print(teens[x])
    else: #otherwise, find the phrase that matches the tens place, and the ones place, and concatenate them together
        print(tens[tens_digit] + "-" + single[ones_digit])#otherwise, find the phrase that matches the tens place, and the ones place, and concatenate them together
        
else:#the number s in the comments are examples of what the statements catch
    if tens_digit == 0 and ones_digit == 0:#100
        print(single[hundreds_digit] + " hundred")
    elif tens_digit== 0 and ones_digit > 0:#101
        print(single[hundreds_digit] + " hundred and " + single[ones_digit])
    elif tens_digit == 1:#115
        print(single[hundreds_digit] + " hundred and " + teens[teens_special])
    elif tens_digit > 1 and ones_digit == 0:#120
        print(single[hundreds_digit] + " hundred and " + tens[tens_digit])
    else:#125
        print(single[hundreds_digit] + " hundred " + tens[tens_digit] + "-" + single[ones_digit])

