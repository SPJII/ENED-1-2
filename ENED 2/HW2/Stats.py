# Activity: HW2p1_Task1_jones6sv.py 
# File:    Stats.py
# Date:    23 January 2023
# By:      Steven Jones II
# Section: 1120
# Team:    Team 242
#
# ELECTRONIC SIGNATURE
# Steven Jones II
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# 
# Create a Python function named Stats that: 
# Has one input argument:  a list of numerical values of any length. 
# Calculates the average and standard deviation for the data in the list. 
# Note: use the equations given in class (and loops) to make the calculations
# – do not use the functions from the Python Statistics Library. 
# Returns the average and standard deviation. 
def Stats(list):
    # Calculate the average
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    average = sum / len(list)
    # Calculate the standard deviation
    sum = 0
    for i in range(len(list)):
        sum = sum + (list[i] - average)**2
    std = (sum / len(list))**0.5
    return average, std
print(Stats([2, 4, 7, 10, 16, 17, 20]))