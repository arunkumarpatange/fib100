

__count = [0]
def permutate(str):

	if len(str) <= 1:
		yield str
		__count[0] = __count[0] + 1
	else:
		for i in xrange(len(str)):
			for s in permutate(str[1:]):
				yield s[:i] + str[0:1] + s[i:]
				__count[0] = __count[0] + 1

assert list(permutate('abc')) == [
	'abc', 'acb', 'bac', 'cab', 'bca', 'cba'
]
assert __count[0] == 18 # n * n!


def num_pad(num):
	num = str(num)
	_d = {
		'1': "abc",
		'2': "def",
		'3': "ghi",
	}
	if (len(num)) <= 1:
		for c in _d.get(num):
			yield c
	else:
		for c in _d.get(num[0]):
			for n in num_pad(num[1:]):
				yield c + n

print list(num_pad(123))

def combinat(length, str):
	if length <= 1:
		for c in str:
			yield c
	else:
		for comb in combinat(length-1, str):
			for c in str:
				yield comb + c
				#yield c + comb

print list(combinat(2, "abc"))
print list(combinat(3, "ab"))

def get_string(N, K):
	count = 0
	prev = 'B'
	ays = 0
	for str in combinat(N, "AB"):
		for c in str:
			if c == 'A':
				prev = c
				ays = ays + 1
			if prev == 'A':
				if c == 'B':
					count = count + ays
		if count == K:
			return str
		count = 0
		ays = 0
		prev = 'B'
	return ""

print get_string(3, 2)
print get_string(2, 0)
print get_string(5, 8)
print get_string(10, 12)




def sevenOfNine(numbers):
	_sum = sum(numbers)
	k = -1
	for i, n in enumerate(numbers):
		for j, _n in enumerate(numbers[i + 1:]):
			if k != -1: continue
			if _n + n == (_sum - 100):
				k = i + j + 1
				break
		else:
			if k != i:
				yield n

print list(sevenOfNine([94, 1, 1, 1, 1, 1, 1, 1, 1]))
print list(sevenOfNine([7, 8, 10, 13, 15, 19, 20, 23, 25]))

def combination(str):
	'''
		ABCD => A	AB ABC ABCD
				B	BC BCD
				C	CD
				D
	'''

	for i, c in enumerate(str, 1):
		yield c
		for j in xrange(len(str[i:])):
			yield c + str[i : i + j + 1]

print list(combination('A'))
print list(combination('AB'))
print list(combination('ABCD'))
