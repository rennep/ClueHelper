from AddingFunctions import *
from ClearingFunctions import *
from RumorBuilder import *
from GameSetup import *
rumor = RumorBuilder()
name = input("Enter the name of the player who passed:  ")
name = name.lower()
print(PlayersPossibleHands[name])
PlayersPossibleHands[name] = ClearPossibleHand(name, rumor, PlayersPossibleHands)
print(PlayersPossibleHands[name])