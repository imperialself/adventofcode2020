
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

# Manually find lowest departure, then the corresponding ID

