# Find number of "valid" passwords
# https://adventofcode.com/2020/day/2

import re

with open('input') as file:
    passwordlist = [line.rstrip('\n') for line in file]

# regexes
rLetter   = '[a-z]'
rMin      = '^[0-9]{1,}'
rMax      = '\-[0-9]{1,}'
rPassword = '\:\s[a-z]{1,100}'

valid = 0

for x in passwordlist:
	letter   = re.search(rLetter, x).group(0)
	min      = int(re.search(rMin, x).group(0))
	max      = int(re.search(rMax, x).group(0)[1:])
	password = re.search(rPassword, x).group(0)[2:]

	if min <= password.count(letter) <= max:
		valid += 1

print(valid)