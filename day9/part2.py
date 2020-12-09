xmas = []
for i in open('input').read().split('\n'):
	xmas.append(int(i))

def checkSum(index,val):
	sum = 0
	while sum < val:
		for i in range(index,len(xmas)):
			sum += xmas[i]
			if sum == val:
				if i != index:
					print(min(xmas[index:i])+max(xmas[index:i]))
					return True				
	return False
				
for i in range(len(xmas)):
	checkSum(i,756008079)