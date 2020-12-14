# Move ship according to instructions, return the "manhattan distance" you travel
# # https://adventofcode.com/2020/day/12

instructions = []
for i in open('input').read().split('\n'):
	instructions.append([i[0],int(i[1:])])

move = {'N': [1,0], 'E':[0,1], 'S':[-1,0], 'W':[0,-1]}		# Modifiers one would make to x,y to move a direction
compass = ['N', 'E', 'S', 'W']
rotate = {'R':1, 'L':-1}
heading = 1		# Use as an index for compass 
x, y = 0, 0

def runStep(step):
	global x,y,heading
	command = step[0]
	if command in compass:					# Move ship a direction times intensity
		x += (move[command][1] * step[1])
		y += (move[command][0] * step[1])
	elif command == 'F':					# Move toward heading times intensity
		x += (move[compass[heading]][1] * step[1])
		y += (move[compass[heading]][0] * step[1])
	elif command in rotate:					# Rotate ship. Divide degrees into quarter turns and do that many
		turns = step[1] / 90
		while turns > 0:
			heading += rotate[command]
			heading = heading % 4			# modulo 4 to keep value between 0-3 
			turns -= 1

for step in instructions:
	runStep(step)

print(f"Total distance: {abs(x) + abs(y)}")
