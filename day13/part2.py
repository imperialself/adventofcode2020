from functools import reduce
import math

info = open('input').read().split('\n')

badbuses = info[1].split(',')
buses = []
offsets = []
for bus in badbuses:
	if bus != 'x':
		buses.append([int(bus), int(badbuses.index(bus))])	# [Bus, minutes after t]
		offsets.append(badbuses.index(bus))

print(buses)

time = 0
interval = 1
for bus in buses:
	print(f"syncing bus {bus[0]}")
	synced = False
	while not synced:
		time += interval
		if (time + bus[1]) % bus[0] == 0:
			interval = interval * bus[0]
			print(f"synced {bus[0]} (offset {bus[1]}) at {time}")
			synced = True