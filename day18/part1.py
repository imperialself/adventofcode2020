# Ingest list of equations, and evaluate with + having same priority as *
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

# Look for inner parentheses. Evaluate them, and replace them with their sum until no more paren, then evaluate
def paren(expression):
	while True:
		matches = innerParenPattern.findall(expression)
		if len(matches)>0:
			for match in matches:
				expression = expression.replace('('+match+')', str(evaluate(match)),1)
		else:
			expression = evaluate(expression)
			break
	return expression

# Evaluate expression operation by operation, no priority for any operand
def evaluate(expression):
	print(expression)
	expression = expression.split(' ')
	sum = 0
	operate = ops['+']
	for c in expression:
		if c in ops:
			operate = ops[c]
		else: 
			sum = operate(sum, int(c))
	return sum


total = 0
for expression in expressions:
	total += paren(expression)
print(total)