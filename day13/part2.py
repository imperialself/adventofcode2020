# Find the first time value, where all buses will arrive in order at time + index (aka offset)
# https://adventofcode.com/2020/day/13

info = open('input').read().split('\n')

badbuses = info[1].split(',')
buses = []
for bus in badbuses:
	if bus != 'x':		# 'x' indexes aren't bound to a bus
		buses.append([int(bus), int(badbuses.index(bus))])	# [Bus, minutes after t]

time = buses[0][0]	# We can just start at the first bus
interval = 1
for bus,offset in buses:
	while (time + offset) % bus != 0:	# Keep adding interval to time until we find a time that works
		time += interval
	interval *= bus					# Makes sure all previous busses will still work at new times
	print(f"{time} works for {bus} and all previous busses")
print(f"Final answer: {time}")
