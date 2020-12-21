# Given a list of gibberish ingredients and their contained allergens,
# determine how many times safe ingredients occur
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
			allergens[a] = allergens[a] & ingr	# Set intersection

# Make single set of all potential allergens
generalAllergens = set()
for k,v in allergens.items():
	for i in v:
		generalAllergens.add(i)

# Count the number of instances of ingredients that 
# are not in our general allergen set
count = 0
for ingr,aller in food:
	for i in ingr:
		# print(i)
		if i not in generalAllergens:
			# print(i)
			count += 1

print(count)