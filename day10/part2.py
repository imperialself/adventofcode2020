# Find total number of valid combinations of adapters, noting that valid 
# means jumps can exist of 1, 2, 3 and can connect to your device at max+3
# https://adventofcode.com/2020/day/10

import functools

jRatings = []
for i in open('input').read().split('\n'):
	jRatings.append(int(i))

jRatings.append(0)					# There's always an outlet at 0
jRatings.append(max(jRatings)+3)	# Your device is always max + 3

@functools.lru_cache				# This makes the following algorithm blistering fast
def permute(num):
	if num == max(jRatings):		# If it reaches max, it's successful
		print("success")
		return 1
	count = 0
	for diff in (1,2,3):			# Basically we want to recurse for all valid jumps in the list
		if (num + diff) in jRatings:
			count += permute(num+diff)
	return(count)

print(permute(0))
