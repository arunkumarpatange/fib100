

def max_product(array):
	'''
		[10, -1, -3, 0, 40] => 40
	'''

	_max = 1
	_min = 1
	current = -1

	for n in array:
		if n == 0:
			_max, _min = 1, -1
		elif n > 0:
			_max = max(_max * n, _max)
			_min = min(_min * n, 1)
		else:
			_tmp = _max
			_max = max(_min * n, _max)
			_min = min(_tmp * n, _min)

		current = max(_max, current)
	#print current
	return current

assert max_product([10, -1, -3,  0, 40]) == 40
assert max_product([6, -3, -10,  0, 2]) == 180
assert max_product([-2, -3, 0, -2, -40]) == 80
assert max_product([1, 1, -1, 3]) == 3
assert max_product([-2, -2, 5]) == 20
assert max_product([3, -1]) == 3
assert max_product([1, 1, -1, 3, 1, -5]) == 15



def prev_num(number):
	'''
		3 4 1 2
		3 _ 1 2
		3 x_ 1 y_
		3 y_ 1 x_
		3 2 4 1
	'''

	def _max(l, k):
		_index = 0
		_m = l[0]
		for index, n in enumerate(l[1:], start=1):
			if _m < n and n <= k:
				_m = n
				_index = index
		return _index

	number = list(str(number))
	j = len(number) - 1
	_sub = ""
	while j >= 0:
		_sub = number[j + 1:] or [number[j]]
		if number[j] > min(_sub):
			_max_index = _max(_sub, number[j])
			number[j], number[j + _max_index + 1] = number[j + _max_index + 1], number[j]
			break
		j = j - 1

	print int("".join(number[:j + 1] + sorted(number[j + 1:], reverse=True)))
	return int("".join(number[:j + 1] + sorted(number[j + 1:], reverse=True)))

assert prev_num(3412) == 3241
assert prev_num(213) == 132
assert prev_num(444) == 444
