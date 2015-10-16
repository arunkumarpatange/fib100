

def number(a):


	i, j, k = 0, 1, 0
	while True:

		if a[i] % 2 == 0:
			if j < len(a):
				a[j], a[i] = a[i], a[j]
				j = j + 2
		if a[i] % 2 != 0:
			if k < len(a):
				a[k], a[i] = a[i], a[k]
				k = k + 2
		i = i + 1
		if i >= len(a):
			break
	for i in xrange(len(a)):
		if i % 2 == 0:
			assert a[i] % 2 != 0, a
		else:
			assert a[i] % 2 == 0, a
	print a
	return a

assert number([2, 3, 4, 1]) == [3, 4, 1, 2]
assert number([1, 2, 3, 4]) == [1, 2, 3, 4]
assert number([4, 3, 2, 1]) == [3, 2, 1, 4]
assert number([2, 7, 4, 1, 5, 7, 4, 8]) == [7, 4, 5, 4, 1, 8, 7, 2]


def odd_even(array):

	m = 0
	i = 0
	j = len(array) - 1 
	while True:
		if array[m] % 2 == 0:
			array[m], array[i] = array[i], array[m]
			i = i + 1
		else:
			array[m], array[j] = array[j], array[m]
			j = j - 1
		
		m = m + 1
		if m >= len(array) - 1:
			break
	return array

assert odd_even([4, 3, 2, 1]) == [4, 2, 1, 3]
assert odd_even(range(1, 10 + 1)) == [2, 4, 6, 10, 3, 5, 7, 9, 8, 1]
