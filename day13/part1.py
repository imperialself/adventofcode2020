# Ingest bus schedule and departure timestamp. Find bus that leaves closest to
# your departure time, then find product of bus and minutes you have to wait
# https://adventofcode.com/2020/day/13

info = open('input').read().split('\n')


timestamp = int(info[0])
badbuses = info[1].replace('x,','').split(',')
buses = {}
for bus in badbuses:
	buses[bus] = {'id':0, 'departure':0 }

def findTime(bus):
	departure = int(bus)
	while departure < timestamp:
		departure += int(bus)
	buses[bus]['departure'] = int(departure-timestamp)
	buses[bus]['id'] = int(bus) * (departure-timestamp)

for bus in buses:
	findTime(bus)

print(buses)

# Manually find lowest departure value, then the corresponding ID
# lol