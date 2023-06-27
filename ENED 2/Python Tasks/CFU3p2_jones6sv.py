# In a simple circuit with a resistor and a capacitor (RC circuit), 
# the time it takes for the capacitor to charge or discharge depends on the time constant, tau
# where R is the resistance (in Ohms), C is the capacitance (in Farads), and tau is the time constant (in seconds).

# The first column consists of resistor (R) values in Ohms.  The second column consists of capacitor (C) values in Farads.
# Read the values for R and C from the text file

# For each pair of R and C values (each row in the text file), compute the time constant, tau, and save the time constants in a list
# Find and output (using print, not write) the maximum time constant and the corresponding resistor and capacitor values
# Write the list of time constants to a text file named, CFU3p2.txt in a single column with two places behind the decimal point
RList = []
Clist = []
Rc = open("RC.txt", "r")
for each in Rc:
    RList.append(float(each.split()[0]))
    Clist.append(float(each.split()[1]))
for each in RList:
    print(each)
for each in Clist:
    print(each)
Rc.close()
Tau = []
for each in range(len(RList)):
    Tau.append(RList[each]*Clist[each])
print("The maximum time constant is", max(Tau), "and the corresponding resistor and capacitor values are", RList[Tau.index(max(Tau))], "and", Clist[Tau.index(max(Tau))])
RcOut = open("CFU3p2.txt", "w")
for each in range(len(Tau)):
    RcOut.write(str(each))
    RcOut.write("Tau value is {0:.2f}\n".format(Tau[each]))
RcOut.close()