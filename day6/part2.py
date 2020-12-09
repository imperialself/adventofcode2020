# Find the number of questions (letters) a group answered yes unanimously
# Return sum of all groups' unanimous letters
# https://adventofcode.com/2020/day/6

# Make each group of people into a list within the customs list
customs = []
for group in open('input').read().split('\n\n'):
	customs.append(group.splitlines())

# Start fresh
yesCounts = []

# Starts with whatever person 1 had, iterate through each person and remove every remaining letter not present
def countYeses(c):
	unanimous = list(c[0])				# Start with whatever person 1 said yes to
	for p in c:
		for l in c[0]:					# More performant than looping through 26 letters every time
			if l not in p:
				try:					# This is going to fail if it's already been removed so we only "try"
					unanimous.remove(l)
				except ValueError:
					pass
	yesCounts.append(len(unanimous))		# The length is a count of the remaining letters

# Iterate through all groups and count their yeses
for group in customs:
	countYeses(group)

print(sum(yesCounts))

