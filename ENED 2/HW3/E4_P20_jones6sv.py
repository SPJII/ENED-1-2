# Activity:E4_P20_jones6sv.py 
# File:    E4_P20_jones6sv.py 
# Date:    13 Febuary 2023
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
# This program will read the x and y coordinates from a file and determine if the coordinates are in the acceptable range. 
# If the coordinates are not in the acceptable range, the program will print the error in the x and y coordinates.
# A team of ENED 1120 students have built their robot and are ready to test how well their robot will be able to navigate to a specific box and a specific shelving unit.  For their first test, they will see how well their robot can navigate to box 2 on shelving unit C1.
Xideal = 19.3125
Yideal = 59
X = float(input("Enter the x coordinate: "))
Y = float(input("Enter the y coordinate: "))
def Fuction(x,y):
    Xerror = x - Xideal
    Yerror = y - Yideal
    Robot = open("Robot.txt", "r")
    for line in Robot:
        x, y = line.split()
        x = float(x)
        y = float(y)
        if x >= 19.125 and x <= 19.5 and y >= 58.75 and y <= 59:
            print("Both x and y positions are in the acceptable range.")
        elif x >= 19.125 and x <= 19.5:
            print("Only the x position is in the acceptable range.")
        elif y >= 58.75 and y <= 59:
            print("Only the y position is in the acceptable range.")
        else:
            print("Neither x nor y position is in the acceptable range.")
        print("The error in the x position is", Xerror, "inches.")
        print("The error in the y position is", Yerror, "inches.")
    Robot.close()
    #  Open a new text file, E4_UCusername.txt for writing, and write two columns: 
    # Xerror and Yerror to the file.  The values should include four places behind the decimal point.
    E4_jones6sv = open("E4_jones6sv.txt", "w")
    E4_jones6sv.write("Xerror\tYerror\n")
    E4_jones6sv.write(str(Xerror) + "\t" + str(Yerror) + "\n")
    E4_jones6sv.close()
function(X,Y)