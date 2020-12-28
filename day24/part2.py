import copy

def googleMaps(path):
	move = {'se':[1,-1], 'sw':[-1,-1], 'nw':[-1,1], 'ne':[1,1], 'e': [2,0], 'w':[-2,0]}
	coord = [0,0]
	#traverse through path
	char = 0
	while char < len(path):
		if path[char] in move:
			coord[0] += move[path[char]][0]
			coord[1] += move[path[char]][1]
			char += 1 
		elif path[char:char+2] in move:
			coord[0] += move[path[char:char+2]][0]
			coord[1] += move[path[char:char+2]][1]
			char += 2
	return coord

# Reuse day17
# Returns set of neighboring coordinates
def getNeighbors(x,y):
	neighbors = set()
	adjacentTiles = [[2,0],[1,-1],[-1,-1],[-2,0],[-1,1],[1,1]]
	for i in adjacentTiles:
		neighbors.add((x+i[0], y+i[1]))
	return neighbors 

# Returns the count of all black neighbors
def checkNeighbors(x,y,blackTiles):
	neighbors = getNeighbors(x,y)
	blackNeighborCount = 0
	for neighbor in neighbors:
		if neighbor in blackTiles:
			# print(neighbor)
			blackNeighborCount += 1
	return blackNeighborCount


# Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
# Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.

# Take one iteration
def iterate(blackTiles):
	# Make list of all coordinates that we need to check, start with blackTiles and add all neighbors
	potentialTiles = copy.deepcopy(blackTiles)
	for tile in blackTiles:
		potentialTiles = potentialTiles | getNeighbors(tile[0], tile[1])
	# print(f"potentials: {potentialTiles}")

	# Check all that we need to check, and add to the next blackTiles set if they meet condition
	newblackTiles = set()
	for tile in potentialTiles:
		x,y = tile[0], tile[1]
		blackNeighborCount = checkNeighbors(x, y, blackTiles)
		if tile in blackTiles:	# If black tile, it only stays if 1 or 2 black neighbors
			if blackNeighborCount == 1 or blackNeighborCount == 2:
				newblackTiles.add(tile)
		else:	# white tiles are in potentialTiles and not blackTiles, flips black if 2 neighbors are black
			if blackNeighborCount == 2:
				newblackTiles.add(tile)
	return newblackTiles

# Main

blackTiles = set()
for i in open('input').read().split('\n'):
	location = googleMaps(i)
	if (location[0], location[1]) not in blackTiles:
		blackTiles.add((location[0], location[1]))
	else:
		blackTiles.remove((location[0], location[1]))

# Run n iterations and return the number of black Tiles at the end of each one
print(f"Initial Day: {len(blackTiles)}")
print("-----------------")
iterations = 100
for i in range(1, iterations+1):
	blackTiles = iterate(blackTiles)
	print(f"Iteration {i}: {len(blackTiles)}")
	print("-----------------")