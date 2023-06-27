# HW_14p1_Task2
# File: HW_14p1_Task2_Jones6sv.py
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
# simulate a two-player dice 
# Each player has two dice and each player starts with a score of 0. 
# Player 1 rolls both dice.  If a five is rolled on either die, Player 1’s turn is over.  If not, 
# Each time a player rolls, the script should display the player’s roll and the updated score (if a five 
# is not rolled) or a message that the player’s turn has ended (if a five is rolled). 
# When one of the player’s reaches a score of at least 50, the script should output which player is 
# the winner and the final scores for each player. 
import random
Start = (input("Please enter Player 1 or Player 2 = "))
Player1Score = 0
Player2Score = 0
# 1. Each player has two dice and each player starts with a score of 0. 
while Player1Score < 50 and Player2Score < 50:
# 2. Player 1 rolls both dice.  If a five is rolled on either die, Player 1’s turn is over.  If not, 
# Player 1’s score increases by the sum of the two dice.  Player 1 continues to roll and 
# score until a five is rolled on either die.  It then becomes Player 2’s turn. 
    if Start == "Player 1":
        print("player One's turn")
        P1Dice1 = random.randint(1,6)
        P1Dice2 = random.randint(1,6)
        
        if P1Dice1 == 5 or P1Dice2 == 5:
            print("Player 1 turn over")
            Start = "Player 2"
        else:
# 3. Player 2 follows the same rules.  Increase the score by the sum of the two dice as long as 
# a five is not rolled on either die.  As soon as a five is rolled, it becomes Player 1’s turn 
# again. 
            Player1Score = Player1Score + P1Dice1 + P1Dice2 
            print(str(P1Dice1)+" "+str(P1Dice2)+" Player One Score "+str(Player1Score))
    if Start == "Player 2":
        print("Player Two's turn")
        P1Dice1 = random.randint(1,6)
        P1Dice2 = random.randint(1,6)
        if P1Dice1 == 5 or P1Dice2 == 5:
            print("Player 2 turn over")
            Start = "Player 1"
        else:
            Player2Score = Player2Score + P1Dice1 + P1Dice2 
            print(str(P1Dice1)+" "+str(P1Dice2)+" Player Two Score "+str(Player1Score))
# 4. Play continues until one of the players reaches a score of at least 50. 
if Player1Score>50:
    print("winner is 1")
    print("Player One Score "+str(Player1Score))
elif Player2Score> 50:
    print("winner is 2")
    print("Player Two Score "+str(Player2Score))