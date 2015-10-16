from pyd.datastructure import Stack

def is_funny_or_not(str):
	for i in xrange(1, len(str)/2 + 1):
		print abs(ord(str[i]) - ord(str[i-1])) 
		print abs(ord(str[-i]) - ord(str[-i-1])) 
		if abs(ord(str[i]) - ord(str[i-1])) != abs(ord(str[-i]) - ord(str[-i-1])): 
			print "Not Funny"
			break
	else:
			print "Funny"

is_funny_or_not('acxz')
is_funny_or_not('ivvkx')


def pangram(str):
	str = str.lower()
	print str
	soup = set("".join(chr(i) for i in xrange(ord('a'), ord('z') + 1)))
	print ("pangram", "not pangram")[soup != set("".join((c for c in str if c in soup)))]


pangram("".join(chr(i) for i in xrange(ord('a'), ord('z') + 1)))
pangram('We promptly judged ntique ivory uckles for the next prie')


from itertools import groupby

def dupes(str):
	print sum(len(list(y)) - 1  for x, y in groupby(str))

dupes('abab')



def canPalin(str):
	str = sorted(str)
	r = (len(list(y)) for x, y in groupby(str))
	if len(str) % 2 == 0:
		if len([n for n in r if n % 2 != 0]) == 0:
			print "Yes"
		else: print "NO"
	else:
		if len([n for n in r if n % 2 != 0]) != 1:
			print "NO"
		else:
			print "Yes"
canPalin('aaaa')
canPalin('aaax')
canPalin('aaaxa')
canPalin('aaabbbb')


def permutation(str):
	if (ord(str[i]) < ord(str[i + 1])):
		str[i], str[i + 1] = str[i + 1], str[i]
		str = str[:i] + str[i:][:: -1]
		print str
	permutation(str)


def is_ana(a, b):
	b = {x:len(list(y)) for x, y in groupby(sorted(b))}
	a = {x:len(list(y)) for x, y in groupby(sorted(a))}

	for s in a: b.setdefault(s, 0)
	for s in b: a.setdefault(s, 0)
	val = 0
	for s, n in a.iteritems():
		val  = val + abs(b[s]- n)
	print val

is_ana('ccd', 'cced')
is_ana('ccc', 'aaa')
is_ana('imkhnpqnhlvaxlmrsskbyyrhwfvgteubrelgubvdmrdmesfxkpykprunzpustowmvhupkqsyjxmnptkcilmzcinbzjwvxshubeln', 'wfnfdassvfugqjfuruwrdumdmvxpbjcxorettxmpcivurcolxmeagsdundjronoehtyaskpwumqmpgzmtdmbvsykxhblxspgnpgfzydukvizbhlwmaajuytrhxeepvmcltjmroibjsdkbqjnqjwmhsfopjvehhiuctgthrxqjaclqnyjwxxfpdueorkvaspdnywupvmy')


def bin_search(list, c):
	middle = len(list) / 2
	to = list[middle]

	if len(list) == 1 and to != c:
		return -1

	if c == to:
		return 1
	if c > to:
		return bin_search(list[middle:], c)
	if c < to:
		return bin_search(list[:middle], c)

print bin_search('123456', '1')
print bin_search('123456', '7')
print bin_search('abcd', 'a')



def rev(str):
	# convinient string split into chars
	str = list(str)
	for i in xrange(len(str) / 2):
		str[i], str[-i - 1] = str[-i - 1], str[i]
	return "".join(str)

print rev("abcd")
print rev("abcde")




def lint(parens):
	stack = Stack()
	#parens_d = "[], {}, ()"		
	parens_d = {
		"(":")",
		"{":"}",
		"[":"]",
	}

	for p in parens:
		if p in parens_d:
			stack.push(p)
		else:
			c = stack.pop()
			if p != parens_d.get(c):
				stack.push(c)
			if c is None:
				break
	else:
		return stack.pop() is None or 'not linted'
	return "not linted"


print lint("((()))")
print lint("((())")
print lint("(()))") # False
print lint("{[(()())]}")
print lint("{[(])}")
print lint("{[()()(]}")

def palindrome(str):
	parity = [ -1 ] * (ord('z') - ord('a') + 1)
	for c in str:
		index = ord(c) % ord('a')
		parity[index] = 1 if parity[index] == 0 else 0
	
	p = (p for p in parity if p != -1)
	if len(str) % 2 == 0:
		return 0 not in list(p)
	return 0 in list(p)
print '-----'
print palindrome('civic')
print palindrome('iivv')
print palindrome('ivxvgg')
print palindrome('zz')


def BoyerMoore(str, pattern):

	p = len(pattern) - 1
	i = p
	while i < len(str):
		if pattern[-1] == str[i]:
			if pattern == str[i - p: i + 1]:
				return i - p
		elif p == 0 or pattern[-2] == str[i]:
			i = i + 1
			continue
		i = i + p
	return -1

assert BoyerMoore("abcde", 'cde') == 2
assert BoyerMoore("abcde", 'cx') == -1

def rm_dupes(str):
	_str = set()

	for c in str:
		if c not in _str:
			_str.add(c)
			yield c

print "".join(list(rm_dupes("abbcxx")))

def get_st(str, width):

	count = 0
	for i in xrange(len(str)):
		_str = ''
		for j in xrange(width):
			if i + j < len(str):
				_str = _str + str[i + j]
				#yield str[i : i + j + 1]
				yield _str
			else:
				#print 'brea'
				break
			count = count + 1
	print 'c', count

assert list(get_st('ABC', 2)) == ['A', 'AB', 'B', 'BC', 'C']
assert list(get_st('ABC', 3)) == ['A', 'AB', 'ABC', 'B', 'BC', 'C']


count = [0]
def permutate(n, l):

	def _permutate(n, l):
		if n == 1:
			count[0] = count[0] + 1
			yield ''.join(l)
		else:
			for i in xrange(0, n - 1):
				for y in _permutate(n - 1, l):
					count[0] = count[0] + 1
					yield y
				if n % 2 == 0:
					l[i], l[n - 1] = l[n - 1], l[i]
				else:
					l[0], l[n - 1] = l[n - 1], l[0]
				count[0] = count[0] + 1
		
			for y in _permutate(n - 1, l):
				yield y

	return _permutate(len(l), list(l))

assert list(permutate(3, 'ABC')) == ['ABC', 'BAC', 'CAB', 'ACB', 'BCA', 'CBA']

assert count[0] == 18 # n * n!
