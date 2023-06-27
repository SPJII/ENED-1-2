# HW_14p1_Task1
# File: HW_14p1_Task1_Jones6sv.py
# Date:    11/25/2022
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
# 4-digit codes are used in multiple applications including pin numbers for debit cards and 
# combinations for bicycle locks. Develop a python script that 
# will simulate attempting to guess a 4-digit number
import random
print("Enter four digits, one at a time ")
Num1 = int(input("Digit One "))
Num2 = int(input("Digit Two "))
Num3 = int(input("Digit Three "))
Num4 = int(input("Digit four "))
ZeroRight = 0
OneRight = 0
TwoRight = 0
ThreeRight = 0
FourRight = 0
if Num1 < 0 or Num2 < 0 or Num3 < 0 or Num4 < 0 and Num1 > 9 or Num2 > 9 or Num3 > 9 or Num4 > 9:
    Num1 = float(input("Digit 1"))
    Num2 = float(input("Digit 2"))
    Num3 = float(input("Digit 3"))
    Num4 = float(input("Digit 4"))
else:
# Include a loop that will create 1000 random guesses for the 4-digit pin number.  To do this, 
# prior to the loop, type the command:   import random 
# Within the loop, generate a guess for each digit as follows: 
# G1 = random.randint(0,9)  where G1 would be the guess for the first digit
    for i in range(int(1000)):
         G1 = random.randint(0,9)
         G2 = random.randint(0,9)
         G3 = random.randint(0,9)
         G4 = random.randint(0,9)
         if G1 == Num1 and G2 == Num2 and G3 == Num3 and G4 == Num4:
             FourRight = FourRight + 1
         elif G1 != Num1 and G2 == Num2 and G3 == Num3 and G4 == Num4  or G1 == Num1 and G2 != Num2 and G3 == Num3 and G4 == Num4 or G1 == Num1 and G2 == Num2 and G3 != Num3 and G4 == Num4 or G1 == Num1 and G2 == Num2 and G3 == Num3 and G4 != Num4 :
             ThreeRight = ThreeRight + 1
         elif G1 != Num1 and G2 != Num2 and G3 == Num3 and G4 == Num4  or G1 != Num1 and G2 == Num2 and G3 != Num3 and G4 == Num4 or G1 != Num1 and G2 == Num2 and G3 == Num3 and G4 != Num4 or G1 == Num1 and G2 != Num2 and G3 != Num3 and G4 == Num4 or G1 == Num1 and G2 != Num2 and G3 == Num3 and G4 != Num4 or G1 == Num1 and G2 == Num2 and G3 != Num3 and G4 != Num4:
            TwoRight = TwoRight + 1
         elif G1 != Num1 and G2 != Num2 and G3 != Num3 and G4 == Num4 or G1 != Num1 and G2 != Num2 and G3 == Num3 and G4 != Num4 or G1 != Num1 and G2 == Num2 and G3 != Num3 and G4 != Num4 or G1 == Num1 and G2 != Num2 and G3 != Num3 and G4 != Num4:
             OneRight = OneRight + 1
         else:
             ZeroRight = ZeroRight +1
    print("There are "+str(FourRight)+" of four correct digits guesses, "+str(ThreeRight)+" of three correct digits guesses, "+ str(TwoRight)+" of two correct digits guesses, "+str(OneRight)+" of one digit guesses, and "+str(ZeroRight)+"  of Zero digit guesses.")