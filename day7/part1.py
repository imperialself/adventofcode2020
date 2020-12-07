# Ingest list of rules for bags containing other bags
# Then find out how many bags indirectly contain a given bag

# Make a dict where bag is key, and list the bags that key contains as the value
rules = {}
for b in open('input').read().split('\n'):
	bag = b.split(" contain ")[0][:-1]
	contains = b.split( "contain " )[1]
	contains = contains.strip(".").split(", ")
	if contains == ['no other bags']:
		contains = []
	for i in range(len(contains)):
		contains[i] = contains[i][2:]			# Strip number of each bags it can hold
		if contains[i][-1] == "s":				# De-pluralize for consistency
			contains[i] = contains[i][:-1]
	rules[bag] = contains

def findShinyGoldBag(bag):
	for b in rules[bag]:
		if 'shiny gold bag' in b or findShinyGoldBag(b):
			return True

winners = []
for bag,children in rules.items():
	if (findShinyGoldBag(bag) == True) and (bag not in winners):
		winners.append(bag)

print(len(winners))