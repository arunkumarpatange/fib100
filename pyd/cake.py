

def min_diff(l):
	min_price, max_price, profit = l[0], l[1], l[0] - l[1] 
	for i, n in enumerate(l[1:]):
		profit = min(profit, min_price - n)
		min_price = min(min_price, n)
		
	print profit 

min_diff([4, 3])
min_diff([4, 3, 5, 1, 1, 1])


def to_bin(num):
	b = 0 if num == 0 else ""
	x = num
	while num == 1 or (num / 2) != 0:
		b = "{}{}".format((num % 2), b)
		num = num / 2
	print "{}: {}".format(x, b)

[to_bin(i) for i in xrange(5)]
