
def fact(n):
	v = 1
	while n > 1:
		v = v * n
		n = n - 1
	return v

assert fact(4) == 24
assert fact(5) == 120


def get_char_count(word, index):
	'''
		word[0] > word[1..]
	'''

	chars = [c for c in word[index + 1:] if c < word[index]]
	return len(chars)

assert get_char_count('string', 0) == 4
assert get_char_count('abc', 0) == 0


def get_rank(word):


	rank = 0
	for i in xrange(len(word)):
		#print get_char_count(word, i), word[i]
		count = {}
		for c in word[i:]:
			count[c] = count.setdefault(c,  0) + 1
		_rank =  (get_char_count(word, i) * (fact(len(word[i:]))) / (len(word) - i))
		use = [v for c, v in count.iteritems() if c < word[i]]
		print use
		rank = rank + _rank / reduce(lambda x, y: x * y, map(lambda x: fact(x), use), 1)
	print word, rank, count
	return rank

assert get_rank('abc') == 0
assert get_rank('acb') == 1
assert get_rank('bac') == 2
assert get_rank('cba') == 5
assert get_rank('aaa') == 0
assert get_rank('bbb') == 0
assert get_rank('aabb') == 0
assert get_rank('abab') == 1
assert get_rank('abba') == 2
assert get_rank('baab') == 3
assert get_rank('baba') == 4
assert get_rank('bbaa') == 5
assert get_rank('string') == 597
assert get_rank('question') == 24571
assert get_rank('bookkeeper') == 10742
