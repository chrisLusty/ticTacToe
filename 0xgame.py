import random

# function to take a user input, and check that it is one of the permitted options
def takeInput(inputOptions, inputPrompt):
  valEntered = ""
  while valEntered not in inputOptions:
  	 valEntered = input(inputPrompt)
  return valEntered

# ask who gets to have the first go, noughts or crosses
firstGoOptions = ["0","X","r"]

pickFirstGoPrompt = "Who goes first? (Enter {}, {} or {} for random): ".format("0","X","r")
  
toStart = takeInput(firstGoOptions, pickFirstGoPrompt)

# make random choice of start player if required
if toStart == "r":
  toStart = random.choice(["X","0"])
  print("Random choice: player \"{}\" starts.".format(toStart))

currentTurn = toStart

requestedSpace = input("Player {}, please enter a coordinate: ".format(currentTurn))

if currentTurn == "X":
  currentTurn = "0"
else:
  currentTurn = "X"

print(currentTurn)

output = """
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

print(output)

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