# Activity Python 5: Task 2
# File: Alloys_jones6sv.py
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
# Aluminum alloys are made by adding other elements to aluminum to improve its properties, such 
# as hardness or tensile strength.  The following tables show the composition of three commonly 
# used alloys which are known by their alloy numbers (2024, 7075, and 356), and the cost for 
# various materials. 
#
# Develop a Python Function named Alloys that has two input arguments:  the Alloy 
# Number and the number of required pounds (lbs.) of the alloy.
# The function should compute and return the total cost for the number of pounds of the 
# specified alloy. 
#
# Assume that the user inputs will be valid; that is, the alloy number will indeed be 
# 2024 or 7075 or 356 and the number of required pounds will be positive. 
def Alloys(AlloyNumber, Lbs):
    if AlloyNumber == 2024:
        Al = .935 * Lbs
        Cu = .44 * Lbs
        Mg = .015 * Lbs
        Mn = .006 * Lbs
        Si = 0 * Lbs
        Zn = 0 * Lbs
    elif AlloyNumber == 7075:
        Al = .903 * Lbs
        Cu = .016 * Lbs
        Mg = .025 * Lbs
        Mn = 0 * Lbs
        Si = 0 * Lbs
        Zn = .056 * Lbs
    elif AlloyNumber == 356:
        Al = .927 * Lbs
        Cu = 0 * Lbs
        Mg = .003 * Lbs
        Mn = 0 * Lbs
        Si = .07 * Lbs
        Zn = 0 * Lbs
    else:
        print("Invalid Alloy Number")
    Alc = Al * 1.08
    Cuc = Cu * 3.81
    Mgc = Mg * 5.27
    Mnc = Mn * 4.00
    Sic = Si * 5.00
    Znc = Zn * 1.35
    TotalCost = Alc + Cuc + Mgc + Mnc + Sic + Znc
    print("The total cost for the number of pounds of the alloy is %.2f $" % TotalCost)
    return TotalCost    