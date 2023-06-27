# Activity:E4_P19_jones6sv.py 
# File:    E4_P19_jones6sv.py 
# Date:    13 Febuary 2023
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
# This script will calculate the maximum height and range of a rocket
# given the initial velocity and the angle of the rocket.
#
# Rocket Trajectory
import math
def Rockets (Vo, N):
    for i in range (N):
        angle = float(input("Enter the angle in degrees: "))
        if angle < 0 or angle > 90:
            print("Invalid angle")
            continue
        angle = angle * math.pi / 180
        maxheight = (Vo ** 2 * math.sin(angle) ** 2) / (2 * 9.81)
        maxrange = (Vo ** 2 * math.sin(2 * angle)) / 9.81
        
    # round to 2 decimal place
        maxheight = round(maxheight, 1)
        maxrange = round(maxrange, 1)
        print("Velocity: ", Vo, "m/s")
        print("Angle: ", angle, "degrees")
        print("Maximum Height: ", maxheight, "m")
        print("Maximum Range: ", maxrange, "m")
vo = float(input("Enter the initial velocity: "))
n = int(input("Enter the number of angles: "))
Rockets(vo, n)