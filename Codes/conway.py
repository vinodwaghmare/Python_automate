

import random, time, copy

WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells
nextCells = []

for x in range(WIDTH):
    columns = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            columns.append("#")
        else:
            columns.append(" ")
    nextCells.append(columns)

 
 # Separate each step with newlines.
currentCells = copy.deepcopy(nextCells)

# Calculate the next step's cells based on current step's cells:

for x in range(WIDTH):
    for y in range(HEIGHT):
    # Get neighboring coordinates
    leftCoord = 
    rgthCoord