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

# 0=white, 1=black
def flip(location):
	if location in tiles:
		state = (tiles[location] + 1) % 2
		return state
	else:
		return 1

tiles = {}
for i in open('input').read().split('\n'):
	location = str(googleMaps(i))
	state = flip(location)
	tiles[location] = state

count = 0
for t,s in tiles.items():
	if s == 1:
		count += 1

print(count)