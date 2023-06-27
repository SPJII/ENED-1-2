
# File: ACT_Python_HeaderTemplate_Team210_jones6sv.py 
# Date:    31 October 2022
# By:      Steven Jones II
# Section: 16
# Team:    210
# 
# ELECTRONIC SIGNATURE
# Steven Paul Jones II
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# Top and Right View. There are two dimensions presented in each view, as shown in the following table.
#Prompt the user to input a specific Orthographic view (Front, Top or Right)
Face = input("Which Orthographic view; ")
Top = "Width and Depth"
Front = "Height and width "
Right = "Depth and Height"
#If the view is not valid, print a message to the user that the view chosen is not valid
if Face != Front or Top or Right:
    print('The view is not valid')
#If the view is valid, print out the corresponding Dimensions for the chosen view
elif Face == Front:
    print(Front)
elif Face == Top:
    print(Top)
elif Face == Right:
    print(Right) 
    