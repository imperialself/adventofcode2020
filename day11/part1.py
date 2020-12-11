# Ingest 2d array representing a seat chart, and apply rules to swap between
# empty or occupied, all at once, until the seat chart reaches a static state
# https://adventofcode.com/2020/day/11

import copy 

seatMap = []
for i in open('input').read().split('\n'):
	seatMap.append(list(i))

# Check adjacent seats in cardinal and diagonal directions, return count of 
def checkAdjacentCount(row,seat,ogMap):
	adjacentSeats = [[row-1,seat-1],  [row-1,seat], [row-1,seat+1], \
				     [row,seat-1], 					[row,seat+1], \
				     [row+1,seat-1],  [row+1,seat],    [row+1,seat+1]]
	occupiedCount = 0
	for i in adjacentSeats:
		if (0 <= i[0] <= len(ogMap)-1) and (0 <= i[1] <= len(ogMap[0])-1): 	# Make sure not out of bounds
			if ogMap[i[0]][i[1]] == "#":
				occupiedCount += 1
	return occupiedCount

def iterate(ogMap):
	newMap = copy.deepcopy(ogMap)
	# Iterate through all rows, seats, and follow the rules to flip seats as necessary
	for row in range(len(ogMap)):
		for seat in range(len(ogMap[row])):
			if ogMap[row][seat] == "L":
				if checkAdjacentCount(row,seat,ogMap) == 0:
					newMap[row][seat] = "#"
			if ogMap[row][seat] == "#":
				if checkAdjacentCount(row,seat,ogMap) >= 4:
					newMap[row][seat] = "L"
	# Check if we're reached parity, and iterate again if we haven't
	if newMap == ogMap:
		print("Success!")
		print(sum(x.count('#') for x in ogMap))
	else: 
		iterate(newMap)

iterate(seatMap)
