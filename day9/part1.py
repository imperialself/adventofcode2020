xmas = []
for i in open('input').read().split('\n'):
	xmas.append(int(i))

def checkValid(index):
	val = xmas[index]
	if index > 24:
		preamble = xmas[index-25:index]
		for x in preamble:
			for y in preamble:
				if x + y == val:
					return True
		else:
			return False

for i in range(len(xmas)):
	if checkValid(i) == False:
		print(xmas[i])