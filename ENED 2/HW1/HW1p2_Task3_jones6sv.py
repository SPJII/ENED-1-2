# Activity Python 5: Task 3
# File: HW_1p2_Task3_jones6sv.py
# Date:    17 January 2023
# By:      Steven Jones II
# Section: 1120
# Team:    IDK
#
# ELECTRONIC SIGNATURE
# Paulo Snoddy
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# Prompt the user for the Alloy Number (see Task 2). 
# Check to make sure the Alloy Number is valid – if not, continue to prompt for an Alloy 
# Number until the user enters a valid value. 
# Prompt the user for required number of pounds (lbs.) of the alloy (use float not int). 
# Check to make sure the number of pounds is valid – if not continue to prompt until the 
# user enters a positive number of pounds. 
# Call the function, Alloys, developed in Task 2 to determine the cost of the Alloy. 
# Output (print) the cost with two places behind the decimal point. 
import Alloys
An = float(input("What is the alloy number?"))
if An == 2024 or An == 7075 or An == 356:
    lbs = float(input("What is the number of required pounds of the alloy?"))
    while lbs < 0:
        lbs = float(input("Please enter a positive value for the weight of alloy in pounds"))
elif An != 2024 and An != 7075 and An != 356:
    while An != 2024 and An != 7075 and An != 356:
        An = float(input("Please enter a valid alloy number"))
    lbs = float(input("What is the number of required pounds of the alloy?"))
    while lbs < 0:
        lbs = float(input("Please enter a positive value for the weight of alloy in pounds"))
TotalCost =Alloys.Alloys(An,lbs)