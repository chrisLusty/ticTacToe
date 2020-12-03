import random

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
#=====================================================

# ask who gets to have the first go, noughts or crosses
firstGoOptions = ["0","X","r"]

pickFirstGoPrompt = "Who goes first? (Enter {}, {} or {} for random): ".format("0","X","r")
  
toStart = takeInput(firstGoOptions, pickFirstGoPrompt)

# make random choice of start player if required
if toStart == "r":
  toStart = random.choice(["X","0"])
  print("Random choice: player \"{}\" starts.".format(toStart))

currentTurn = toStart

print(blankBoard)

availableSpaces = allSpaces.copy() # weirdly, if you set list 2 = list 1, changes made to list 2 are reflected in list 1. Therefore use copy() to make a separate list.

workingBoard = blankBoard

for turns in range(9):

	requestSpacePrompt = "Player {}, please enter a coordinate: ".format(currentTurn)
	
	requestedSpace = takeInput(availableSpaces, requestSpacePrompt)
	
	availableSpaces.remove(requestedSpace)
	
	#print(availableSpaces)
	#print(allSpaces)
	chosenSpaceIndex = allSpaces.index(requestedSpace)
	
	# you can't change a character within an existing string in Python. To get round, convert string to list, switch out the list item to represent the player move, then convert back to a string.
	workingBoardList = list(workingBoard)
	workingBoardList[spaceLocations[chosenSpaceIndex]] = currentTurn
	workingBoard = "".join(workingBoardList)
	
	print(workingBoard)
	
	if currentTurn == "X":
	  currentTurn = "0"
	else:
	  currentTurn = "X"

#print(currentTurn)



#====================================================3

#for m in range(len(output)):
 # print(m, output[m])
  
"""
A1 = 51
A2 = 59
A3 = 67
B1 = 142
B2 = 150
B3 = 158
C1 = 233
C2 = 241
C3 = 249
"""