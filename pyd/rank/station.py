
import heapq
def max_m(n, m, array):
	m = int(m)
	_m, __m = m, m
	n = int(n)
	array = map(int, array)
	q = []
	for i in array:
		heapq.heappush(q, -i)

	_max = 0
	count = 0
	while m > 0:
		count = count + 1
		val = heapq.heappop(q)

		_max = _max + -1 * val
		val = val + 1
		heapq.heappush(q, val)
		m = m - 1

	def _check(n, m, array):
		__m = m
		curr_max = 0
		prev_max = 0
		sum = 0
		array = [ a for a in sorted(array, reverse=True) ]
		while __m > 0:
			sum = sum + array[curr_max]
			array[curr_max] = array[curr_max] - 1
			__m = __m - 1
			if __m == 0:
				break
			if array[curr_max + 1] > array[curr_max]:
				curr_max = curr_max + 1
			elif array[curr_max] <= array[0]:
				curr_max = 0

		return sum
	
	assert _check(n, _m, array) == _max, _max

	return _check(n, _m, array)

assert max_m(10, 15, [9, 6, 7, 5, 4, 11, 3, 1, 8, 2]) == 115
assert max_m(2, 4, [2, 5]) == 14
assert max_m(3, 5, [2, 5, 3]) == 17
assert max_m(3000000, 2500000, [10] * 3000000) == 25000000
