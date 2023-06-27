# HW_13p1_Task1
# File: HW_13p1_Task1_Jones6sv.py
# Date:    11/20/2022
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
# The code takes Pressure (atm) and Temperature (in Celsius) as inputs and output the 
# corresponding phase state of water (liquid, gas, ice or other states as indicated in the flow diagram) 
# Assuming line BD is vertical at T = 273.15K for simplified calculation
import math
P= float(input("Enter the pressure(atm) "))
T= float(input("Enter the Temperature(c) "))
T = T + 273.15
# converts Temp from (c) to (K)
P1 = (0.006*math.exp( 6293 *( 1/273.15 - 1/T ) - 0.56*math.log( T/273.15 )))
#^ Sublimation-deposition line
P2 = (0.006*math.exp( 6808 *( 1/273.15 - 1/T ) - 5.09*math.log ( T/273.15 )))
#^ Vaporization line
if T > 647 and P > 218:
    print("Super critical liquid")
elif T < 273.15 and P > P1:
    print("Solid")
elif T > 273.15 and P > P2:
    print("liquid")
else:
    print("Gas")