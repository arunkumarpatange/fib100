

def permutation(parens):

	def _perm(parens):
		if len(parens) == 1:
			yield parens
		else:
			for i in xrange(len(parens)):
				for paren in _perm(parens[1:]):
					yield paren[:i] + parens[0:1] + paren[i:]
	# print list(_perm(parens))
	return _perm(parens)

assert next((permutation('ABC'))) == 'ABC'


def balance(n, open, close):

	open = [open]
	close = [close]

	def _balance(n, k, str):
		if k == 0 and n == 0:
			yield str

		if n > 0:
			for s in _balance(n - 1, k + 1, str + open[0]):
				yield s
		if k > 0:
			for s in _balance(n, k - 1, str + close[0]):
				yield s


	#print list(_balance(n, 0, ''))
	return _balance(n, 0, '')



assert list((balance(3, '(', ')'))) == ['((()))', '(()())', '(())()', '()(())', '()()()']
assert next((balance(5, '(', ')'))) == '((((()))))'


def dp_balance(n):

	str = []
	if n = 1:
		str.append(["()"])

	for i in xrange(n):
		for j in xrange(len(str[i])):
			



