instructions = []
for i in open('input').read().split('\n'):
	instructions.append([i.split(" ")[0], int(i.split(" ")[1])])

def runStep(index):
	global stepsRan, accumulator
	# print(accumulator)
	if index in stepsRan:
		return False
	elif index > len(instructions)-1:
		print(f"Successfully terminated. Accumulator: {accumulator}")
		return True
	else:
		stepsRan.append(index)
		if instructions[index][0] == "nop":
			runStep(index+1)
		if instructions[index][0] == "acc":
			accumulator += instructions[index][1]
			runStep(index+1)
		if instructions[index][0] == "jmp":
			runStep(index+instructions[index][1])

for index in range(len(instructions)):
	if "nop" in instructions[index]:
		instructions[index][0] = "jmp"
		stepsRan = []
		accumulator = 0
		runStep(0)
		instructions[index][0] = "nop"		# Change back
	if "jmp" in instructions[index]:
		instructions[index][0] = "nop"
		stepsRan = []
		accumulator = 0
		runStep(0)
		instructions[index][0] = "jmp"		# Change back