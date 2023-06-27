# 1) Imports the random library using the command:  import random.
import random 
# 2) Prompts the user for the number of times, N, to roll two dice (should be a positive 
# integer).  
N = int(input("How many times do you want to roll the dice? "))
# 3) Checks to make sure N is positive and continues to prompt until N is greater than zero.  
# Note: you don’t have to check if N is an integer because the int command with throw an 
# error if user enters a decimal number. 
while N <= 0:
    N = int(input("Please enter a positive integer: "))
# 4) Have a loop that rolls two dice N times and stores the sum of the two dice in a list.  Use a 
# command such as:  Dice1 = random.randint(1,6) to simulate a dice roll. 
# 5) Has a second loop that goes through the list and counts the number of times the sum of 
# the two dice is 7.
dice = []
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
for i in range(N):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice.append(dice1 + dice2)
    dice7 = dice.count(7)
print("The list of dice rolls is: ", dice)
print("The number of times the sum of the two dice is 7 is: ", dice7)
# 6) Outputs both the list and the count. 