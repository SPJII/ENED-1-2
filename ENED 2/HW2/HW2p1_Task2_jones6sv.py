# Activity:HW2p1_Task2_jones6sv.py 
# File:    HW2p1_Task2_jones6sv.py 
# Date:    17 January 2023
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
# Antoine’s Equation describes the relationship between vapor pressure and temperature for a pure 
# substance.  The equation is: log10(𝑃)=A− (B/(C+T))
# P = vapor pressure (mmHg) 
# T = temperature (oC) 
# A, B, C are constants that depend on the substance
#
# Prompt the user for the substance (Methanol, Butane, or Octane)
#Check to make sure the substance entered is valid.  If not, continue to prompt until a valid substance is entered. 
# a loop will certainly prove useful for creating the list of temperature.  The list of temperatures will be different for each substance. 
Substance = input("Enter the substance (Methanol, Butane, or Octane): ")
if Substance == "Methanol":
    Tlist = [-16, -10.4, -4.7, .89, 6.5, 12.1, 17.8, 23.4, 29, 34.7, 40.3, 45.9, 51.6, 57.2, 62.8, 68.5, 74.1, 79.7, 85.4, 91, 96.6]
    A = 8.0724
    B = 1574.99
    C = 238.87
elif Substance == "Butane":
    Tlist = [-78, -72.9, -67.8, -62.7, -57.6, -52.5, -47.4, -42.3, -37.2, -32, -26.9, -21.8, -16.7, -11.6, -6.5, -1.4, 3.7, 8.8, 13.9, 19, 24.1]
    A = 6.80896
    B = 935.86
    C = 238.73
elif Substance == "Octane":
    Tlist = [19, 26, 33, 40, 47, 54, 61, 68, 75, 82, 89, 96, 103, 110, 117, 124, 131, 138, 145, 152, 159]
    A = 6.9094
    B = 1349.82
    C = 209.385
else:
    print("Invalid substance")
    Substance = input("Enter the substance (Methanol, Butane, or Octane): ")
Plist = [0] * len(Tlist)
for i in range(len(Tlist)):
    math = A - (B/(C + Tlist[i]))
    Value = 10**math
    Plist[i] = Value
    print("Temperature = %.3f" %Tlist[i], "Pressure = %.3f" %Plist[i])
