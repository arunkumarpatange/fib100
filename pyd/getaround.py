def angle(time):
	hour, min = list(float(x) for x in time.split(":"))

	min_angle = min * 6
	hour_angle =  0.5 * ((hour % 12) * 60 + min)

	print abs(hour_angle - min_angle)


angle("12:00")
angle("1:05")
angle("3:30")


import re
def expression(exp):
	regex = r'\d+|[+/*-]'
	values = re.findall(regex, exp)
	print(values)
	v = div(values[::-1])
	v = v[::-1]
	v = mul(v)
	print addsub(v)


def div(list):
	'''
	reversed list
	'''
	l = []
	for i, s in enumerate(list):
		if s == '/':
			v = float(list[i + 1]) / float(list[i - 1])
			l = l[:-1] + [ v ] + list[i + 1 + 1:]
			return div(l)
		else:
			l.append(s) 
	return l

def mul(list):
	'''
	list
	'''
	l = []
	for i, s in enumerate(list):
		if s == '*':
			v = float(list[i + 1]) * float(list[i - 1])
			l = l[:-1] + [ v ] + list[i + 1 + 1:]
			return mul(l)
		else:
			l.append(s) 
	return l

def addsub(list):
	'''
	list
	'''
	l = []
	for i, s in enumerate(list):
		if s == '-' or s == "+":
			if s == '-':
				v = float(list[i - 1]) - float(list[i + 1])
			else: 
				v = float(list[i + 1]) + float(list[i - 1])
			l = l[:-1] + [ v ] + list[i + 1 + 1:]
			return addsub(l)
		else:
			l.append(s) 
	return l


q = '23 * 345 - 123 + 65 - 2'
q = '5 * 6 / 3 + 1'
expression(q)

print div([1, '/', 2])
print div(list(reversed([12, '/', 4, '/', 2])))

print mul([1, '*', 2, "*", 5])

print addsub([1, '-', 2, "-", 5])


expression('1+2')
expression('1+2*3')
expression('1+2*3/3')
expression('1+2*3/3*5')
expression('1+2*3/3*5-5')
