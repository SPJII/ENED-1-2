# HW_13p1_Task2
# File: HW_13p1_Task2_Jones6sv.py
# Date:    11/21/2022
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
# Based on the given values, the code then calculates the density (g/cm3) and 
# then determine whether the inputted crystal structure for the metal make sense based on the 
# difference between actual density and the calculated density.  
#
import math
Metal = input("Enter the Metal (Al, Co, or Cr) ")
CS= input("Enter the crystal structure (BCC, FCC, or HCP) ")
#Choose a Metal, each metal has their own If condition and they're listed below.
if Metal == "Al":
    Mass = 26.98
    Rnm = .1431
    ADensity = 2.7
elif Metal == "Co":
    Mass = 58.93
    Rnm = .1253
    ADensity = 8.9
elif Metal == "Cr":    
    Mass = 52.00
    Rnm = .1249
    ADensity = 7.2
else:
    print("invaild metal")
#Choose a Crystal structure, each Crystal structure has their own If condition and they're listed below.
if CS == "BCC":
   a = 4*Rnm/ math.sqrt(3)
   V = a**3
   NumOfAtom = 2
elif CS == "FCC":
    a = 4*Rnm/ math.sqrt(2)
    V = a**3
    NumOfAtom = 4 
elif CS == "HCP": 
    a = 2*Rnm
    c = 1.63*a
    V = ((3* math.sqrt(3)*c*a**2)/2)
    NumOfAtom = 6
else:  
    print('Invaild Crystal Structure')
# Mass of an atom is Molar mass*(var(Mass))* divided by Avogado’s constant (6.022e23 atoms/mol)
MA = Mass/6.022*10**23
# CDensity is Calulated Density, 
# 𝐶𝑎𝑙𝑐𝑢𝑙𝑎𝑡𝑒𝑑 ⁡𝐷𝑒𝑛𝑠𝑖𝑡𝑦 = ⁡𝑀𝑎𝑠𝑠 ⁡𝑜𝑓⁡ 𝑡ℎ𝑒⁡ 𝐴𝑡𝑜𝑚 × 𝑛𝑢𝑚𝑏𝑒𝑟⁡ 𝑜𝑓⁡ 𝑎𝑡𝑜𝑚𝑠 ⁡𝑖𝑛 ⁡𝑒𝑎𝑐ℎ⁡ 𝑢𝑛𝑖𝑡⁡ 𝑐𝑒𝑙𝑙
#                           /𝑉𝑜𝑙𝑢𝑚𝑒⁡ 𝑜𝑓 ⁡𝑈𝑛𝑖𝑡⁡𝐶𝑒𝑙𝑙
CDensity =  (MA*NumOfAtom/V)/10**25
# %⁡𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑐𝑒 = |𝐴𝑐𝑡𝑢𝑎𝑙⁡𝑑𝑒𝑛𝑠𝑖𝑡𝑦−𝑐𝑎𝑙𝑐𝑢𝑙𝑎𝑡𝑒𝑑⁡𝑑𝑒𝑛𝑠𝑖𝑡𝑦| / 𝐴𝑐𝑡𝑢𝑎𝑙⁡𝑑𝑒𝑛𝑠𝑖𝑡𝑦 ∗ 100%
PDiff = (abs(ADensity-CDensity)/ADensity)*1
#
print("The calculated density of "+ str(Metal) +" with "+ str(CS)+"is"+str(round(CDensity,2))+"g/cm^3") 
if PDiff > .05 or PDiff < 0.0:
    print("The entered Crystal structure may be wrong")
else:
    print("The Difference is "+str(round(PDiff*100,2))+ "% thus "+str(CS)+" is the Crystal Structure")
    