# E3_P24
# File: E3_P24_jones6sv.py
# Date:    7 December 2022
# By:      Steven Jones II
# Section: 16
# Team:    205
# 
# ELECTRONIC SIGNATURE
# Steven Paul Jones II
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# Prompts the user for a model type (linear, power, or exponential)
# Checks for a valid model type.  If the user entered an invalid model type,
# prints a message that the model type is invalid, and the program simply ends.
# If the user entered a valid model type, prompts the user for the x and y coordinates of two data points: (x1, y1) and (x2, y2)
# Computes and outputs (prints) the equation for the model (see table below for the appropriate formulas).  
# When outputting the equation for the model, the constants, m and b, should be displayed with four places behind the decimal point.
import math
ModelType = input("Enter a model type (linear, power, or exponential): ")
if ModelType == "linear":
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    print("y = " + str(m) + "x + " + str(b))
elif ModelType == "power":
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    m = math.log(y2 / y1) / math.log(x2 / x1)
    b = y1 / (x1 ** m)
    print("y = " + str(b) + "x^" + str(m))
elif ModelType == "exponential":
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    print("y = " + str(m) + "e^(" + str(b) + "x)")
else:
    print("Invalid model type")