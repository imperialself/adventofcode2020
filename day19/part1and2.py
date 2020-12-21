# Ingest a list of nested rules about letter orders, see which messages 
# are valid according to those rules
# https://adventofcode.com/2020/day/19

import re
from collections import defaultdict

r = open('input').read().split('\n\n')[0].split('\n')
messages = open('input').read().split('\n\n')[1].split('\n')

rules = {}

# 122: 86 1 | 99 20 becomes: {122: [['86', '1', '|', '99', '20']]}
for rule in r:
	number = int(rule.split(':')[0])
	sub = rule.split(': ')[1]
	if '\"' in sub:
		subrules = sub.strip('\"')

	else:
		subrules = sub.split(' ')
		for s in range(len(subrules)):
			if subrules[s] != "|":
				subrules[s] = int(subrules[s])
	rules[number] =  subrules

# Does what it says on the tin
def genRegex(rule,depth):
	if depth > 30:	# Necessary as part 2's rules loop.
		return "" 
	elif "a" in rule:
		return "a"
	elif "b" in rule:
		return "b"
	elif "|" in rule:
		# branch left and right on the |
		split = rule.index('|')
		left = rule[:split]
		right = rule[split+1:]
		# recurse deeper
		return "(?:" + genRegex(left,depth+1) + "|" + genRegex(right,depth+1) + ")"
	else:
		# recurse deeper
		regex = ''
		for r in rule:
			regex += genRegex(rules[r],depth+1)
		return regex

# Compile the suuuuuuper long regex and name him Reggie
Reggie = re.compile(genRegex(rules[0],0))

# Count number of messages matche
matches = 0
for m in messages:
	if re.fullmatch(Reggie, m):
		matches += 1
print(matches)