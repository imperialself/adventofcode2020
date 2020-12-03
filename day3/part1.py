# how many times do you run into `#` when traversing through a
# horizontally repeating pattern at a given slope?

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

while y < row:
	if matrix[y][x] == '#':
		collisions += 1
	x += 3      # slope is right 3, down 1
	y += 1
	if x > 30:  # pattern repeats when you go off the edge
		x -= 31 # subtract 31 because index 30 means 31 objects

print(f"Collisions: {collisions}")