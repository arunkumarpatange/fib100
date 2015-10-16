

def egg(n, k):
	'''
		memoization
	'''
	_cache = {}
	def _egg(n, k):
		if n == 1 or k in (1, 0):
			return k

		_min = 10000
		for i in range(1, k + 1):
			if (n - 1, i - 1,) not in _cache:
				_cache.setdefault((n - 1, i - 1), _egg(n - 1, i - 1))
			if (n, k - i,) not in _cache:
				_cache.setdefault((n, k - i), _egg(n, k - i))
			count = max(_cache.get((n - 1, i - 1)), _cache.get((n, k - i)))
			_min = min(_min, count)

		return _min + 1
	v = _egg(n, k)
	return v




assert egg(2, 10) == 4, egg(2, 10)
assert egg(2, 100) == 14, egg(2, 100)
