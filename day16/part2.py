import copy

input = open('input').read().split('\n\n')
r = input[0].split('\n')
t = input[1].split('\n')
n = input[2].split('\n')[1:]

# Clean up rules
rules = {}
for l in r:
	name = l.split(": ")[0]
	val = l.split(": ")[1]
	val = [int(x) for x in val.replace(" or ","-").split("-")]
	rules[name] = val	# {'row': [49, 634, 650, 957]} where valid is between [0:1] and between [2:3]

# Clean up my ticket
myTicket = [int(x) for x in t[1].split(",")]

# Make clean list of nearby tickets
nearby = []
for l in n:
	l = [int(x) for x in l.split(",")]
	nearby.append(l)

# Returns True if all numbers are valid, False if a single number is invalid
def checkValidNumber(num):
	valid = False
	for k,v in rules.items():
		if (v[0] <= num <= v[1]) or (v[2] <= num <= v[3]):
			valid = True
	return valid

# This checks if a ticket is valid and returns True if it is
def checkIfValid(ticket):
	valid = True
	for n in ticket:
		if not checkValidNumber(n):
			valid = False
	return valid

# This iterates through all the tickets and makes a new list of valid tickets
def checkTickets(nearby):
	valid = []
	for ticket in nearby:
		if checkIfValid(ticket):
			valid.append(ticket)
	return valid

# This matches a val to the fields it is valid for
def returnPossible(num):
	possible = []
	for k,v in rules.items():
		if (v[0] <= num <= v[1]) or (v[2] <= num <= v[3]):
			possible.append(k)
	return possible

# Look through each index, iterate through every ticket, 
# starting with full field list, use process of elimination
def findPossible(index):
	global fieldPossibilities
	possibleFields = copy.deepcopy(masterList)
	for ticket in validTickets:
		possible = returnPossible(ticket[index])
		for f in masterList:
			if f not in possible:
				possibleFields.discard(f)
	fieldPossibilities[index] = possibleFields


# Stage 1: discard invalid tickets
validTickets = checkTickets(nearby)
validTickets.append(myTicket)	# my ticket is valid, afterall

# Stage 2: start with a full field list narrow down the possible fields per index
masterList = set()
for f in rules:
	masterList.add(f)

fieldPossibilities = {}
for index in range(len(myTicket)):
	findPossible(index)

# Stage 3: since many indexes have multiple possible fields, find out the definitive arrangment 
matched = {}
while len(matched) != (len(myTicket)):					# While we haven't matched all the fields:
	for k in fieldPossibilities:
		if len(fieldPossibilities[k]) == 1:				# If an index only has one possible...
			field = " ".join(fieldPossibilities[k])
			matched[k] = field							# add it to the matched dict...
			for i in fieldPossibilities:
				if field in fieldPossibilities[i]:
					fieldPossibilities[i].discard(field)	# and discard it from the possibl 

# Stage 4: find product of my ticket's "departure" fields
product = 1
for k,v in matched.items():
	if "departure" in v:
		product *= myTicket[k]
print(product)


