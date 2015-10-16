
def uniq(l):
	x = 0
	for n in l:
		x = n ^ x
	return x
print uniq([1, 2, 10, 1, 2])

def has_cycle(l, head):
	''' 
		1 - 2 - 3 - 4
			| 		|
			- - - - - 
	'''

	next = current = head
	while l.get(current) is not None:
		current = l.get(current)
		next = l.get(l.get(next))
		print current, next
		if next == current:
			return "cycle"
	return 'nox cycle'

print has_cycle({
	1: 2,
	2: 3,
	3: 4,
	4: 3,
}, 1)

def rev(l, head):
	def _rev(l, head):

		tail = head
		if l.get(head) is not None:
			tail = _rev(l, l.get(head))
			l[l.get(head)] = head

		return tail

	print _rev(l, head)
	if l.get(head) is not None:
		l.pop(head)
	return l

assert rev({1: None}, 1) == {1: None}
assert rev({1: 2}, 1) == {2: 1}
assert rev({1: 2, 2: 3}, 1) == {3: 2, 2: 1}
assert rev({1: 2, 2: 3, 3:4, 4:5}, 1) == {2: 1, 3: 2, 4:3, 5:4}

def pyramid(n):
	chr = 1
	j = 1
	for i in xrange(1, n + 1):
		space = "{}{}{}".format(' ' * (n - i), "".join([str(i)] * j), ' ' * (n - 1))
		j = j + 2 
		print space

pyramid(4)


print "min cost train"
def min_cost(path, start=0, end=None):

	_cost = path[start][end]
	for i in xrange(start + 1, end):
		_cost = min(_cost,
			min_cost(path, start, i) + min_cost(path, i, end))
	
	if start == 0:
		assert _cost == min_cost_dp(path, end=end), (start, end, _cost)
	return _cost

def min_cost_dp(path, start=0, end=None):

	d = [11111] * (end + 1)
	d[0] = 0
	for i in xrange(start, end + 1):
		for j in xrange(start + 1, end + 1):
			_cost = path[i][j]
			if d[j] > d[i] + _cost:
				d[j] = _cost + d[i]
	return d[end]

print min_cost([
	[0, 15, 80, 90],
	[-1, 0, 40, 50],
	[-1, -1, 0, 70],
	[-1, -1, -1, 0]
], end=3)


def rotate_sorted(list, k):
	start, end = 0, len(list) - 1

	while start < end:
		mid = (start + end) / 2

		if list[mid] == k:
			return True
		elif k < list[mid]:
			if list[e] < list[mid] and list[e] >= k:
				start = mid + 1
			else:
				end = mid - 1
		else:
			if list[s] > list[mid] and list[s] <= k:
				end = mid - 1
			else:
				start = mid + 1
