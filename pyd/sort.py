

def partition(list):
	middle = len(list) / 2
	list[-1], list[middle] = list[middle], list[-1]
	pivot = list[-1]

	index = 0
	for i in xrange(len(list)):
		if pivot > list[i]:
			list[i], list[index] = list[index], list[i]
			index = index + 1

	list[-1], list[index] = list[index], list[-1]
	# print list, index
	return index

assert partition([5, 4, 3, 2, 1]) == 2
assert partition([4, 5, 1, 3, 8, 6]) == 1

def quick(list):
	if len(list) <= 1:
		return list

	index = partition(list)
	a, b = list[:index], list[index:]
	if index > 0:
		a = quick(a)
	if index > 0:
		b = quick(b)
	return a + b

print quick([4, 5, 1, 3, 8, 6])
print quick([4, 3, 5, 6, 8, 8, 8, 9, 0, 2, 3, 77, 10, 23])

def kth(list, k):

	middle = len(list) / 2
	list[-1], list[middle] = list[middle], list[-1]
	pivot = list[-1]
	index = 0

	for i in xrange(len(list)):
		if pivot > list[i]:
			list[i], list[index] = list[index], list[i]
			index = index + 1

	list[-1], list[index] = list[index], list[-1]


	if pivot == list[k]:
		return pivot

	if k < index:
		return kth(list[:index], k)
	return kth(list[index:], k - len(list[index:]))

print kth([1, 2, 3], 0)
print kth([4, 3, 5, 6], 2)
print kth([4, 3, 5, 6, 8, 8, 8, 9, 0, 2, 3, 77, 10, 23], 7)


def merge(a, b):
	if len(a) == 0 or len(b) == 0:
		return a + b

	if a[0] < b[0]:
		return [a[0]] + merge(a[1:], b)
	else:
		return [b[0]] + merge(a, b[1:])

def merge_sort(list):
	if len(list) <= 1: 
		return list

	l = len(list) / 2
	return merge(merge_sort(list[:l]), merge_sort(list[l:]))

print merge_sort([5, 4, 3, 2, 6])


def majority(list):
	c = 1
	prev = list[0]
	for n in list[1:]:
		if c == 0:
			prev = n
		elif n == prev:
			c = c + 1
		else:
			c = c - 1
	return prev

print majority([1, 2, 1, 3, 1, 4, 1, 1])
print majority([1, 1, 1, 1, 2, 1, 2, 2, 3, 3])


def amerisort(l):
	''' RB '''
	i, j = 0, len(l) - 1
	while i < j:
		if l[i] == 'B':
			l[i], l[j] = l[j], l[i]
			j = j - 1
		else:
			i = i + 1
	return l

print amerisort(list('RBBBRB'))

def amerisort2(l):
	''' RBY '''

	i, j, k = 0, len(l) - 1, 0
	while i < j:
		if l[i] == 'B':
			l[i], l[j] = l[j], l[i]
			j = j - 1
		if l[i] == 'R':
			l[i], l[k] = l[k], l[i]
			i = i + 1
			k = k + 1
		else:
			i = i + 1
	return l

print amerisort2(list('BBRYBRRY'))

def rev_sent(str):
	def rev(str, start=0, l=None):
		l = l or len(str)
		for i in xrange(l / 2):
			str[start + i], str[start + l - i - 1] = str[start + l - i - 1], str[start + i]

	i = 0
	def length():
		t = []
		for c in str:
			if c == ' ':
				yield len(t)
				t = []
			else:
				t.append(c)
		yield len(t)

	rev(str)
	x = 0
	for i, l in enumerate(length()):
		rev(str, x + i, l)
		x = x + l

	return str

print rev_sent(list('AB CD EF'))

def merge_sorted(a, b):

	sortd = []
	i, j = 0, 0
	while i < len(a) or j < len(b):
		if j >= len(b) or (i < len(a) and a[i] < b[j]):
			sortd.append(a[i])
			i = i + 1
		elif j < len(b):
			sortd.append(b[j])
			j = j + 1

	return sortd

print merge_sorted([1, 3, 5, 7, 9, 13], [2, 4, 6, 8, 10, 11, 12])
print merge_sorted([2, 4, 6, 8, 10, 11, 12], [1, 3, 5, 7, 9, 13])
print merge_sorted([1, 3, 5, 7, 9, 13], [0])

