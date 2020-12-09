# Determine the contiguous set of numbers that sum to 756008079, the val
# returned from the previous exercise, return sum of min() and max()
# https://adventofcode.com/2020/day/9

xmas = []
for i in open('input').read().split('\n'):
	xmas.append(int(i))

def checkSum(index,val):
	sum = 0
	while sum < val:						# Stop the following loop as soon as sum > val
		for i in range(index,len(xmas)):	# Loop through the set from index forward
			sum += xmas[i]					# Adding each following val to "sum" 
			if sum == val:					# And check each time to see if it == sum
				if i != index:				# Ensure a set larger than 1
					print(min(xmas[index:i])+max(xmas[index:i]))

# Loop through indexes
for i in range(len(xmas)):
	checkSum(i,756008079)