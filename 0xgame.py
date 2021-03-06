#=====================SETUP=========================

import random # used later to make a random decision on which player starts
import os # used to send a "clear" command to the shell to keep all turns shown on a single board

# function to take a user input, and check that it is one of the permitted options
def takeInput(inputOptions, inputPrompt):
  valEntered = ""
  while valEntered not in inputOptions:
  	 valEntered = input(inputPrompt)
  return valEntered

# set out blank playing board  
blankBoard = """
      A       B       C
          |       |
1         |       |    
          |       |
   -------|-------|-------
          |       |
2         |       |    
          |       |
   -------|-------|-------
          |       |
3         |       |    
          |       |
"""

# define space addresses that exist on the board
allSpaces = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

# define the locations where we can later put text on the board
spaceLocations = [51, 142, 233, 59, 150, 241, 67, 158, 249]

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

os.system('clear') # sends "clear" command to the shell, to clear previous text on screen

# make random choice of start-player if required
if toStart == "r":
	toStart = random.choice(["X","0"])
	print("Random choice: player \"{}\" starts.".format(toStart))
else:
	print("OK, player \"{}\" starts.".format(toStart))

print(blankBoard)

#================INITIALISE VARS===================

availableSpaces = allSpaces.copy() # weirdly, if you set list2 = list1, changes made to list2 are reflected in list1. Therefore use copy() to make list2 a separate list.

currentTurn = toStart

ownedByX = set() # create blank set to store locations owned by X
ownedBy0 = set() # create blank set to store locations owned by 0

workingBoard = blankBoard # initialise a version of the board to be filled in during game

timeToEnd = False # initialise a boolean used to end game when a player wins or all spaces taken

#==============MAIN GAMEPLAY LOOP==================

while not timeToEnd:

	requestSpacePrompt = "Player {}, please enter a coordinate: ".format(currentTurn)
	
	requestedSpace = takeInput(availableSpaces, requestSpacePrompt)
	
	availableSpaces.remove(requestedSpace)
	
	chosenSpaceIndex = allSpaces.index(requestedSpace)
	
	# you can't change a character within an existing string in Python. To get round, convert string to list, switch out the list item to represent the player move, then convert back to a string.
	workingBoardList = list(workingBoard)
	workingBoardList[spaceLocations[chosenSpaceIndex]] = currentTurn
	workingBoard = "".join(workingBoardList)
	
	os.system('clear')
	
	print('\n', workingBoard)
	
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
	
	# If all spaces are taken but no one has won, display draw message and end game
	if len(availableSpaces) == 0 and not timeToEnd:
		print("""
	********************
	********************
	*    It's a draw   *
	********************
	********************
				""")
		timeToEnd = True

#======================END===========================


