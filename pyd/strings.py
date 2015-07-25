
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
