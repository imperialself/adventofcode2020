# Ingest 2d array representing a seat chart, and apply rules to swap between
# empty or occupied, all at once, until the seat chart reaches a static state
# https://adventofcode.com/2020/day/11

import copy 

seatMap = []
for i in open('input').read().split('\n'):
	seatMap.append(list(i))

height = len(seatMap)
width = len(seatMap[0])

# Check seats in all cardinal directions, skipping the floor, return count of occupied seats
def checkAdjacentCount(row,seat,ogMap):
	# Set directions to look in, and init occupiedCount
	direction = [[-1,-1], [-1,0], [-1,1], \
				 [0,-1], 		  [0,1], \
				 [1,-1],  [1,0],  [1,1]]				     
	occupiedCount = 0
	for i in direction:
		seatFound = False
		rowToCheck = row + i[0]		# Add direction to row and seat vals
		seatToCheck = seat + i[1]
		while (0 <= seatToCheck < width) and \
			  (0 <= rowToCheck < height) and \
			  (seatFound == False):		# Run while inside bounds and/or until seatFound
			if ogMap[rowToCheck][seatToCheck] == "#":
				occupiedCount += 1
				seatFound = True
			elif ogMap[rowToCheck][seatToCheck] == "L":
				seatFound = True
			else:		# Else, keep moving in current direction til we find a seat
				rowToCheck = rowToCheck + i[0]
				seatToCheck = seatToCheck + i[1]
	return occupiedCount

def iterate(ogMap):
	newMap = copy.deepcopy(ogMap)
	# Iterate through all rows, seats, and make any changes to newMap
	for row in range(len(ogMap)):
		for seat in range(len(ogMap[row])):
			if ogMap[row][seat] == "L":
				if checkAdjacentCount(row,seat,ogMap) == 0:
					newMap[row][seat] = "#"
			if ogMap[row][seat] == "#":
				if checkAdjacentCount(row,seat,ogMap) >= 5:
					newMap[row][seat] = "L"
	# Check if we're reached parity, and iterate again if we haven't
	if newMap == ogMap:
		print("Success!")
		print(sum(x.count('#') for x in ogMap))
	else: 
		iterate(newMap)

iterate(seatMap)
