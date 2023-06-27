# Activity:HW3p2_Task1_jones6sv.py 
# File:    HW3p2_Task1_jones6sv.py 
# Date:    31 January 2023
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
# Antoine’s Equation describes the relationship between vapor pressure and temperature for a pure 
# substance.  The equation is Antoine’s Equation describes the relationship between vapor pressure and temperature for a pure 
# log10(P)=A−B/(C+T) 
# P = vapor pressure (mmHg) 
# T = temperature (oC) 
# A, B, C = constants for each substance
A = []
B = []
C = []
Tmin = []
Tmax = []
T = []
Plist = []
Task1 = open("Task1.txt", "r")
for each in Task1:
    A.append(float(each.split()[0]))
    B.append(float(each.split()[1]))
    C.append(float(each.split()[2]))
    Tmin.append(float(each.split()[3]))
    Tmax.append(float(each.split()[4]))
    T.append(float(each.split()[5]))
    if T[each] > Tmin[each] and T[each] < Tmax[each]:
        P = 10**(A[each]-(B[each]/(C[each]+T[each])))
        Plist.append(P)
    else:
        Plist.append(-9999)
Task1.close()

print(Plist)
Task1_Results=open("Task1_Results.txt", "w")
Task1_Results.write("{0:15} {1:15} {2:10.2f}".format("Substance", "Temperature", "Pressure"))
for each in Plist:
    Task1_Results.write("{0:15} {1:15} {2:10.2f}".format("Substance", "Temperature", "Pressure"))
Task1_Results.close()

                    