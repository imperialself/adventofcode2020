import csv

input = []

with open('input1.csv', newline='') as csvfile:
	input1 = csv.reader(csvfile)
	for row in input1:
		input.append(row)

for x in input:
	for y in input:
		for z in input:
			sum = int(x[0]) + int(y[0]) + int(z[0])
			if sum == 2020:
				product = int(x[0]) * int(y[0]) * int(z[0])
				print("numbers: " + str(x + y + z))
				print("sum: " + str(sum))
				print("product: " + str(product))
				print("---------")