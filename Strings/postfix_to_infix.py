class Term:

	def __init__(self, expr, op=None):
		self.expr = expr
		self.op = op

	def paranthesize(self):
		self.expr = '(' + self.expr + ')'

def postfix_to_infix(E):
	stack = []
	for c in E:
		term = None
		if c.isalnum():
			stack.append(Term(c))
		elif c != ' ':
			# operation. right term has to be popped regardless
			right = stack.pop()
			if not stack: 
				return 'invalid'
			# left needs to be processed as well
			left = stack.pop()

			# conditionals
			if c == '-' and right.op in ('+', '-'):
				right.paranthesize()
				
			elif c in ('*', '/'):
				if left.op in ('+', '-'):
					left.paranthesize()
				if right.op in ('+', '-') or c == '/':
					right.paranthesize()

			elif c == '^':
				if left.op != '^':
					left.paranthesize()
				if rght.op != '^':
					right.paranthesize()

			stack.append(Term(left.expr + c + right.expr, c))			
	if len(stack) > 1: return 'invalid'
	return stack[0].expr

if __name__ == '__main__':
	postfix = '123+*'
	infix = postfix_to_infix(postfix)
	print(infix)