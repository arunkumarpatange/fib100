from __future__ import division

count = 0
def power_set(str):
	global count
	for i, sub in enumerate(str):
		yield sub
		count  = count + 1
		for c in power_set(str[i + 1:]):
			yield sub + c
			count  = count + 1

count = 0
assert set(power_set('abc')) == {'a', 'b', 'c', 'ab', 'bc', 'ac', 'abc'}
assert count == (len('abc') * 1.0/2 * 2**len('abc'))
count = 0
assert set(power_set("ab")) == {'a', 'b', 'ab'}
assert count == (len('ab') * 1.0/2 * 2**len('ab'))

def iter_power_set(_str):
	bins = [bin(i) for i in xrange(2 ** len(_str))]
	for b in bins:
		element = ""
		for set, c in zip("0" * (len(_str) - len(b[2:])) + b[2:], _str[::-1]):
			if set == '1':
				element = c + element
		yield element

assert set(iter_power_set('abc')) == {'', 'a', 'b', 'c', 'ab', 'bc', 'ac', 'abc'}

