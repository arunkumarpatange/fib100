
def product(A, k):

	if k == 1:
		for c in A:
			yield c
	else:
		for c in A:
			for d in product(A, k - 1):
				yield c + d

assert list(product('ABC', 2)) == ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']

def pivot(A):

	total = sum(A)
	_sum = 0
	_min = 100000
	for n in A:
		_sum = _sum + n
		_min = min(_min, abs(total - _sum - _sum))

	return _min
assert pivot([3, 1, 2, 4, 3]) == 1

def next_big(number):
	#yield list(number)

	def _get(number):
		for i in xrange(1, len(number)):
			if number[-i - 1] < number[ -i ]:
				break
		else:
			return None

		k = len(number) - i - 1
		for i in xrange(len(number) - 1, k, -1):
			if number[k] < number[i]:
				break
		l = i
		number[l], number[k] = number[k], number[l]
		return number[0:k + 1] + number[k + 1:][::-1]

	return _get(list(number))
#	while True:
#		number = str(number)
#		num = _get(list(number))
#		if num != None:
#			yield num
#			number = ''.join(num)
#		else:
#			break

assert next_big('aabb') == list('abab')

def _get_rank(word):
	_word = ''.join(sorted(word))
	count = 0
	if word == _word:
		return 0
	while True:
		_word = ''.join(next_big(_word))
		count = count + 1
		if _word == word:
			return count

assert _get_rank('abc') == 0
assert _get_rank('acb') == 1
assert _get_rank('baab') == 3
assert _get_rank('bookkeeper') == 10742

def get_path(A, B):

	def find(M, k):
		for i, n in enumerate(M): 
			if k == n: 
				yield i

	def path(index):
		#print index
		yield A[index]
		#yield B[index]
		for m in find(A, B[index]):
			#yield B[m]
			for x in path(m):
				yield x

	v = list(path(0))
	print 'v', v
	for n in v:
		yield n

def solution(A, B, k):
	C = '0' * (len(A) - k) + '1' * k

	for number in next_big(C):
		print number

A = [5, 1, 0, 2, 7, 0, 6, 6, 1]
B = [1, 0, 7, 4, 2, 6, 8, 3, 9]

assert list(get_path(A, B)) == ''
assert solution(A, B, 0) == 3
