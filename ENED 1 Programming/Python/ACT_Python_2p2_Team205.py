#Determine whether a solution is acidic, basic, or neutral based on the pH.
#Prompts  the  user  for  the  pH  of  a  solution between 0-14.
SolutionPH=float(input('Enter Ph level between 0-14 = '))
if SolutionPH <= 0 or SolutionPH > 14:
    print('The pH is invalid')
# If the pH is invalid, the program should output a message
elif SolutionPH >= 0 and SolutionPH < 7:
    # 0≤ph<7 Acidic
    print("This solution is acidic")
# to the user indicating that the value entered for pH is not valid. 
elif SolutionPH == 7:
    print('This solutin is Neutral')
#pH=7 Neutral
elif SolutionPH > 7 and SolutionPH <= 14:
    print('The solution is Basic')
#7<pH≤14 Basic
else:
    print('The pH is invalid :(')
#Everything Else Invalid