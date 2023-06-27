# Activity Python 1: Task 3
# File:# HW_11p1_Task3_jones6sv.py 
# Date:    11/7/2022
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
# Inputs the amplitude of the incident wave 𝐄𝟎𝐢, the intrinsic impedances (η1, and η2), the angle of 
# the incident wave, 0i, and the angle of the transmitted wave, 0t. Compute the amplitude of the reflected wave(𝐄𝟎𝐫) 
# and transmitted wave (𝐄𝟎𝐭).The wave amplitudes should then be displayed the Python IDLE Shell with two places after the 
# decimal point using Python’s print function.  
import math
Eio = float(input('Enter the amplitude of the incident wave =' ))
n1 = float(input('Enter the intrinsic impedance of medium 1 =' ))
n2 = float(input('Enter the intrinsic impedance of medium 2 = ')) 
Oi = float(input('Enter the angle of the incident wave (in Degrees) = '))
Oi = Oi*(math.pi/180)
Ot = float(input('Enter the angle of the transmitted wave (in Degrees) = '))
Ot = Ot*(math.pi/180)
Eot = ((2*n2*math.cos(Oi))/(n2*math.cos(Ot)+n1*math.cos(Oi)))*(Eio)
Eor = (n2*math.cos(Oi)-n1*math.cos(Ot))/(n2*math.cos(Oi)+n1*math.cos(Ot))*(Eio)
print("The amplitude of the transmitted wave is E_t = {0:.2f} v/m,".format(Eot))
print("The amplitude of the reflected wave E_r = {0:.2f} v/m,".format(Eor))