

def min_diff(l):
	min_price, max_price, profit = l[0], l[1], l[0] - l[1] 
	for i, n in enumerate(l[1:]):
		profit = min(profit, min_price - n)
		min_price = min(min_price, n)
		
	print profit 

min_diff([4, 3])
min_diff([4, 3, 5, 1, 1, 1])


def to_bin(num):
	b = 0 if num == 0 else ""
	rb = 0 if num == 0 else ""
	x = num
	while num == 1 or (num / 2) != 0:
		b = "{}{}".format((num % 2), b)
		rb = "{}{}".format(rb, (num % 2))
		num = num / 2
	print "{}: {}, {}".format(x, b, rb)

[to_bin(i) for i in xrange(8)]


def left_edge(list):
	list = sorted(list, cmp=lambda a, b: 1 if a[0] > b[0] else -1)
	left, right = list[0]
	_d = []
	for i, (l, r) in enumerate(list):
		if l <= right:
			right = max(r, right)
		else:
			_d.append((left, right))
			left, right = l, r
	_d.append((left, right))
	print _d

left_edge(((1, 2), (2, 3),))
left_edge(((1, 4), (1, 2), (1, 5), (1, 3), (2, 6),))
left_edge(((3, 4), (1, 2),))
left_edge([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])

_ = lambda list: enumerate(list)
def product(list):
	'''
		highest product
	'''
	prod = -1
	for i, l in _(list):
		for j, m in _(list[i + 1:]):
			for k, n in _(list[i + j + 1: ]):
				if prod < l * m * n:
					prod = l * m * n
	print prod

product([1, 2, -5, 3, -5])

def compose(list, n, total, set):
	''' 
		interger composition 2^n-1
		4: 1, 2, 3
		1 + 1 + 1 + 1
		1 + 3
		1 + 1 + 2
		2 + 2
	'''
	for i in list:
		total = total + i
		set.append(i)
		if total < n:
			compose(list, n, total, set[:])
		elif total == n:
			print total, set
		total = total - i
		set = set[:-1]


compose([1, 2, 3], 4, 0, [])

def fib(n, cache):
	if n in cache: return cache[n]
	cache[n] = n if n < 2 else fib(n-1, cache) + fib(n-2, cache)
	return cache[n]

def fib2(n):
	if n < 2: return n 
	return fib2(n-1) + fib2(n-2)

print "cached"
print fib(50, {})
print 'non-cached'
print fib2(5)

def fact(n):
	v = 1
	while n > 1:
		v = v * n
		n = n - 1
	return v
print fact(5)

def iterfib(n):
	fib = [1, 1]
	for i in xrange(2, n):
		fib.append(fib[i-1] + fib[i-2])
	return fib[n-1]

print iterfib(6)
