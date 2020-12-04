# process passport batch file and check for required fields

import re 

passportList = open('input').read().strip().split('\n\n')

# List of required fields to check for
need = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def checkPassport(passportList):
    valid = 0
    for i in passportList:
        # Make sure it has ALL required fields
        if re.search(need[0], i) and \
           re.search(need[1], i) and \
           re.search(need[2], i) and \
           re.search(need[3], i) and \
           re.search(need[4], i) and \
           re.search(need[5], i) and \
           re.search(need[6], i):
              valid += 1
    print(valid)

checkPassport(passportList)