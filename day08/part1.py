# Run looping instructions and return accumulator sum right before
# it starts its second loop
# https://adventofcode.com/2020/day/8

instructions = []
for i in open('input').read().split('\n'):
	instructions.append([i.split(" ")[0], int(i.split(" ")[1])])

accumulator = 0
stepsRan = []

def runStep(index):
	global stepsRan, accumulator
	if index in stepsRan:
		print("Infinite loop")
		return
	stepsRan.append(index)

	if instructions[index][0] == "nop":
		runStep(index+1)
	if instructions[index][0] == "acc":
		accumulator += instructions[index][1]
		runStep(index+1)
	if instructions[index][0] == "jmp":
		runStep(index+instructions[index][1])

runStep(0)
print(accumulator)