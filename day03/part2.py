# how many times do you run into `#` when traversing through a
# horizontally repeating pattern at a given slope?
# https://adventofcode.com/2020/day/3

with open('input') as file:
    map = [line.rstrip('\n') for line in file]

# create 2d array
matrix = []
rows = 0

for x in map:
	matrix.append([])
	for y in x:
		matrix[rows].append(y)
	rows += 1

# initialize these for later
collisions = 0
results = []

# set width since we have to know when to repeat
width = len(matrix[0])

# functionizing this to count the collisions on a given slope
def collide(right,down):
	print(f"Slope: {right}, {down}")
	x, y = 0, 0
	collisions = 0
	while y < rows:
		if matrix[y][x] == '#':
			collisions += 1
		x += right
		y += down
		if x > width-1:  # pattern repeats when you go off the edge
			x -= width   # width-1 because the largest index is len-1
	print(f"Collisions: {collisions}")
	results.append(collisions) # save the result for later

# Do multiple slopes this time
# Right 1, down 1.
# Right 3, down 1.
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
slopesArray = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for slope in slopesArray:
	collide(slope[0],slope[1])

# find product of the collisions
product = 1
for n in results:
	product = n * product

print(f"Final product: {product}")