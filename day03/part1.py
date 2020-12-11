# how many times do you run into `#` when traversing through a
# horizontally repeating pattern at a given slope?
# https://adventofcode.com/2020/day/3

with open('input') as file:
    map = [line.rstrip('\n') for line in file]

# create 2d array
matrix = []
row = 0

for x in map:
	matrix.append([])
	for y in x:
		matrix[row].append(y)
	row += 1

# set these for later
x, y = 0, 0
collisions = 0
width = len(matrix[0])

while y < row:
	if matrix[y][x] == '#':
		collisions += 1
	x += 3      # slope is right 3, down 1
	y += 1
	if x > width-1:  # pattern repeats when you go off the edge
		x -= width   # width-1 because the largest index is len-1

print(f"Collisions: {collisions}")