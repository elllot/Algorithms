"""

given a constraint that you're given a RNG for ints between 1-i, generate a random
number between 1-j
"""

def generate(i):
	one = random.randint(1, i) - 1
	two = random.randint(1, i) - 1
	calc = one * i + two

def random_number(i, j):
	val = generate(i)
	tail = i ** 2 - 1
	_max = tail - tail % j - 1
	while val > _max:
		val = generate(i)
	return val

if __name__ == '__main__':
	random_number(5, 7)