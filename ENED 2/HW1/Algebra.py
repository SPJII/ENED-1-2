# Activity Python 5: Task 1
# File: Algebra_jones6sv.py
# Date:    17 January 2023
# By:      Steven Jones II
# Section: 1120
# Team:    Team IDK
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
# Consider the two linear equations shown below: a1x+b1y=c1 and a2x+b2y=c2 
# A unique solution for x and y can be determined as long as the following is true: a1∙b2−a2∙b1≠0 
#
# Develop a Python Function named Algebra that has six input arguments: a1, b1, c1, a2, 
# b2, and c2. 
# Within the function, determine whether or not a unique solution for x and y exists. 
# If  a  unique  solution  does  not  exist,  output  a  statement  indicating  that  there  is  no  unique 
# solution for x and y. 
# If  a  unique  solution  does  exist,  determine  and  output  the  values  for  x  and  y  using  three 
# places behind the decimal. 

# Use the elimination method to determine the appropriate equations for x and y in terms of the input 
# arguments. 

def Algebra(a1, b1, c1, a2, b2, c2):
    if a1*b2-a2*b1 != 0:
        x = (c1*b2-c2*b1)/(a1*b2-a2*b1)
        y = (a1*c2-a2*c1)/(a1*b2-a2*b1)
        print("x = %.3f" % x)
        print("y = %.3f" % y)
    else:
        print("There is no unique solution for x and y.")
        return(x,y)
Algebra(2,3,2,5,6,1)
