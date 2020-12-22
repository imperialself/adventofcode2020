# Deck game like "war" where flip over top card and highest card
# gets both cards added to the bottom of their deck.
# https://adventofcode.com/2020/day/22

p1hand,p2hand = open('input').read().split('\n\n')

p1hand = [int(x) for x in p1hand.split('\n')[1:]]
p2hand = [int(x) for x in p2hand.split('\n')[1:]]

def round():
	global p1hand,p2hand
	p1 = p1hand.pop(0)
	p2 = p2hand.pop(0)
	if p1 > p2:
		p1hand.extend((p1,p2))
	elif p2 > p1:
		p2hand.extend((p2,p1))
 
def score(hand):
	sum = 0
	for i in range(1,len(hand)+1):
		sum += hand[-i] * i
	return sum

def playGame():
	while p1hand and p2hand:
		round()
	winner = p1hand + p2hand
	print(score(winner))

playGame()