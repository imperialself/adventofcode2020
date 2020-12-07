# Ingest list of rules for bags containing other bags
# Iterate through to see how many bags are nested in a given bag

# Make a dict where bag is key, and another dict containing children and their qty
rules = {}
for b in open('input').read().replace("bags","bag").split('\n'):
	bag = b.split(" contain ")[0]
	contains = b.split( "contain ")[1]
	contains = contains.strip(".").split(", ")		# make list of child bags
	rules[bag] = {}									# Init the dict to dump child bags into
	if contains[0] == 'no other bag':				# If no child bags, give it an empty dict
		rules[bag] = {}
	else:											# Else, rules[bag] = {'childbag1': qty, 'childbag2' = qty}
		for i in contains:
			rules[bag][i[2:]] = int(i[0])

# Count the total qty of bags nested in a given bag
def countBags(bag):
	sum = 0 
	if len(rules[bag]):					# Check if the bag has children
		for child in rules[bag]:
			# Add the qty of child bags, plus, the product of the grandchildren and the qty of that child, iteratively
			# Ex: if bag contains 2 bags containing 3 bags containing 4 bags containing 0 bags, sum = 2 + 2 * (3 + 3 * (4 + 4 * 0))
			sum += rules[bag][child] + (rules[bag][child] * countBags(child))
		return sum
	else:								# Else, no new children so return 0
		return 0

print(countBags("shiny gold bag"))
