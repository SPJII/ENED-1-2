# Activity Python 1: Task 3
# File:  HW_11p1_Task2_jones6sv.py
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
# The VI Block diagram and Front Panel takes Vo,K,and m then outputs V(in/s). I rewrote the program in Python script 
# that implements the same functionality and prints the output with two decimal points and with the appropriate units.  
import math
Vo= float(input('Vo(m/s) = '))
Vo = ((Vo*39.4)**2)
K = float(input('K((kgm**2)/s) = '))
K = K*15477.02
m = float(input('m(kg) = '))
m = m*.07
v = math.sqrt(Vo-(K/m))
print("V = {0:.2f} in/s,".format(v))