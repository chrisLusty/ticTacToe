#=====================SETUP=========================

import random # used later to make a random decision on which player starts

# function to take a user input, and check that it is one of the permitted options
def takeInput(inputOptions, inputPrompt):
  valEntered = ""
  while valEntered not in inputOptions:
  	 valEntered = input(inputPrompt)
  return valEntered

# set out blank playing board  
blankBoard = """
      1       2       3
          |       |
A         |       |    
          |       |
   -------|-------|-------
          |       |
B         |       |    
          |       |
   -------|-------|-------
          |       |
C         |       |    
          |       |
"""

# define space addresses that exist on the board
allSpaces = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

# define the locations where we can later put text on the board
spaceLocations = [51, 59, 67, 142, 150, 158, 233, 241, 249]

# define the various combinations of locations that equate to a win (three in a row)
winningCombos = [{"A1", "A2", "A3"}, {"B1", "B2", "B3"}, {"C1", "C2", "C3"}, {"A1", "B1", "C1"}, {"A2", "B2", "C2"}, {"A3", "B3", "C3"}, {"A1", "B2", "C3"}, {"A3", "B2", "C1"}]

#=================START OF GAME=====================

print("""
**********************************************************
***********   Welcome to Noughts and Crosses   ***********

This is a two player game. Players must assign themselves
as either noughts (0) or crosses (X).

Please follow the on screen prompts to play. Have fun!
**********************************************************
""")

# ask who gets to have the first go, noughts or crosses
firstGoOptions = ["0","X","r"]

pickFirstGoPrompt = "Who goes first? (Enter {}, {} or {} for random): ".format(*firstGoOptions) # the asterisk unpacks the list stored in firstGoOptions, giving "format" the three separate entries it is looking for. If you just put in the list without unpacking, you get an error.
  
toStart = takeInput(firstGoOptions, pickFirstGoPrompt)

# make random choice of start-player if required
if toStart == "r":
  toStart = random.choice(["X","0"])
  print("\n Random choice: player \"{}\" starts.".format(toStart))

print(blankBoard)

#================INITIALISE VARS===================

availableSpaces = allSpaces.copy() # weirdly, if you set list2 = list1, changes made to list2 are reflected in list1. Therefore use copy() to make list2 a separate list.

currentTurn = toStart

ownedByX = set() # create blank set to store locations owned by X
ownedBy0 = set() # create blank set to store locations owned by 0

workingBoard = blankBoard # initialise a version of the board to be filled in during game

timeToEnd = False # initialise a boolean to be used to end the game when a player wins

#==============MAIN GAMEPLAY LOOP==================

for turns in range(9):

	requestSpacePrompt = "Player {}, please enter a coordinate: ".format(currentTurn)
	
	requestedSpace = takeInput(availableSpaces, requestSpacePrompt)
	
	availableSpaces.remove(requestedSpace)
	
	chosenSpaceIndex = allSpaces.index(requestedSpace)
	
	# you can't change a character within an existing string in Python. To get round, convert string to list, switch out the list item to represent the player move, then convert back to a string.
	workingBoardList = list(workingBoard)
	workingBoardList[spaceLocations[chosenSpaceIndex]] = currentTurn
	workingBoard = "".join(workingBoardList)
	
	print(workingBoard)
	
	if currentTurn == "X":
		
		ownedByX.add(requestedSpace) # update set containing locations owned by X
		currentTurn = "0" # switch to 0's turn for next loop
		
		# loop through the various winning combination options, and check if any of them form a subset of the locations owned by X. If so, display message and prepare to end programme.
		for i in range(len(winningCombos)):
			if winningCombos[i].issubset(ownedByX) == True:
				print("""
	********************
	********************
	***    X wins!   ***
	********************
	********************
				""")
				timeToEnd = True
				break
	else:
		
		ownedBy0.add(requestedSpace) # update set containing locations owned by 0
		currentTurn = "X" # switch to X's turn for next loop
		
		# loop through the various winning combination options, and check if any of them form a subset of the locations owned by 0. If so, display message and prepare to end programme.
		for i in range(len(winningCombos)):
			if winningCombos[i].issubset(ownedBy0) == True:
				print("""
	********************
	********************
	***    0 wins!   ***
	********************
	********************
				""")
				timeToEnd = True
				break
	
	# End programme if either of the players has won
	if timeToEnd == True:
		break

#======================END===========================


