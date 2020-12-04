# process passport batch file and check and validate required fields

import re

passportDump = open('input').read().strip().split('\n\n')

passports = []
valid = 0

# Parse dump into a list of dicts
index = 0
for p in passportDump:
	passports.append({})
	pp = re.findall(r"\w{3}\:#?\S*", p)
	for i in pp:
		field = i.split(":")
		passports[index][field[0]] = field[1]
	index += 1

# print(passports)

def checkPassport(p):
	global valid
	need = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	
	if all (k in p for k in need) and \
		1920 <= int(p["byr"]) <= 2002 and \
		2010 <= int(p["iyr"]) <= 2020 and \
		2020 <= int(p["eyr"]) <= 2030 and \
		re.match(r"#\S{6}", p["hcl"]) and \
		re.match(r"(amb|blu|brn|gry|grn|hzl|oth)", p["ecl"]) and \
		re.fullmatch(r"\d{9}", p["pid"]) and \
		re.match(r"\d*(cm|in)", p["hgt"]):
			height = re.match(r"\d*(cm|in)", p["hgt"]).group(0)
			unit = height[len(height)-2:]
			num = int(height[:len(height)-2])
			if (unit == "cm" and 150 <= num <= 193) or (unit == "in" and 59 <= num <= 76):
				valid += 1

for i in passports:
	checkPassport(i)

print(valid)