# 
#Unit conversion is a common task required in engineering projects.  Develop a Python script that 
#will prompt the user for the following: 
#A numerical value for pressure 
#The units for the pressure value that was entered by the user. 
#The desired units for the pressure value 
#For this task, limit the allowable units to Pascals (Pa) and pounds per square inch (psi).
Start = input("Would you like to convert a pressure value? (y/n): ")
while Start == "y": 
    NVP= input("Enter a numerical value for pressure: ")
    UnitsGiven= input("Enter the units for the pressure value that was entered by the user ((Pa) or (psi)): ")
    DesiredUnits= input("Enter the desired units for the pressure value ((Pa) or (psi)): ")
#The script should then determine if the units were entered properly (either Pa to psi or psi to Pa).  
#If so, the pressure should be converted to the new set of units and the script should output (print) 
#both the converted pressure and the new set of units. If units were not entered correctly, the 
#script should output (print) an error message to the user indicating that the units were not entered 
#correctly. 
    if UnitsGiven == "Pa" and DesiredUnits == "psi":
        print("The pressure is", float(NVP)*0.00014503773800722, "psi")
    elif UnitsGiven == "psi" and DesiredUnits == "Pa":
        print("The pressure is", float(NVP)*6894.757293168361, "Pa")
    else:
        print("Units were not entered correctly")
    Start = input("Would you like to convert a pressure value again? (y/n): ")
#The script should then ask the user if he/she would like to do another conversion.  If so, the 
#process above should be repeated.  If not, the script should terminate. 
else:
    print("Goodbye!")