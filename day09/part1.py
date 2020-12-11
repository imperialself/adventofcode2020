# Determine which number in list cannot be summed by any two of the
# preceding 25 numbers in the list
# https://adventofcode.com/2020/day/9

xmas = []
for i in open('input').read().split('\n'):
	xmas.append(int(i))

def checkValid(index):
	val = xmas[index]
	if index > 24:
		preamble = xmas[index-25:index]		# slice the previous 25 numbers
		for x in preamble:					# same algorithm as day 1
			for y in preamble:
				if x + y == val:
					return True
		else:
			return False

# Loop through all in indexes and see which index can't be summed
for i in range(len(xmas)):
	if checkValid(i) == False:
		print(xmas[i])