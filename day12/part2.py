# https://adventofcode.com/2020/day/12

instructions = []
for i in open('input').read().split('\n'):
	instructions.append([i[0],int(i[1:])])

move = {'N': [1,0], 'E':[0,1], 'S':[-1,0], 'W':[0,-1]}		# Modifiers one would make to x,y to move a direction
compass = ['N', 'E', 'S', 'W']
rotate = {'R':1, 'L':-1}
shipX,shipY = 0, 0		# starts at 0,0
wayX,wayY = 10,1		# starts at 10 east, 1 north

def rotateRight(x,y):
	global wayX,wayY
	wayY = -x 
	wayX = y

def rotateLeft(x,y):
	global wayX,wayY
	wayX = -y
	wayY = x

def runStep(step):
	global wayX,wayY,shipX,shipY,errors
	command = step[0]
	if command in compass:		# Moves Waypoint a direction a given number of spaces
		wayX += (move[command][1] * step[1])
		wayY += (move[command][0] * step[1])
	elif command == "R":		# Rotates the waypoint AROUND the ship
		turns = step[1] // 90	# Converts degrees to number of quarter turns
		while turns > 0:
			rotateRight(wayX,wayY)
			turns -= 1
	elif command == "L":		# Rotates the waypoint AROUND the ship
		turns = step[1] // 90
		while turns > 0:
			rotateLeft(wayX,wayY)
			turns -= 1
	elif command == 'F':		# moves ship through the waypoint n times
		shipX += wayX * step[1]
		shipY += wayY * step[1]

for step in instructions:
	runStep(step)

print(f"Total distance: {abs(shipX) + abs(shipY)}")
