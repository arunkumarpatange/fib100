

def search(list, n):

	count = [0]
	def _search(list, i, j, n):
		mid =  (i + j) / 2
		if list[mid] == n:
			return mid
		if i == mid:
			return i

		if n > list[mid]:
			return _search(list, mid, j, n)
		return _search(list, i, mid, n)

	return _search(list, 0, len(list), n)



assert search([1, 2, 3, 4], 1) == 0
assert search([1, 2, 3, 4], 2) == 1
assert search([1, 2, 3, 4], 3) == 2
assert search([1, 2, 3, 4,5, 6,7], 4) == 3
assert search([1, 2, 3, 4,5, 6,7], 7) == 6
assert search([1, 2, 3, 4], 6) == 3
assert search([1, 2, 3, 4], 0) == 0
assert search([1, 3, 5, 7], 4) == 1
assert search([1, 3, 5, 7], 2) == 0
