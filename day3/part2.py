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

# initialize these for later
collisions = 0
collisionsArray = []

# functionizing this to count the collisions on a given slope
def collide(right,down):
	print(f"Slope: {right}, {down}")
	x, y = 0, 0
	collisions = 0
	while y < row:
		if matrix[y][x] == '#':
			collisions += 1
		x += right
		y += down
		if x > 30:   # pattern repeats when you go off the edge
			x -= 31  # 31 because index 30 means 31 objects
	print(f"Collisions: {collisions}")
	collisionsArray.append(collisions) # save the result for later

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
for n in collisionsArray:
	product = n * product

print(f"Final product: {product}")