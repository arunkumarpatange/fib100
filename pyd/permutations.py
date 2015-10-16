


def permutate(str):
	'''
		ab
		ba
	'''
	if len(str) <= 1:
		return [str]
	vals = permutate(str[1:])
	r = []
	for i in vals:
		for j in range(len(i) + 1):
			r.append(i[:j] + str[0] + i[j:])

	return r

print permutate("abc")


def perm(str):

	if len(str) <= 1: yield str
	else: 
		for s in perm(str[1:]):
			for i in xrange(len(str)):
				print i, s, str, s[:i] + str[0:1] + s[i:]
				yield s[:i] + str[0:1] + s[i:]


print [s for s in perm('abc')]
