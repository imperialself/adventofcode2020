# Find the number of questions (letters) a group answered yes unanimously
# Return sum of all groups' unanimous

from string import ascii_lowercase

customsDump = open('input').read().strip().split('\n\n')

# Make each group of people into a list, add to the Cleaned list
customsCleaned = []
for group in customsDump:
	customsCleaned.append(group.splitlines())

# Start fresh
yesCounts = []

# Starts with full list of alphabet, iterate through each person and remove eve
def countYeses(c):
	yeses = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for p in c:
		for l in ascii_lowercase:		# Convenient string is convenient
			if l not in p:
				try:					# This is going to fail if it's already been removed so we only "try"
					yeses.remove(l)
				except ValueError:
					pass
	yesCounts.append(len(yeses))		# The length is a count of the remaining letters

# Iterate through all groups and count their yeses
for group in customsCleaned:
	countYeses(group)

print(sum(yesCounts))