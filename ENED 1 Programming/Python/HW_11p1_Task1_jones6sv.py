#  11p1 HW :Task 1
# File: ACT_Python_HeaderTemplate_Team210_jones6sv.py 
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
# Code that implements the algorithm Gam=1/Sqrt(1-(v/c)**2), p=m*v, and q=m*v*Gam. Then prints output with two decimal points, and with the appropriate units. 

import math
c = float(input('Speed of light in m/s = '))
v = float(input('Speed of mobile in m/s = '))
m = float(input('Mass of moblie in Kg = '))
d = (1-(v/c)**2)
Gam = (1/math.sqrt(d))
p = m*v
q = m*v*Gam
print("Gam = {0:.2e},".format(Gam))
print("q = {0:.2e} kg*m/s,".format(q))
print("p = {0:.2e} kg*m/s,".format(p))