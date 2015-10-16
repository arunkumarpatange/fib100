


def twosum(l, k):
	l = sorted(l)

	i, j = 1, 1
	while True:
		if l[i - 1] + l[-j] == k: 
			return True

		if l[i - 1] + l[-j] > k:
			j = j + 1
		else:
			i = i + 1

		if i > len(l) - j:
			return False

assert twosum([4, 3, 2, 5], 5)
assert not twosum([4, 3, 2, 5], 15)
assert twosum([4, 3, 2, 6, 5], 9)
assert twosum([4, 3, 2, 6, 5], 11)


def threesum(l, k):
	l = sorted(l)

	for m, n in enumerate(l, start=1):

		i, j = m + 1, 1
		while True:
			if l[i - 1] + l[-j] + n == k: 
				return True

			if l[i - 1] + l[-j] + n > k:
				j = j + 1
			else:
				i = i + 1

			if i > len(l) - j:
				break

assert threesum([4, 3, 2, 6, 5], 14)
