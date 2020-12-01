# find two numbers in list that add to 2020, output the product of those two numbers

import csv

input = []

with open('input1.csv', newline='') as csvfile:
	input1 = csv.reader(csvfile)
	for row in input1:
		input.append(row)

for x in input:
	for y in input:
		sum = int(x[0]) + int(y[0])	
		if sum == 2020:
			print(str(x[0]) + " and " + str(y[0]))
			product = int(x[0]) * int(y[0])
			print("product: " + str(product))
