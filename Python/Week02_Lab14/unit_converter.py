units = {
  "feet":0.3048,
  "miles":1609.344,
  "meters":1.0,
  "kilometers":1000.0,
  "yards":0.9144,
  "inches":0.0254,
}

while True:
    desired_units = input("Please select the unit you wish to convert into meters. Acceptable answers are feet, miles, meters, kilometers, yards, or inches.\n>").lower().strip()#Allow the user to enter the units
    if desired_units not in units:#check to see if their answer is in the dictionary
        print(f"{desired_units} is not a valid answer.")#let the user know their answer isn't valid.
        continue#loop around to the top so the user can try again
    else:#if the desired_units are in the units dictionary:
        desired_distance = float(input("Please enter the distance:\n>"))#Allow the user to enter the distance as a float. 
        final_answer = str(desired_distance * units[desired_units])#calculate the distance, and turn it into a string.
        print(f"{desired_distance} {desired_units} is {final_answer} meters.")#display the first and final units and distances
        exit ()#end the program.