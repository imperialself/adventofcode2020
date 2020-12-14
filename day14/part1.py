initProgram = []
for i in open('input').read().split('\n'):
	if i.split(' = ')[0] == 'mask':
		initProgram.append([i.split(' = ')[0], i.split(' = ')[1]])
	if i.split('[')[0] == 'mem':
		val = int(i.split(' = ')[1])
		address = int(i.split('[')[1].split(']')[0])
		initProgram.append([address,val])

memDict = {}
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# mask applies to value
for step in initProgram:
	if step[0] == 'mask':
		mask = step[1]
	else:
		address = step[0]
		val = step[1]
		bVal = format(val, '#038b')[2:]
		for n in range(len(mask)):
			if mask[n] != 'X':
				bVal = bVal[:n] + mask[n] + bVal[n+1:]
		memDict[address] = bVal

sum = 0
for key in memDict:
	sum += int(memDict[key], 2)

print(sum)