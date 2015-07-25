



#is_pal = lambda str: str == str[::-1]
#
#n = int(input())
#
#for sstr in [ raw_input() for i in range(n) ]:
#    if is_pal(sstr): 
#        print -1 
#        continue
#    for i, s in enumerate(sstr):
#        if is_pal(sstr[:i] + sstr[i+1:]):
#            print i
#            break

from itertools import count

def palindromes():
    """Generate numbers that are palindromes in base 10."""
    yield 0
    for digits in count(1):
		print (digits - 1, (digits - 1) // 2)
		first = 10 ** ((digits - 1) // 2)
		for s in map(str, range(first, 10 * first)):
			yield int(s + s[-(digits % 2)-1::-1])

dd = palindromes()
print [ dd.next()  for i in range(40) ]


soup = 'abcdefghijklmnopqrstuvwxyz'

a = input()
b = raw_input()
c = int(input())

cipher = ""
for s in b:
    ch = ord(s) + c % len(soup)
    if s in soup:
        cipher = cipher + ( chr(ord('a') + (ch % ord('z')) - 1) if ch > ord('z') else chr(ch) ) 
    elif s in soup.upper():
        cipher = cipher + ( chr(ord('A') + (ch % ord('Z')) - 1) if ch > ord('Z') else chr(ch) )
    else:
        cipher = cipher + s
        
print cipher
