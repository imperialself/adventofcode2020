# Find the number of questions (letters) that anybody in the group said yes to
# Find sum of all groups' yes sums

from string import ascii_lowercase

customsDump = open('input').read().strip().split('\n\n')

yesCounts = []

def countYeses(c):
	global yesCounts
	yes = 0
	for l in ascii_lowercase:
		if l in c:
			yes += 1
	yesCounts.append(yes)

for group in customsDump:
	countYeses(group)

print(sum(yesCounts))