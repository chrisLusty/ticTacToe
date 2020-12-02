toStart = input("Who goes first? (Enter 0, X, or r for random): ")

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
C         |   X   |   0
          |       |
"""

print(output)