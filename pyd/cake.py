

def min_diff(l):
	min_price, max_price, profit = l[0], l[1], l[0] - l[1] 
	for i, n in enumerate(l[1:]):
		profit = min(profit, min_price - n)
		min_price = min(min_price, n)
		
	print profit 

min_diff([4, 3])
min_diff([4, 3, 5, 4, 4, 4])


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

def to_hex(num):
	hext = "0123456789ABCDEF"
	h = ""
	while num != 0 and num < 16 or num / 16 != 0:
		h = "{}{}".format(hext[num % 16], h)
		num = num / 16
	return h

print [ to_hex(x) for x in (1, 16, 15, 30, 32)]

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

#print "cached"
#print fib(50, {})
#print 'non-cached'
#print fib2(5)

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

def knapsack(list, n):

	if n == 0: return 1

	if (n < 0 or 
		len(list) == 0 and n >= 1): return 0

	y = knapsack(list[:-1], n)
	x = knapsack(list, n - list[-1]) 
	#print x, y, list, n
	return x + y

print "ksack %s" % knapsack([1, 2, 3], 4)


def point(a, b):
	if a['x'] > b['x']:
		a, b = b, a
	def xx():
		for x in (a['x'], a['x'] + a ['width']):
			for y in (a['y'], a['y'] + a ['height']):
				if ((x >= b['x'] and x <= (b['x'] + b['width'])) and
					(y >= b['y'] and y <= (b['y'] + b['height']))):
					print x, y
					return dict(
						x=b['x'],
						y=b['y'],
						height=a['y'] + a['height'] - b['y'],
						width=a['x'] + a['width'] - b['x'],
					)
	def yy():
		x, y = a['x'] + a ['width'], a['y'] + a['height']
		if ((x >= b['x'] and x <= (b['x'] + b['width'])) and
			(y >= b['y'] and y <= (b['y'] + b['height']))):
			print x, y
			return dict(
				x=b['x'],
				y=b['y'],
				height=a['y'] + a['height'] - b['y'],
				width=a['x'] + a['width'] - b['x'],
			)
	return xx(), yy()


print point(
	dict(x=2, y=2, width=5, height=5),	
	dict(x=3, y=3, width=5, height=5),	
)

print point(
	dict(x=2, y=2, width=5, height=5),	
	dict(x=8, y=8, width=5, height=5),	
)

print point(
	dict(x=2, y=2, width=5, height=5),	
	dict(x=3, y=3, width=1, height=1),	
)

print point(
	dict(x=3, y=3, width=1, height=1),	
	dict(x=3, y=3, width=1, height=1),	
)

print point(
	dict(x=3, y=3, width=1, height=1),	
	dict(x=4, y=3, width=1, height=1),	
)


def max_sum(list):

	s, prev = 0, 0
	for n in list:
		if n < 0:
			prev = 0 
			continue
		prev = s = max(n, prev + n)

	return s

assert max_sum([1, -1, 2, 3, 4, -2]) == 9 
assert max_sum([1, -1, 2, 3, 4, -2, 7,7]) == 14



def long_sub(list, max_sum=0):

	length = len(list)
	for i in range(length):
		for j in range(i+1, length):
			if list[j] > list[i]:
				sum = 1 + long_sub(list[j:])
				#if sum > max_sum:
				#	print list[i], list[j]
				max_sum = max(max_sum, sum)
				break

	return max_sum

print long_sub([14, 3, 2, 4, 15, 2, 28, 3, 6, 39, 7]) 
print "-------"
print long_sub([9, 2, 11, 1, 12, 3, 14, 6, 15, 7, 16])
