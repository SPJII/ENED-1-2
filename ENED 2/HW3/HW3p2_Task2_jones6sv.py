# Activity:HW3p2_Task2_jones6sv.py 
# File:    HW3p2_Task2_jones6sv.py 
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
#
# Open the file and take a look at it.  Year is in the first column, January Daily Temperatures are in 
# the second column, and July Daily Temperatures are in the third column.  There are no column 
# headers.  Note that the first 31 rows all have the same year, 1950, since there are 31 days in both 
# January and July.  The next 31 rows are for 1951, etc. 
# Read the data from the text file, Task2.txt 
#
Task2 = open("Task2.txt", "r")
Jan = []
Jul = []
for each in Task2:
    Jan.append(float(each.split()[1]))
    Jul.append(float(each.split()[2]))
Task2.close()
JanAvg = sum(Jan)/len(Jan)
JulAvg = sum(Jul)/len(Jul)
print(JanAvg)
print(JulAvg)
Task2_Results=open("Task2_Results.txt", "w")
Task2_Results.write("{0:15} {1:15} {2:10.2f}".format("Year", "January Average", "July Average"))
Task2_Results.write("{0:15} {1:15} {2:10.2f}".format("1950", JanAvg, JulAvg))
Task2_Results.close()

    
