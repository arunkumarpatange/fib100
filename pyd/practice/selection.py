
def partition(a):
	mid = len(a) / 2
	pivot = a[mid]
	i, j = 0, len(a) - 1

	a[j], a[mid] = a[mid], a[j]
	_j = j
	j = j - 1
	while i <= j:
		if a[i] > pivot:
			a[i], a[j] = a[j], a[i]
			j = j - 1
		else:
			i = i + 1

	a[_j], a[i] = a[i], a[_j]
	# a[_j], a[j] = a[j], a[_j]
	# print a, i, j
	return a, i

assert partition([5, 4, 3, 2, 1]) == ([2, 1, 3, 5, 4], 2)
assert partition([4, 5, 1, 3, 8, 6]) == ([1,3,6,8,4,5], 1)

def kth(array, k):

	#count = [0]
	def _kth(array, k):

		if len(array) == 1:
			return array[0]

		count[0] = count[0] + 1
		a, mid = partition(array)
		if mid == k:
			return array[k]

		if k < mid:
			return _kth(array[:mid], k)
		return _kth(array[mid:], k - mid)
	v = _kth(array, k)
	return v
# assert
count = [0]
def _assert(array, _count):
	global count
	for i in xrange(len(array)):
		count = [0]
		assert kth(array, i) == sorted(array)[i]
		assert count[0] == _count[i]
_assert([5, 4, 3, 2, 1], [2, 3, 1, 2, 2])
_assert([4, 5, 1, 3, 8, 6], [1, 4, 3, 1, 2, 2])
