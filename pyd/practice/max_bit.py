

def max_bit(binary):
	'''
		flip bits to get max set bits
	'''

	max_count = 0
	count = 0
	ones = 0
	start = 0
	for i, b in enumerate(binary):
		if b == '1':
			n = -1
			ones = ones + 1
		else:
			n = 1
	
		count = count + n
		if count < 0:
			count = 0
			start = i + 1
		_tmp = max_count
		max_count = max(max_count, count)
		if _tmp != max_count:
			print start, i

	return max_count + ones

assert max_bit('110001001') == 8
assert max_bit('10000') == 5





