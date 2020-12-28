# Only 1 part today

# Given public key inputs, determine number of handshake loops required
# on each the door and card. Then, find encryption key using public key
# and the prevously found number of loops

# https://adventofcode.com/2020/day/25

input = []
with open('input') as data:
	for line in data:
		input.append(int(line))

cardPublicKey = input[0]
doorPublicKey = input[1]
subjectNum = 7

def handshake(subnum,key):
	loops = 0
	value = 1
	while value != key:
		value *= subnum
		value = value % 20201227
		loops += 1
	return loops

def findEncryption(subnum,loops):
	value = 1
	for i in range(loops):
		value *= subnum
		value = value % 20201227
		loops += 1
	return value

# Get Card's loop size (number of loops to return cardPublicKey)
print("Finding card loops...")
cardLoops = handshake(subjectNum,cardPublicKey)

# Get Door's loop size (number of loops to return doorPublicKey)
print("Finding door loops...")
doorLoops = handshake(subjectNum,doorPublicKey)

# Make sure that the reverse-engineered encryption key results match
print("Finding encryption keys and comparing results")
encryption1 = findEncryption(doorPublicKey,cardLoops)
encryption2 = findEncryption(cardPublicKey,doorLoops)
if encryption1 == encryption2:
	print(f"Success! Encryption key is {encryption1}")

