import requests# import requests
import time# import time
import re# import regex
from datetime import datetime# import the datetime class from the datetime module
import math
# -------------------------------------------------------------
# grab the raw data from the website
with open('rain_table.rain', 'r') as file:# the rain table is saved to another file, and called here.
    text = file.read()
data = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)# first capture group is the date. middle is the whitespace. last capture group is total rain.
# print(data)

#parse the data and arrange it so it can be worked with
rainfall = []# average daily rainfall numbers as integers. These numbers are in inches (converted from tips. 1 tip = .01 inches)
for datum in data:# iterate over the list of tuples.
    rain = datum[1]# grab the daily rainfall variable.
    rain = (float(rain)) * .01# convert the daily rainfall numbers from tips to inches. the answer will be a float.
    rain = round(rain, 2)#after converting, round to the tens place.
    rainfall.append(rain)# pass the values from rain into the rainfall list


#-----------------------------------------------------------------------
# Mean
added_rainfall = sum(rainfall)# add up all the daily rainfall values as floats.
mean_rainfall = added_rainfall / len(rainfall)#take the added values, and divide by the number of values in the list.
mean_rainfall = round(mean_rainfall, 2)#round the average to the tens place.
# print(mean_rainfall)# 0.1

#------------------------------------------------------------------
# Variance

# Work out the Mean (the simple average of the numbers)
# Then for each number: subtract the Mean and square the result (the squared difference).
# Then work out the average of those squared differences. 

squared_differences = []# all squared differences are added to the list
for i in range(len(rainfall)):# iterate through the list of daily totals. 
    mean_difference = rainfall[i] - mean_rainfall# for each number: subtract the Mean 
    squared_difference = mean_difference * mean_difference# and square the result (the squared difference).
    squared_difference = round(squared_difference, 4)# round the squared difference to 4 decimal places
    squared_differences.append(squared_difference)#add squared differences to the list


added_differences = sum(squared_differences)# get the avarage of the squared differences.
added_differences = added_differences / len(squared_differences)
variance = round(added_differences, 4)
# print(variance)# 0.0478
#------------------------------------------------------------------------------------------------------------------------------
#Finding the day which had the most rain.

running_max = data[0]# the biggest running value to start with is the first tuple.
for t in data:
    if int(t[1]) > int(running_max[1]): # look into the next tuple, and compare their rainfall numbers. 
        running_max = t
print(running_max)