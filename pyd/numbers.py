import math

def gcd(a, b):
	if b == 0:
		return a

	return gcd(b, a % b)

assert gcd(4, 5) == 1
assert gcd(10, 5) == 5
assert gcd(3, 9) == 3

def max_sum(list):

	sum = 0
	max_val = list[0]
	for i in list:
		sum = sum + i
		max_val = max(max_val, sum)
		if i < 0:
			sum = 0
	return max_val

assert max_sum([1, -2, 3]) == 3
assert max_sum([1, 2, -2, 3]) == 3


def to_n_ary(number, ary=2):
	nary = ""
	n = number
	while n !=0 :
		nary = str(n % ary) + nary
		n = n / ary
	return nary

def nary_to_number(nary, ary=2):
	number = 0 
	for index, n in enumerate(nary[::-1]):
		number = number + int(n) * (ary ** index)	
	return number

assert nary_to_number(to_n_ary(10)) == 10
assert nary_to_number(to_n_ary(6)) == 6
assert nary_to_number(to_n_ary(3)) == 3
assert nary_to_number(to_n_ary(12, 3), 3) == 12
assert nary_to_number(to_n_ary(5, 3), 3) == 5

def uniq(lisst, rep=2):
	total = 0
	_list = []
	for n in lisst:
		_list.append(int(to_n_ary(n, rep)))

	_list_ = [''] * 10
	for i, n in enumerate(_list):
		i = 0
		while n != 0:
			_list_[i] = "{}{}".format(_list_[i], n % 10)
			i = i + 1
			n = n / 10
	add = [ map(int, list(nary)) for nary in _list_ if nary]
	add = ('{}'.format(sum(n) % rep) for n in add[::-1] if n != '')
	return nary_to_number(''.join(list(add)), rep)

assert uniq([1, 2, 3, 1, 2])  == 3
assert uniq([6, 6, 6, 1, 1, 1, 5], 3) == 5


def composite(list, sum, num=""):
	''' with repetion '''

	if sum < 0:
		yield ""
	elif sum == 0:
		yield "".join(sorted(num))
	else:
		for n in list:
			for v in composite(list, sum - n, num + str(n)):
				if v != "":
					yield v

print set(composite([4, 3, 1, 2], 4))
#print set(composite([4, 3, 1, 2], 10))


def subseq(list, max_seq=0):
	'''
		longest increasing subsequence
	'''

	max_count = 0
	for i, m  in enumerate(list):
		start = m
		max_seq = 0
		for j, n in enumerate(list[i + 1:]):
			if n > start:
				#max_seq = max(max_seq, 1 + subseq(list[i + 1 + j:]))
				#break
				start = n
				max_seq = max_seq + 1
		max_count = max(max_count, max_seq)

	return max_count + 1

assert subseq([10, 9, 5, 2, 6, 1, 9, 11]) == 4
assert subseq([10, 22, 9, 33, 21, 50, 41, 60]) == 5
#print subseq([10, 22, 9, 13, 21, 50, 41, 60, 80, 10, 10, 10, 90])
#print subseq([9,13,21,50,60,80,90])

def next_big(str):
	'''
	1. a[k] < a[k + 1]
	2. a[k] < min(a[l]) | l > k

	'''
	dbg = int(str)
	l = len(str)
	str = list(str)
	while True:
		for i in xrange(1, l + 1):
			if i != l:
				if str[ -i - 1] < str[-i]:
					break
		else:
			break
		j = 1
		g = str[-i]
		l = i
		i = i + 1
		while -j >= -i:
			if str[-i] < str[-j]:
				if g > str[-j]:
					g = str[-j]
					l = j
					break
			j = j + 1

		str[-i], str[-l] = str[-l], str[-i]
		str = str[:-i + 1] + sorted(str[-i + 1:])
		if dbg == 517639842:
			print i, j, l, str
		yield "".join(str)


assert next(next_big("517639842"), None) == "517642389"
assert next(next_big("4321"), None) is None
assert next(next_big("8967125430")) == "8967130245"
assert next(next_big("1342")) == "1423"
assert next(next_big("34722641"), None) == "34724126"
assert next(next_big("1231"), None) == "1312"
assert next(next_big("1432"), None) == "2134"
assert next(next_big("3241"), None) == "3412"
assert next(next_big("132"), None) == "213"
#print list(next_big("122222"))


def max_product(list):

	curr = 1
	_max, _min = 1, 1
	for i, m  in enumerate(list):
		if m > 0:
			_max = _max * m
			_min = min(_min * m, 1)
		else:
			if m == 0:
				_max, _min = 1, 1
			else:
				_ = _max
				_max = max(_min * m, 1) 
				_min = _ * m 
		curr = max(curr, _max)

	return curr

assert max_product([10, -1, -3,  0, 40]) == 40
assert max_product([6, -3, -10,  0, 2]) == 180
assert max_product([-2, -3, 0, -2, -40]) == 80
assert max_product([1, 1, -1, 3]) == 3
assert max_product([-2, -2, 5]) == 20
assert max_product([3, -1]) == 3
assert max_product([1, 1, -1, 3, 1, -5]) == 15

def min_product(list):

	curr = 1
	_max, _min = 1, 1
	for i, m  in enumerate(list):
		if m > 0:
			_max = _max * m
			_min = min(_min * m, 1)
		else:
			if m == 0:
				_max, _min = 1, 1
			else:
				_ = _max
				_max = max(_min * m, 1) 
				_min = _ * m 
		curr = min(curr, _min)

	return curr

#print '****** min ******'
assert min_product([0, 2, 2]) == 1 #TODO
assert min_product([1, 1, -1, 3, 1, -5]) == -15
assert min_product([-2, -2, 5]) == -10


def shortest_square(number):

	nums = [ i for i in xrange(1, number + 1) if i ** 2 <= 12]

	number = [number]
	def _composite(nums, total=0, path=''):
		if total > number[0]:
			pass
		elif total == number[0]:
			#do something
			yield path
		else:
			for i in nums:
				for s in _composite(nums, total + i**2, path + str(i)):
					yield s

	return min(_composite(nums), key=lambda x: len(x))


assert shortest_square(12) == '222'

def missing(l):
	nums = [i for i in xrange(100)]

	prev = -1
	for i in l:
		xy = nums[prev + 1:i]
		yield '%s-%s' % (xy[0], xy[-1])
		prev = i

	xy = nums[prev + 1:]
	yield '%s-%s' % (xy[0], xy[-1])

assert list(missing([1, 5, 45, 86])) == ['0-0', '2-4', '6-44', '46-85', '87-99']


def int_composition(number):
	#nums = [i for i in xrange(1, number + 1) if i**2 <= number][::-1]
	nums = [i for i in xrange(1, number + 1) if i**2 <= number]

	opt = None
	for n in nums:
		j = n
		m = number
		total = []
		while m > 0 and j > 0:
			if  m - j ** 2 >= 0:
				total.append(j)
				m = m - j ** 2
			else:
				j = j - 1

		if opt is None or len(opt) > len(total):
			opt = total

	print opt
	return opt

assert int_composition(12) == [2, 2, 2]
assert int_composition(11) == [3, 1, 1]


def int_comp2(num):

	def _int_comp2(num, path):
		if num == 0:
			yield path
		elif num > 0:
			for n in xrange(1, num + 1):
				for p in _int_comp2(num - n, path + [n]):
					yield p

	return _int_comp2(num, [])

#assert min(int_comp2(12), key=lambda l: len(l)) == '222'
#assert min(int_comp2(12), key=lambda l: len(l)) == [11, 1]


def comb_digit(length):
	'''
		01 02 ... 98

	'''
	count = [0]
	def _comb(length, start=1):
		if length == 1:
			for n in xrange(0, 10):
				yield str(n)
		else:
			for n in xrange(0, 10):
				for i in _comb(length - 1, n):
					if str(n) not in i:
						yield '{}{}'.format(n , i)
					count[0] = count[0] + 1
	
	v = list(_comb(length))
	return v

assert comb_digit(2) == [
	'%02d' % x for x in xrange(0, 99)
	if x not in [ 11 * i for i in range(0, 10)]
]

def sub_zero_length(l):
	'''
						  / [1, -1]
		[1, -1, 2, -1, -1] 				-> 3
						  \ [1, -1, 2]

	'''
	_d = {}
	sum = 0
	max_len = 0
	for i, n in enumerate(l):
		sum = sum + n

		if sum == 0:
			max_len = i + 1
		

		prev = _d.setdefault(sum, i)
		max_len = max(max_len, i - prev)

	return max_len

assert sub_zero_length([-1, 1, 2, -1, -1]) == 5
assert sub_zero_length([-1, 3, 2, -1, -1, -2]) == 6


def two_sum(l, v):

	i = 0
	j = len(l) - 1
	while True:

		if l[i] + l[j] == v:
			return True

		if l[i] + l[j] > v:
			j = j - 1
		else: 
			i = i + 1
		if i >= j:
			break

assert two_sum([1, 3, 5, 7], 10)
assert two_sum([1, 3, 5, 7], 20) is None


def largest(list):
	'''
		[1, 2, 50, 9] = > 95021 or 12509
	'''
	def _cmp(a,b):
		# print a, b
		return cmp('%s%s' % (a, b), '%s%s' % (b, a)) 
	return sorted(list, cmp=_cmp, reverse=True)

assert largest([1, 2, 50, 9]) == [9, 50, 2, 1]
assert largest([420, 42, 423]) == [42, 423, 420]
