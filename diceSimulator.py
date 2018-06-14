# progam to simulate rolling a dice
# Program will run, it randomly chooses a number between 1 and 6
# program will print result
# program will ask if you would like to run it again
# HINT: set min and max number your dice can produce
# HINT: want a function that randomly grabs a number from that range and prints it
import random

print('Hello, let me roll the dice for you!')

def rollDice():
    randomNumber = random.randint(1, 6)
    return randomNumber

diceRoll = rollDice()
print('The dice rolled ' + str(diceRoll))