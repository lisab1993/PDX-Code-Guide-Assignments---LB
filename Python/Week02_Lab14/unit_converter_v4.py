
to_meters = {#convert user's distance in starting units to meters.
    "feet":0.3048,
    "miles":1609.344,
    "meters":1.0,
    "kilometers":1000.0,
    "yards":0.9144,
    "inches":0.0254,
}

from_meters = {#convert the user's distance from meters to requested units.
    "feet":3.28,
    "miles":0.000621371,
    "meters":1,
    "kilometers":0.001,
    "yards":1.09361,
    "inches":39.3701,
}

while True:
    starting_units = input("Please select your starting units. Acceptable answers are feet, miles, meters, kilometers, yards, or inches.\n>").lower().strip()#Allow the user to enter the units
    if starting_units not in to_meters:#check to see if their answer is in the dictionary
        print(f"{starting_units} is not a valid answer.")#let the user know their answer isn't valid.
        continue#loop around to the top so the user can try again
    else:#if the desired_units are in the to_meters dictionary:
        requested_units = input("Please select the unit you wish to convert to:\n>")#prompt the user for their final units
        if requested_units not in to_meters:#check if their answer is valid by looking in the to_meters dictionary.
            print(f"{requested_units} is not a valid answer.")#let the user know if it isn't.
            continue#and ask until we get a valid answer.
        else: 
            desired_distance = float(input("Please enter the distance:\n>"))#Allow the user to enter the distance as a float. 
            in_meters = desired_distance * to_meters[starting_units]#calculate the distance in meters.
            target_number = in_meters * from_meters[requested_units]#calculate the goal number
            print(f"{desired_distance} {starting_units} is {target_number} {requested_units}.")#display a sentence with the conversion.
            exit()