# Deck game like "war" but recursive
# https://adventofcode.com/2020/day/22

p1,p2 = open('input').read().split('\n\n')

p1 = [int(x) for x in p1.split('\n')[1:]]
p2 = [int(x) for x in p2.split('\n')[1:]]


def score(hand):
	sum = 0
	for i in range(1,len(hand)+1):
		sum += hand[-i] * i
	return sum

def checkWinner(p1,p2):
	if len(p1) > len(p2):
		return 1
	else:
		return 2

def game(p1,p2):
	states = set()

	while p1 and p2:
		# 1. check if we've seen this state before
		state = (str(p1) + str(p2))
		if state in states:
			return 1
		states.add(state)

		# 2. draw cards
		c1 = p1.pop(0)
		c2 = p2.pop(0)

		# 3. recurse if both players have same or more cards as the number they drew
		if len(p1) >= c1 and len(p2) >= c2:
			# New subgame with amount of cards as the number they drew
			winner = game(p1[:c1],p2[:c2])	
		# else, normal round 
		elif c1 > c2:
			winner = 1 
		elif c2 > c1:
			winner = 2

		# 4. add cards to winner:
		if winner == 1:
			p1.extend((c1,c2))
		else:
			p2.extend((c2,c1))

	# return winner of game	
	return checkWinner(p1,p2)


gameWinner = game(p1,p2),

if gameWinner == 1:
	print(score(p1))
else:
	print(score(p2))

