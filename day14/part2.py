initProgram = []
for i in open('input').read().split('\n'):
	if i.split(' = ')[0] == 'mask':
		initProgram.append([i.split(' = ')[0], i.split(' = ')[1]])
	if i.split('[')[0] == 'mem':
		val = int(i.split(' = ')[1])
		address = int(i.split('[')[1].split(']')[0])
		initProgram.append([address,val])

def joinAddress(address):
	return int(''.join(map(str, address)),2)

def joinMask(mask):
	return ','.join(map(str, mask)).replace(',','')

# Mask applies to address. 
# X means 0 AND 1, so multiple addresses potentially
# 0 means unchanged
# 1 means overwrite with 1
def getAddresses(address,mask):
	global addresses
	binAd = format(address, '#038b')[2:]	# get address in binary, 36 bits long
	binAd = list(binAd)
	mask = list(mask)
	for n in range(len(mask)):
		if mask[n] == '1':
			binAd[n] = 1	# flip bit
			mask[n] = 0		# dont flag bit in future recursions
		if mask[n] == 'X':
			mask[n] = 0		# dont flag bit in future recursions
			binAd[n] = 0	# need to run iterations as if it were both 0 and 1
			getAddresses(joinAddress(binAd) , joinMask(mask))
			binAd[n] = 1
			getAddresses(joinAddress(binAd), joinMask(mask))
	addresses.add(joinAddress(binAd))
	return addresses

def getSum(memDict):
	sum = 0
	for key in memDict:
		sum += memDict[key]
	return sum

def runProgram(initProgram):
	global addresses
	addresses = set()
	memDict = {}	# init
	mask = ''
	inc = 1
	inc2 = 1
	for step in initProgram:
		if step[0] == 'mask':
			mask = step[1]
		else:
			addresses = getAddresses(step[0],mask)	# gonna be more than one address due to bitmask
			for i in addresses:
				memDict[i] = step[1]
			addresses.clear()
		# fancy animation so you know its working but only every 10 steps
		if inc % 10 == 0:
			print('working on it' + '.'*(inc2))
			inc2 += 1
		inc += 1
	print(getSum(memDict))

runProgram(initProgram)
