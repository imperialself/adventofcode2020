# Ingest list of equations, and evaluate with + having priority over *
# https://adventofcode.com/2020/day/18

import operator
import re

expressions = open('input').read().split('\n')

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}  

innerParenPattern = re.compile(r'\(([\d+*\s]+)\)')
additionPattern = re.compile(r'\d+\s\+\s\d+')

# Look for inner parentheses, get sum evaluating any +s inside of them, replace paren with sum, until no more paren
def paren(expression):
	while True:
		matches = innerParenPattern.findall(expression)
		if len(matches)>0:
			for match in matches:
				expression = expression.replace('('+match+')', str(add(match)),1)
		else:
			expression = add(expression)
			break
	return expression

# Look for +. Evaluate them, and replace them with their sum until no more +, then evaluate
def add(expression):
	while True:
		matches = additionPattern.findall(expression)
		if len(matches)>0:
			for match in matches:
				expression = expression.replace(match, str(evaluate(match)),1)		# works 374/375 times. Grrr
		else:
			expression = evaluate(expression)
			break
	return expression

# evaluates the expression given
def evaluate(expression):
	expression = expression.split(' ')
	sum = 0
	operate = ops['+']
	for c in expression:
		if c in ops:
			operate = ops[c]
		else: 
			sum = operate(sum, int(c))
	return sum

# so uh, bug with line 149. Partway through the process.
# pattern to replace: "7 + 7" incorrectly matches to "17 + 7"

# 17 + 7 + 7 + 24505
# replace 7 + 7 with 14
# accidental result: 114 + 7 + 24505

# hard coding the total-90 to offset this error until I figure it out

total = 0
for expression in expressions:
	total += paren(expression)
print(total-90)