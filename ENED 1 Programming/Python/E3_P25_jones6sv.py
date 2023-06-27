# E3_P25
# File: E3_P25_jones6sv.py
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
# A sequence of values is determined by the following equation: yn = q*yn-1+r*yn-2
#
# where q and r are constants and y0 and y1 are initial values.
# Write a program that Prompts the user for the two constants (floats):  q and r.  
# Determines and outputs (prints) whether or not the sequence will oscillate (i.e., increase and decrease). 
#
# To do this, first compute d=q^2+4r
# If d > 0, the sequence will not oscillate.  If d < 0, the sequence will oscillate.
# Next, determine whether or not the sequence will converge to zero.  
# The conditions under which the sequence will converge depend on whether d > 0 or d < 0 
#
# If the sequence does not converge, print a message to the user that the sequence does not converge to zero.
# If the sequence does converge to zero, print a message that the sequence will converge to zero.
#
# Next, prompt the user for the number of y-terms to be computed.  Check to make sure the number of terms is positive (greater than 0).
# If not, continue to prompt until the user enters in a positive number of terms.
# Using a loop, compute the required number of terms for the sequence and output (print) the results.
import math
q = float(input("Enter q: "))
r = float(input("Enter r: "))
# Determines and outputs (prints) whether or not the sequence will oscillate
d=(q**2)+(4*r)
if d >= 0:
    print("The sequence will not oscillate")
elif d <=0:
    print("The sequence will oscillate")
 # If the sequence does not converge, print a message to the user that the sequence does not converge to zero.
    if abs(q+math.sqrt(d)/2) > 1 and abs(q-math.sqrt(d)/2) > 1:
        print("The sequence does not converge to zero")     
# Next, prompt the user for the number of y-terms to be computed.
    else:
        print("The sequence does converge to zero")
        yTerm = int(input("Enter the number of y-terms to be computed: "))
        if yTerm <= 0:
            print("The number of terms must be positive")  
            yTerm = int(input("Enter the number of y-terms to be computed: "))
        else:
            y1 = 0
            y2 = 0
            for i in range(yTerm):
                y1 = y1 +yTerm
                y2 = y2 +yTerm
                y1 = q*y1+r*y2
                print(y1)
    