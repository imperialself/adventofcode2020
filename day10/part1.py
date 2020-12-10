# Adapters can jump 1, 2, or 3. Find how many of each jump are present
# and return the product of the 1 and 3 jump counts
# https://adventofcode.com/2020/day/10

jRatings = []
for i in open('input').read().split('\n'):
	jRatings.append(int(i))

# Wall outlet is always 0, and your device is max+3
jRatings.append(0)
jRatings.append(max(jRatings)+3)
jRatings.sort()

# Set each jump number to 0
jumps = {1:0, 2:0, 3:0}

for i in range(len(jRatings)-1):
	diff = jRatings[i+1] - jRatings[i]
	jumps[diff] += 1

print(jumps)
print(jumps[1] * jumps[3])