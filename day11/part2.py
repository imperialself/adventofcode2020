# Ingest 2d array representing a seat chart, and apply rules to swap between
# empty or occupied, all at once, until the seat chart reaches a static state
# https://adventofcode.com/2020/day/11

import copy 

seatMap = []
for i in open('input').read().split('\n'):
	seatMap.append(list(i))

height = len(seatMap)
width = len(seatMap[0])

# Prints the map
def printMap(map):
	for row in map:
		print(''.join(row))

# Check seats in all cardinal directions, skipping the floor, return count of occupied seats
def checkAdjacentCount(row,seat,ogMap):
	# Set and visualize directions to look in
	direction = [[-1,-1], [-1,0], [-1,1], \
	            [0,-1],           [0,1], \
	            [1,-1],   [1,0],  [1,1]]				     
	occupiedCount = 0

	# Check all directions until we find a seat
	for i in direction:
		seatFound = False
		rowToCheck = row + i[0]		# Start moving in a direction
		seatToCheck = seat + i[1]
		# Run while inside map bounds or until seat found
		while (0 <= seatToCheck < width) and \
		      (0 <= rowToCheck < height) and \
		      (seatFound == False):		
			if ogMap[rowToCheck][seatToCheck] == "#":	# If occupied
				occupiedCount += 1
				seatFound = True
			elif ogMap[rowToCheck][seatToCheck] == "L":	# If unoccupied
				seatFound = True
			else:		# Else floor, so keep moving in current direction until seat is found
				rowToCheck += i[0]
				seatToCheck += i[1]
	return occupiedCount

# Run through seat map and make changes
def iterate(ogMap):
	newMap = copy.deepcopy(ogMap) # Need deepcopy here

	# Iterate through all rows, seats, and apply any changes to newMap
	for row in range(height):
		for seat in range(width):
			# If seat is empty and 0 adjacent are occupied
			if ogMap[row][seat] == "L" and checkAdjacentCount(row,seat,ogMap) == 0:
				newMap[row][seat] = "#"
			# If seat is occupied and 5 or more adjacent are occupied
			if ogMap[row][seat] == "#" and checkAdjacentCount(row,seat,ogMap) >= 5:
				newMap[row][seat] = "L"

	# Check if stabilized, count occupied seats, and iterate again with newMap if unstable
	ogCount = sum(x.count('#') for x in ogMap)
	newCount = sum(x.count('#') for x in newMap)
	printMap(ogMap)
	if newMap == ogMap:
		print(f"{ogCount} -> {newCount} occupied... Stabilized at {ogCount}!")
	else:
		print(f"{ogCount} -> {newCount} occupied... Unstable. Iterating!")
		iterate(newMap)

# Run program
iterate(seatMap)
