

def preprocess(list):

	MAX = 99999999
	cache = {}
	_len = len(list)
	for i in xrange(len(list)):
		for j in range(_len)[i:]:
			_max = min(cache.get((i, j - 1), MAX), list[j])
			cache.setdefault((i, j), _max)
	return cache

assert preprocess([2, 3, 4, 1]) == {
	(0, 0): 2, 
	(0, 1): 2,
	(0, 2): 2,
	(0, 3): 1,
	(1, 1): 3, 
	(1, 2): 3, 
	(1, 3): 1, 
	(2, 2): 4,
	(2, 3): 1, 
	(3, 3): 1,}

assert preprocess([-2, 7, -4, 5, 8, 2, 10])[2, 4] == -4
assert preprocess([-2, 7, -4, 5, 8, 2, 10])[4, 6] == 2
