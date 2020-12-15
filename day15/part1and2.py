# Find the nth number in series following rules
# https://adventofcode.com/2020/day/15 

# part 1: 2020
# part 2: 30000000
target = 2020 # nth iteration we want to know

# Initialize
said = {}
starting = [2,0,1,7,4,14,18]	# The input given by AoC

def takeTurn(turn):
	global said,lastTurn

	# If still in the starting numbers
	if turn < len(starting)+1:
		said[starting[turn-1]] = [turn]
		lastTurn = starting[-1]
		return

	# ok, rules of the game:
	if len(said[lastTurn]) > 1:		# If last turn's num has been said 2+ times, find diff in previous two times said
		thisTurn = said[lastTurn][-1] - said[lastTurn][-2]
	elif len(said[lastTurn]) == 1:	# If last turn num was the first time it was said, say 0
		thisTurn = 0

	# add to list 
	if thisTurn not in said:	# If first time said, need to initialize the key's array
		said[thisTurn] = [turn]	
	else:
		said[thisTurn].append(turn)
	lastTurn = thisTurn		# Lets me keep iterating

# take n=target turns defined at top:
for turn in range(target+1):
	takeTurn(turn)
	if turn % (target//10) == 0:
		print(f"Progress: {turn*100//target}%")

print(lastTurn)