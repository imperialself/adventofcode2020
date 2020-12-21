# Given a list of gibberish ingredients and their contained allergens,
# determine which ingredient is which allergen, return concat str of ingredients
# https://adventofcode.com/2020/day/21

# 'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)' becomes
# [{mxmxvkd, kfcds, sqjhc, nhms}, {dairy, fish}]
food = []
for line in open('input').read().split('\n'):
	ingr = set(line.split(' (')[0].split(' '))
	aller = set(line.split('(contains ')[1].strip(')').replace(',','').split(' '))
	food.append([ingr, aller])

# for each line, for each allergen, perform set intersection to narrow down
# the list of ingredients we can know for certain are allergens
# {allergen: set of potential ingredients responsible}
allergens = {}
for ingr,aller in food:
	for a in aller:
		if a not in allergens:
			allergens[a] = ingr
		else:
			allergens[a] = allergens[a] & ingr 	# Set intersection

# Stolen from day 16 part 2
matched = {}
while len(matched) != (len(allergens)):		# While we haven't matched all the allergens:
	for ingr,aller in allergens.items():
		if len(aller) == 1:	
			allergen = " ".join(aller)
			matched[ingr] = allergen
			for i in allergens:
				if allergen in allergens[i]:
					allergens[i].discard(allergen)

# Compile a sorted-by-allergen, comma-separated list of bad ingredients
cannonicallyBad = ''
for i in sorted (matched) : 
	cannonicallyBad += matched[i] + ','
cannonicallyBad = cannonicallyBad[:-1] # dont need the last comma

print(cannonicallyBad)