
def spiral(matrix):

	row = len(matrix)
	col = len(matrix[0])

	r = (0, row)
	c = (0, col)

	while True:
		m, n = r
		x, y = c

		h = ""
		for i in xrange(x, y):
			h = h + ' ' + matrix[m][i]
		print h

		v = ""
		for j in xrange(m + 1, n):
			v = v + ' ' + matrix[j][y - 1]
		print v

		if m >= n - 1: break
		h = ''
		for i in xrange(y - 2, x, -1):
			h = h + ' ' + matrix[n - 1][i]
		print h

		if x > y - 2: break
		v = ""
		for j in xrange(n - 1, m, -1):
			v = v + ' ' + matrix[j][x]
		print v

		r = (m + 1, n - 1)
		c = (x + 1, y - 1)
		if (
			r[0] >= r[1] or
			c[0] >= c[1]
		):	
			break


spiral([
	"a",
])
print "-------------"
spiral([
	"a",
	"b",
	"c",
])
print "-------------"
spiral([
	"ab1m",
])
print "-------------"
spiral([
	"ab1m",
	"hc2n",
	"gd3o",
])


def get_adj(i, j, M, N):

	for l in (i, i + 1, i - 1):
		for m in (j, j + 1, j - 1):
			if l >=0  and l < M:
				if m >= 0 and m < N:
					if (l, m) != (i, j):
						yield (l, m)


assert list(get_adj(1, 1, 3, 3)) == [(1, 2), (1, 0), (2, 1), (2, 2), (2, 0), (0, 1), (0, 2), (0, 0)]


def words(M, str=""):

	r = len(M)
	c = len(M[0])
	B = [[False] * c for i in range(r)]

	def print_words(M, i, j, str):
		B[i][j] = True

		if str in _words:
			yield str

		for l, m in get_adj(i, j, r, c):
			if not B[l][m]:
				for s in print_words(M, l, m, str + M[l][m]):
					yield s
		B[i][j] = False

	for i in xrange(r):
		for j in xrange(c):
			for s in print_words(M, i, j, M[i][j]):
				yield s


_words = "exmda xe bex xeb adef abcx def ae aeg dm md".split(' ')

assert set(words([
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['m', 'x', 'g'],
])) == (set(_words) - {'abcx'})


def diag_matrix(M, _print=False):
	row = len(M) - 1
	col = len(M[0]) - 1

	i = 0
	j = 0
	while True:
		r, c = i, j 
		_str = ""
		while True:
			_str = _str + str( M[r][c] )
			if r == 0 or c == col:
				break
			r = r - 1
			c = c + 1
		yield _str
		if _print:
			print _str

		if i == row and j == col:
			break

		if i < row:
			i = i + 1
		else:
			j = j + 1

		

assert list(diag_matrix([
	[1, 2, 3],
	[4, 5, 6]	
])) == "1,42,53,6".split(',')

assert list(diag_matrix([
	[1, 4],
	[2, 5],	
	[3, 6]
])) == '1,24,35,6'.split(',')

assert list(diag_matrix([[1, 4]], True)) == "1,4".split(',')

assert list(diag_matrix([
	[1, 4, 7],
	[2, 5, 8],	
	[3, 6, 9]
], True)) == '1,24,357,68,9'.split(',')


assert list(diag_matrix([
[1 ,2 ,3 , 4],
[5 , 6 ,7 ,8],
[9 , 10,11,12],
[13, 14,15,16],
[17, 18,19,20],
], True)) == '1,52,963,131074,1714118,181512,1916,20'.split(',')


def rot_matrix(m):
	pass








assert rot_matrix([
	list('abc')
	list('def')
	list('ghi')
]) == [
		list("gda")
		list("heb")
		list("ifc")
		
	]
