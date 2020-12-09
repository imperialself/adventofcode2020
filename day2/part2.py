# Find number of "valid" passwords
# https://adventofcode.com/2020/day/2

import re

with open('input') as file:
    passwordlist = [line.rstrip('\n') for line in file]

# regexes
rLetter   = '[a-z]'
rPos1     = '^[0-9]{1,}'
rPos2     = '\-[0-9]{1,}'
rPassword = '\:\s[a-z]{1,100}'

valid = 0

for x in passwordlist:
	letter   = re.search(rLetter, x).group(0)
	pos1     = int(re.search(rPos1, x).group(0)) - 1
	pos2     = int(re.search(rPos2, x).group(0)[1:]) - 1
	password = re.search(rPassword, x).group(0)[2:]

	if (password[pos1] == letter and password[pos2] != letter) or (password[pos1] != letter and password[pos2] == letter):
			valid += 1

print(valid)