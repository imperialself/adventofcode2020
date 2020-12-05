# Implement Binary Space Partitioning decoding algorithm to find each Seat ID
# then sort and find the missing ID in the list
import math

boardingPasses = open('input').read().strip().split('\n')

# First 7 characters, range 0-127 where F means keep lower hald and B means upper
def getRow(p):
	p = p[:7]
	range = [0, 127]
	for c in p:
		if c == "F": # Lower
			range[1] = range[1] - math.ceil((range[1] - range[0]) / 2)
		if c == "B": # Upper
			range[0] = range[0] + math.ceil((range[1] - range[0]) / 2)
	row = range[0]
	return row

# Last three characters, range 0-7 where L means keep lower half and R means upper
def getSeat(p):
	p = p[7:]
	range = [0,7]
	for c in p:
		if c == "L": # Lower
			range[1] = range[1] - math.ceil((range[1] - range[0]) / 2) 
		if c == "R": # Upper
			range[0] = range[0] + math.ceil((range[1] - range[0]) / 2)
	seat = range[0]
	return seat

# Every seat also has a unique seat ID: multiply the row by 8, then add the column
def getID(p):
	global ids
	row = getRow(p)
	seat = getSeat(p)
	id = row * 8 + seat
	ids.append(id)

# Create, populate, and sort the IDs array 
ids = []
for p in boardingPasses:
	getID(p)

ids.sort()

# Find missing boarding pass ID
for i in range(len(ids)-1):
	if ids[i] + 1 != ids[i+1]:
		print(f"Missing ID is: {ids[i]+1}")