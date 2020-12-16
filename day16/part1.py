# Ingest list of rules, return sum of numbers that aren't valid for any rule
# https://adventofcode.com/2020/day/16

input = open('input').read().split('\n\n')
r = input[0].split('\n')
t = input[1].split('\n')
n = input[2].split('\n')[1:]

# Clean up rules
rules = {}
for l in r:
	name = l.split(": ")[0]
	val = l.split(": ")[1]
	val = val.replace(" or ","-").split("-")
	val = [int(x) for x in val]
	rules[name] = val

# Clean up my ticket
myTicket = t[1]	

# Clean up nearby ticket list
nearby = []
for l in n:
	l = [int(x) for x in l.split(",")]
	nearby.append(l)

# If a number doesn't match any rule, this will return False
def checkValidNumber(num):
	valid = False
	for k,v in rules.items():
		if (v[0] <= num <= v[1]) or (v[2] <= num <= v[3]):
			valid = True
	return valid

# Check each number on a given ticket, add the invalid ones to a list
def checkTicket(ticket):
	global invalidNums
	valid = True
	for n in ticket:
		if not checkValidNumber(n):
			invalidNums.append(n)

# Iterate over all nearby tickets
invalidNums = []
for ticket in nearby:
	checkTicket(ticket)

print(sum(invalidNums))