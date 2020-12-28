# input = [3,8,9,1,2,5,4,6,7]
input = [7,1,2,6,4,3,5,8,9]

def destination(cups,currCup):
	found = False
	while not found:
		for i in range(1, len(cups)):
			destCup = currCup-i
			if destCup in cups:
				destIndex = cups.index(destCup)
				found = True
				break
			elif destCup < min(cups):
				destCup = max(cups)
				destIndex = cups.index(destCup)
				found = True
				break
	return destCup

#make it so nextCup lives at the index +1
def arrange(cups,nextCup,currIndex):
	newOrder = [None] * len(cups)
	nextIndex = cups.index(nextCup)
	diff = currIndex - nextIndex
	for i in cups:
		oldIndex = cups.index(i)
		newOrder[(oldIndex+diff)%len(cups)] = i
	return newOrder


def turn(cups,currCup):
	print(cups)
	print(f"currcup: {currCup}")

	# 1. Pickup 3 cups following the current cup:
	# Note: these need to wrap around
	currIndex = cups.index(currCup)
	pickups = [cups.pop((currIndex+1)%len(cups)),cups.pop((currIndex+1)%len(cups)),cups.pop((currIndex+1)%len(cups))]
	print(f"pickups: {pickups}")
	print(f"cups after pickup: {cups}")

	# 2. select destination cup
	destCup = destination(cups,currCup)
	destIndex = cups.index(destCup)
	print(f"destination: {destCup} index: {destIndex}")
	
	# 3. Place cups right after the destination
	cups = cups[:destIndex+1] + pickups + cups[destIndex+1:]
	print(f"cups after placement: {cups}")
	print("------------------------------------------")

	# 4. pick new current cup
	nextCup = cups[(currIndex+1)%len(cups)]

	# 5. rearrange it so it the next cup is index + 1
	cups = arrange(cups,nextCup,currIndex)

	return cups,nextCup

def finalBit(cups):
	startingIndex = cups.index(1) + 1
	final = ''
	for i in range(len(cups)-1):
		final += str(cups[(startingIndex+i)%len(cups)])
	return final


def game(cups,starting,moves):
	nextCup = starting
	for i in range(moves):
		print(f"turn: {i+1}")
		cups,nextCup = turn(cups,nextCup)
	print(finalBit(cups))


game(input,7,100)


