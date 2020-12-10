# Adapters can jump 1, 2, or 3. Find how many of each jump are present
# and return the product of the 1 and 3 jump counts
# https://adventofcode.com/2020/day/10

jRatings = []
for i in open('input').read().split('\n'):
	jRatings.append(int(i))

jRatings.append(0)						# The wall outlet always 0
jRatings.append(max(jRatings)+3)		# Your device is max+3
jRatings.sort()

# Set each jump number to 0
jumps = {'1':0, '2':0, '3':0}

for i in range(len(jRatings)-1):
	if jRatings[i] == jRatings[i+1] - 1:		# Jump of 1
		jumps['1'] += 1
	elif jRatings[i] == jRatings[i+1] - 2:		# Jump of 2
		jumps['2'] += 1
	elif jRatings[i] == jRatings[i+1] - 3:		# Jump of 3
		jumps['3'] += 1

print(jumps)
print(jumps['1'] * jumps['3'])