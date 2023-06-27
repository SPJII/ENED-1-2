# Activity:HW2p1_Task3_jones6sv.py 
# File:    HW2p1_Task3_jones6sv.py 
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
# Create a 2d list of Resistor Values: 
# Using a loop, for each row in R, compute the resistance if the two resistors are combined 
# in series and save the results in a list. 
# Using a loop, for each row in R, compute the resistance if the two resistors are combined 
# in parallel and save the results in a list.  Note: can do this within same loop used to 
# calculate series resistances. 
# Output each pair of resistor values and the corresponding series resistance and parallel resistance. 
# Use one place behind the decimal point for the parallel resistance. 
# Using a loop, for each row in R, compute the resistance if the two resistors are combined in series and save the results in a list. 
# Note: can do this within same loop used to calculate series resistances. 
# Output each pair of resistor values and the corresponding series resistance and parallel resistance. 
# Use one place behind the decimal point for the parallel resistance. 
# print R1, r2, Rseries, Rparallel
R = [[100, 200], [810, 560], [470, 360]] # 2d list of resistor values
def Circuit(r):
    for i in range(len(r)):
# R1 and R2
        R1 = r[i][0]
        R2 = r[i][1]
# Rseries
        r[i] = r[i][0] + r[i][1]
# Rparallel
        r2= 1 / ((1 / R1) + (1 / R2))
# print R1, r2, Rseries, Rparallel
        print("R1 =",R1,"Ohms,","R2 =",R2,"Ohms,","Rseries =",r[i], "Ohms,","Rparallel =",round(r2,1),"Ohms.",end="\n")
    return R1, R2, r, r2
Circuit(R)

