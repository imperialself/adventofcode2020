# Flip elements in 4d grid on or off according to their neighbors
# https://adventofcode.com/2020/day/17

import copy

starting = open('input').read().split('\n')

activeCubes = set()
for y,row in enumerate(starting):
	for x, val in enumerate(list(row)):
		if val == '#':
			activeCubes.add((x, y, 0, 0))

# Returns set of neighboring coordinates
def getNeighbors(x,y,z,w):
	neighbors = set()
	xs = [x-1,x,x+1]
	ys = [y-1,y,y+1]
	zs = [z-1,z,z+1]
	ws = [w-1,w,w+1]
	for i in xs:
		for j in ys:
			for k in zs:
				for l in ws:
					neighbors.add((i, j, k, l))
	neighbors.remove((x,y,z,w))
	return neighbors 

# Returns the sum of all active neighbors
def checkNeighbors(x,y,z,w):
	neighbors = getNeighbors(x,y,z,w)
	activeNeighborCount = 0
	for neighbor in neighbors:
		if neighbor in activeCubes:
			activeNeighborCount += 1
	return activeNeighborCount

# Take one iteration
def iterate(activeCubes):
	newActiveCubes = set()

	# Make list of all coordinates that we need to check, activeCubes + all neighbors
	potentialCubes = copy.deepcopy(activeCubes)
	for cube in activeCubes:
		potentialCubes = potentialCubes | getNeighbors(cube[0], cube[1], cube[2], cube[3])

	# Check all that we need to check, and add to the next activeCubes set if they meet condition
	for cube in potentialCubes:
		activeNeighborCount = checkNeighbors(cube[0],cube[1],cube[2],cube[3])
		if cube in activeCubes:
			if activeNeighborCount == 2 or activeNeighborCount == 3:
				newActiveCubes.add(cube)
		else:
			if activeNeighborCount == 3:
				newActiveCubes.add(cube)
	return newActiveCubes

# Run n iterations and return the number of active cubes at the end of each one
iterations = 6
for i in range(iterations):
	activeCubes = iterate(activeCubes)
	print(f"Iteration {i+1}: {len(activeCubes)}")