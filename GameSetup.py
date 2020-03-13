AllCards = {}
SetOfRooms = set()
SetOfWeapons = set()
SetOfCharacters = set()

NumberOfRooms = input("How many rooms are there?  ")
NumberOfRooms = int(NumberOfRooms)

for j in range(0, NumberOfRooms):
    SetOfRooms.add(input("Enter the name of the room: ").lower())

AllCards['rooms'] = SetOfRooms

NumberOfWeapons = input("How many weapons are there?  ")
NumberOfWeapons = int(NumberOfWeapons)

for j in range(0, NumberOfWeapons):
    SetOfWeapons.add(input("Enter the name of the weapon: ").lower())

AllCards['weapons'] = SetOfWeapons

NumberOfCharacters = input("How many characters are there?  ")
NumberOfCharacters = int(NumberOfCharacters)

for j in range(0, NumberOfCharacters):
    SetOfCharacters.add(input("Enter the name of the character: ").lower())

AllCards['characters'] = SetOfCharacters


NumberOfPlayers = input("How many players are there?  ")
NumberOfPlayers = int(NumberOfPlayers)
PlayersPossibleHands = {}
PlayersActualHands = {}
Rumors = {}

for j in range(0, NumberOfPlayers):
    name = input("Enter Name: ").lower()
    PlayersPossibleHands[name] = AllCards
    PlayersActualHands[name] = set()
    Rumors[name] = {}

print(PlayersPossibleHands)
print(PlayersActualHands)
print(Rumors)