# Ingest list of equations, and evaluate with + having priority over *
# https://adventofcode.com/2020/day/18

import re

expressions = open('input').read().split('\n')

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

# Look for +. Evaluate them, and replace them with their eval until no more *, then evaluate
def add(expression):
	while True:
		matches = additionPattern.findall(expression)
		if len(matches)>0 and "*" in expression:	# if no * we can just eval
			for match in matches:
				expression = expression.replace(match, str(eval(match)),1)
		else:
			expression = eval(expression)
			break
	return expression

total = 0
for expression in expressions:
	total += paren(expression)
print(total)